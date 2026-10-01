#!/usr/bin/env python3
"""Generate REFs, per-shot keyframes and Seedance videos from anime_plan.json, then optionally join them.

Usage:
  python run_anime.py plan.json --check              # pre-generation check + count, no API calls
  python run_anime.py plan.json --stage refs         # REFs only
  python run_anime.py plan.json --stage keyframes    # second-0 frame of each i2v shot
  python run_anime.py plan.json --stage videos       # submit and download all videos
  python run_anime.py plan.json --only s09 --force   # regenerate specific shots
  python run_anime.py plan.json --concat             # join into final.mp4 with ffmpeg

Finished items are recorded in <out>/manifest.json and skipped on re-runs.
Submitted-but-not-downloaded video tasks keep their task id, so a re-run resumes
waiting instead of submitting (and paying) again.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ark  # noqa: E402
from i18n import set_lang, t  # noqa: E402

MAX_VIDEO_REFS = 5      # 4–5 per shot is the most stable in practice
MAX_IMAGE_REFS = 10
IMAGE_INDEX = re.compile(r"(?:image|圖|图|画像)\s*(\d+)", re.I)
AT_IMAGE_INDEX = re.compile(r"@Image\s*(\d+)")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check(plan, base_dir):
    errors = []
    refs = {r["id"]: r for r in plan.get("refs", [])}
    if not plan.get("style_anchor"):
        errors.append(t("err_style"))
    for r in plan.get("refs", []):
        if not r.get("prompt") and not r.get("file"):
            errors.append(t("err_ref_src", id=r["id"]))
        if r.get("file") and not os.path.exists(os.path.join(base_dir, r["file"])):
            errors.append(t("err_ref_file", id=r["id"], file=r["file"]))
    durations = set()
    seen = set()
    for s in plan.get("shots", []):
        sid = s.get("id")
        if sid in seen:
            errors.append(t("err_shot_dup", id=sid))
        mode = s.get("mode", "i2v")
        if mode not in ("i2v", "r2v"):
            errors.append(t("err_shot_mode", id=sid))
        if not s.get("video_prompt"):
            errors.append(t("err_shot_vprompt", id=sid))
        d = s.get("duration", plan.get("duration", 12))
        durations.add(d)
        if not 4 <= d <= 30:
            errors.append(t("err_shot_duration", id=sid, d=d))
        src = s.get("first_frame_from")
        if src:
            if mode != "i2v":
                errors.append(t("err_chain_mode", id=sid))
            elif src not in seen:
                errors.append(t("err_chain_order", id=sid, src=src))
        seen.add(sid)
        if mode == "i2v":
            if "@Image" in s.get("video_prompt", ""):
                errors.append(t("err_i2v_atimage", id=sid))
            if src:
                continue
            if not s.get("keyframe_prompt") and not s.get("keyframe_file"):
                errors.append(t("err_i2v_keyframe", id=sid))
            kr = s.get("keyframe_refs", [])
            if len(kr) > MAX_IMAGE_REFS:
                errors.append(t("err_kf_ref_count", id=sid, max=MAX_IMAGE_REFS))
            missing = [x for x in kr if x not in refs]
            if missing:
                errors.append(t("err_kf_ref_missing", id=sid, refs=missing))
            used = [int(x) for x in IMAGE_INDEX.findall(s.get("keyframe_prompt", ""))]
            if used and max(used) > len(kr):
                errors.append(t("err_kf_image_idx", id=sid, idx=max(used), n=len(kr)))
        elif mode == "r2v":
            vr = s.get("video_refs", [])
            if len(vr) > MAX_VIDEO_REFS:
                errors.append(t("err_vref_count", id=sid, n=len(vr), max=MAX_VIDEO_REFS))
            missing = [x for x in vr if x not in refs]
            if missing:
                errors.append(t("err_vref_missing", id=sid, refs=missing))
            used = [int(x) for x in AT_IMAGE_INDEX.findall(s.get("video_prompt", ""))]
            if used and max(used) > len(vr):
                errors.append(t("err_vref_idx", id=sid, idx=max(used), n=len(vr)))
    if len(durations) > 1 and not plan.get("allow_mixed_duration"):
        errors.append(t("err_mixed_duration", ds=sorted(durations)))
    return errors


def ref_path(out, rid, plan, base_dir):
    for r in plan.get("refs", []):
        if r["id"] == rid and r.get("file"):
            return os.path.join(base_dir, r["file"])
    return os.path.join(out, "refs", f"{rid}.png")


def lastframe_path(out, sid):
    return os.path.join(out, "lastframes", f"{sid}.png")


def keyframe_path(out, shot, base_dir):
    if shot.get("first_frame_from"):
        return lastframe_path(out, shot["first_frame_from"])
    if shot.get("keyframe_file"):
        return os.path.join(base_dir, shot["keyframe_file"])
    return os.path.join(out, "keyframes", f"{shot['id']}.png")


def save_manifest(out, manifest):
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def with_style(style, prompt):
    return prompt if prompt.startswith(style) else f"{style}\n{prompt}"


def concat(plan, out):
    if not shutil.which("ffmpeg"):
        print(t("no_ffmpeg"))
        return 1
    files = [os.path.join(out, "videos", f"{s['id']}.mp4") for s in plan.get("shots", [])]
    missing = [f for f in files if not os.path.exists(f)]
    if missing:
        print(t("videos_missing", files=missing))
        return 1
    listfile = os.path.join(out, "concat.txt")
    with open(listfile, "w", encoding="utf-8") as f:
        for p in files:
            f.write(f"file '{os.path.abspath(p)}'\n")
    final = os.path.join(out, "final.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile, "-c", "copy", final], check=True)
    print(t("concat_done", path=final))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--out", default=None)
    ap.add_argument("--stage", choices=["refs", "keyframes", "videos", "all"], default="all")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--concat", action="store_true")
    ap.add_argument("--poll", type=int, default=10, help="video task polling interval in seconds")
    args = ap.parse_args()

    plan = load(args.plan)
    set_lang(plan.get("lang"))
    base_dir = os.path.dirname(os.path.abspath(args.plan))
    out = args.out or os.path.join(base_dir, "output")
    os.makedirs(out, exist_ok=True)
    mpath = os.path.join(out, "manifest.json")
    manifest = load(mpath) if os.path.exists(mpath) else {}
    only = set(args.only) if args.only else None
    if args.force:
        for k in list(manifest):
            if only is None or k.split(":", 1)[1] in only:
                manifest.pop(k)

    if args.concat:
        return concat(plan, out)

    errors = check(plan, base_dir)
    if errors:
        print(t("check_failed"))
        for e in errors:
            print("  -", e)
        return 1

    def pick(items, prefix):
        return [x for x in items if (only is None or x["id"] in only) and manifest.get(prefix + x["id"]) != "done"]

    shots = plan.get("shots", [])
    todo_refs = pick([r for r in plan.get("refs", []) if r.get("prompt") and not r.get("file")], "ref:")
    todo_kf = pick([s for s in shots if s.get("mode", "i2v") == "i2v" and not s.get("keyframe_file")
                    and not s.get("first_frame_from")], "keyframe:")
    todo_vid = pick(shots, "video:")
    chained_from = {s["first_frame_from"] for s in shots if s.get("first_frame_from")}
    if args.stage not in ("refs", "all"):
        todo_refs = []
    if args.stage not in ("keyframes", "all"):
        todo_kf = []
    if args.stage not in ("videos", "all"):
        todo_vid = []
    secs = sum(s.get("duration", plan.get("duration", 12)) for s in todo_vid)
    print(t("anime_ok", refs=len(todo_refs), kf=len(todo_kf), imodel=ark.image_model(),
            vids=len(todo_vid), secs=secs, vmodel=ark.video_model()))
    if args.check:
        return 0
    if not os.environ.get("ARK_API_KEY"):
        print(t("key_missing_run"))
        return 1

    style = plan["style_anchor"]
    failed = []

    for r in todo_refs:
        print(t("running_ref", id=r["id"]))
        try:
            ark.generate_image(with_style(style, r["prompt"]), os.path.join(out, "refs", f"{r['id']}.png"),
                               size=r.get("size", "2K"))
            manifest["ref:" + r["id"]] = "done"
        except ark.ArkError as e:
            manifest["ref:" + r["id"]] = f"failed: {e}"
            failed.append(r["id"])
            print(t("item_failed", err=e))
        save_manifest(out, manifest)

    for s in todo_kf:
        paths = [ref_path(out, x, plan, base_dir) for x in s.get("keyframe_refs", [])]
        absent = [p for p in paths if not os.path.exists(p)]
        if absent:
            print(t("shot_ref_absent", id=s["id"], paths=absent))
            failed.append(s["id"])
            continue
        print(t("running_kf", id=s["id"]))
        try:
            ark.generate_image(with_style(style, s["keyframe_prompt"]), keyframe_path(out, s, base_dir),
                               ref_paths=paths, size=s.get("ratio", plan.get("ratio", "16:9")), seed=s.get("seed"))
            manifest["keyframe:" + s["id"]] = "done"
        except ark.ArkError as e:
            manifest["keyframe:" + s["id"]] = f"failed: {e}"
            failed.append(s["id"])
            print(t("item_failed", err=e))
        save_manifest(out, manifest)

    # Submit everything first (re-using recorded task ids), then wait and download.
    pending = []

    def finish(s, task_id):
        print(t("waiting", id=s["id"], tid=task_id))
        try:
            ark.wait_video(task_id, os.path.join(out, "videos", f"{s['id']}.mp4"), poll_seconds=args.poll,
                           last_frame_path=lastframe_path(out, s["id"]))
            manifest["video:" + s["id"]] = "done"
            if s["id"] in chained_from and not os.path.exists(lastframe_path(out, s["id"])):
                print(t("no_lastframe", id=s["id"]))
        except ark.ArkError as e:
            manifest["video:" + s["id"]] = f"failed: {e}"
            failed.append(s["id"])
            print(t("item_failed", err=e))
        manifest.pop("task:" + s["id"], None)
        save_manifest(out, manifest)

    for s in todo_vid:
        src = s.get("first_frame_from")
        if src:
            # A chained shot needs its source shot's last frame: finish that one first.
            for item in list(pending):
                if item[0]["id"] == src:
                    finish(*item)
                    pending.remove(item)
        tkey = "task:" + s["id"]
        if manifest.get(tkey):
            pending.append((s, manifest[tkey]))
            continue
        mode = s.get("mode", "i2v")
        kwargs = dict(duration=s.get("duration", plan.get("duration", 12)),
                      ratio=s.get("ratio", plan.get("ratio", "16:9")),
                      resolution=s.get("resolution", plan.get("resolution")),
                      generate_audio=s.get("generate_audio", plan.get("generate_audio", True)),
                      seed=s.get("seed"), return_last_frame=s["id"] in chained_from)
        try:
            if mode == "i2v":
                kf = keyframe_path(out, s, base_dir)
                if not os.path.exists(kf):
                    print(t("no_first_frame", id=s["id"]))
                    failed.append(s["id"])
                    continue
                last = s.get("last_frame_file")
                task_id = ark.create_video_task(with_style(style, s["video_prompt"]), first_frame=kf,
                                                last_frame=os.path.join(base_dir, last) if last else None, **kwargs)
            else:
                paths = [ref_path(out, x, plan, base_dir) for x in s.get("video_refs", [])]
                absent = [p for p in paths if not os.path.exists(p)]
                if absent:
                    print(t("shot_ref_absent", id=s["id"], paths=absent))
                    failed.append(s["id"])
                    continue
                task_id = ark.create_video_task(with_style(style, s["video_prompt"]), ref_paths=paths, **kwargs)
            manifest[tkey] = task_id
            save_manifest(out, manifest)
            print(t("submitted", id=s["id"], tid=task_id))
            pending.append((s, task_id))
        except ark.ArkError as e:
            manifest["video:" + s["id"]] = f"failed: {e}"
            failed.append(s["id"])
            print(t("item_failed", err=e))
            save_manifest(out, manifest)

    for s, task_id in pending:
        finish(s, task_id)

    if failed:
        print(t("n_failed", n=len(failed), ids=" ".join(sorted(set(failed)))))
        print(t("anime_retry"))
        return 2
    print(t("anime_done"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

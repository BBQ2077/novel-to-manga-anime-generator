#!/usr/bin/env python3
"""Generate REF sheets and every comic panel from comic_plan.json, plus an HTML page preview.

Usage:
  python run_comic.py plan.json --check                # pre-generation check + count, no API calls
  python run_comic.py plan.json --stage refs           # REFs only
  python run_comic.py plan.json --stage panels         # all panels (REFs must exist)
  python run_comic.py plan.json --only p05_3 --force   # regenerate specific panels
  python run_comic.py plan.json --preview              # HTML preview from the page layouts

Finished items are recorded in <out>/manifest.json and skipped on re-runs.
"""

import argparse
import html
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ark  # noqa: E402
from i18n import set_lang, t  # noqa: E402

MAX_REFS = 10
IMAGE_INDEX = re.compile(r"(?:image|圖|图|画像)\s*(\d+)", re.I)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check(plan, base_dir):
    """Hard pre-generation checks. Returns a list of errors."""
    errors = []
    refs = {r["id"]: r for r in plan.get("refs", [])}
    if not plan.get("style_anchor"):
        errors.append(t("err_style"))
    for r in plan.get("refs", []):
        if not r.get("prompt") and not r.get("file"):
            errors.append(t("err_ref_src", id=r["id"]))
        if r.get("file") and not os.path.exists(os.path.join(base_dir, r["file"])):
            errors.append(t("err_ref_file", id=r["id"], file=r["file"]))
    seen = set()
    for p in plan.get("panels", []):
        pid = p.get("id")
        if pid in seen:
            errors.append(t("err_panel_dup", id=pid))
        seen.add(pid)
        if not p.get("prompt"):
            errors.append(t("err_panel_prompt", id=pid))
            continue
        missing = [x for x in p.get("refs", []) if x not in refs]
        if missing:
            errors.append(t("err_panel_ref_missing", id=pid, refs=missing))
        n = len(p.get("refs", []))
        if n > MAX_REFS:
            errors.append(t("err_panel_ref_count", id=pid, n=n, max=MAX_REFS))
        used = [int(x) for x in IMAGE_INDEX.findall(p["prompt"])]
        if used and max(used) > n:
            errors.append(t("err_panel_image_idx", id=pid, idx=max(used), n=n))
    panel_ids = {p["id"] for p in plan.get("panels", [])}
    for page in plan.get("pages", []):
        for row in page.get("rows", []):
            for pid in row:
                if pid not in panel_ids:
                    errors.append(t("err_page_panel", id=page["id"], panel=pid))
    return errors


def estimate(plan, manifest, only):
    todo_refs = [r for r in plan.get("refs", []) if r.get("prompt") and not r.get("file")
                 and (only is None or r["id"] in only) and manifest.get("ref:" + r["id"]) != "done"]
    todo_panels = [p for p in plan.get("panels", [])
                   if (only is None or p["id"] in only) and manifest.get("panel:" + p["id"]) != "done"]
    return todo_refs, todo_panels


def ref_path(out, rid, plan, base_dir):
    for r in plan.get("refs", []):
        if r["id"] == rid and r.get("file"):
            return os.path.join(base_dir, r["file"])
    return os.path.join(out, "refs", f"{rid}.png")


def save_manifest(out, manifest):
    with open(os.path.join(out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def with_style(style, prompt):
    return prompt if prompt.startswith(style) else f"{style}\n{prompt}"


def write_preview(plan, out):
    direction = "row-reverse" if plan.get("reading_direction", "rtl") == "rtl" else "row"
    parts = [f"<!doctype html><meta charset=utf-8><title>{t('preview_title')}</title>",
             "<style>body{background:#888;margin:0;padding:24px;font-family:sans-serif}"
             ".page{background:#fff;width:800px;margin:0 auto 32px;padding:16px;box-sizing:border-box}"
             f".row{{display:flex;gap:8px;margin-bottom:8px;flex-direction:{direction}}}"
             ".row img{flex:1;min-width:0;object-fit:cover;border:3px solid #000;max-height:600px}"
             ".tag{font-size:12px;color:#333;margin-bottom:6px}</style>"]
    for page in plan.get("pages", []):
        parts.append(f"<div class=page><div class=tag>{html.escape(page['id'])}"
                     f" {html.escape(page.get('type', ''))}</div>")
        for row in page.get("rows", []):
            imgs = "".join(f"<img src='panels/{html.escape(pid)}.png' alt='{html.escape(pid)}'>" for pid in row)
            parts.append(f"<div class=row>{imgs}</div>")
        parts.append("</div>")
    path = os.path.join(out, "preview.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--out", default=None, help="output folder (default: output/ next to the plan)")
    ap.add_argument("--stage", choices=["refs", "panels", "all"], default="all")
    ap.add_argument("--only", nargs="*", help="only these ids")
    ap.add_argument("--force", action="store_true", help="regenerate even if done")
    ap.add_argument("--check", action="store_true", help="check and estimate only, no API calls")
    ap.add_argument("--preview", action="store_true", help="write the HTML preview only")
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

    if args.preview:
        print(t("preview", path=write_preview(plan, out)))
        return 0

    errors = check(plan, base_dir)
    if errors:
        print(t("check_failed"))
        for e in errors:
            print("  -", e)
        return 1

    todo_refs, todo_panels = estimate(plan, manifest, only)
    if args.stage == "refs":
        todo_panels = []
    if args.stage == "panels":
        todo_refs = []
    print(t("comic_ok", refs=len(todo_refs), panels=len(todo_panels),
            total=len(todo_refs) + len(todo_panels), model=ark.image_model()))
    if args.check:
        return 0
    if not os.environ.get("ARK_API_KEY"):
        print(t("key_missing_run"))
        return 1

    style = plan["style_anchor"]
    failed = []

    for r in todo_refs:
        dst = os.path.join(out, "refs", f"{r['id']}.png")
        print(t("running_ref", id=r["id"]))
        try:
            ark.generate_image(with_style(style, r["prompt"]), dst, size=r.get("size", "2K"))
            manifest["ref:" + r["id"]] = "done"
        except ark.ArkError as e:
            manifest["ref:" + r["id"]] = f"failed: {e}"
            failed.append(r["id"])
            print(t("item_failed", err=e))
        save_manifest(out, manifest)

    for p in todo_panels:
        paths = [ref_path(out, x, plan, base_dir) for x in p.get("refs", [])]
        absent = [x for x in paths if not os.path.exists(x)]
        if absent:
            print(t("panel_ref_absent", id=p["id"], paths=absent))
            failed.append(p["id"])
            continue
        dst = os.path.join(out, "panels", f"{p['id']}.png")
        print(t("running_panel", id=p["id"], n=len(paths)))
        try:
            ark.generate_image(with_style(style, p["prompt"]), dst, ref_paths=paths,
                               size=p.get("aspect", "2K"), seed=p.get("seed"))
            manifest["panel:" + p["id"]] = "done"
        except ark.ArkError as e:
            manifest["panel:" + p["id"]] = f"failed: {e}"
            failed.append(p["id"])
            print(t("item_failed", err=e))
        save_manifest(out, manifest)
        time.sleep(plan.get("delay_seconds", 0))

    if plan.get("pages"):
        print(t("preview", path=write_preview(plan, out)))
    if failed:
        print(t("n_failed", n=len(failed), ids=" ".join(failed)))
        print(t("comic_retry"))
        return 2
    print(t("comic_done"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

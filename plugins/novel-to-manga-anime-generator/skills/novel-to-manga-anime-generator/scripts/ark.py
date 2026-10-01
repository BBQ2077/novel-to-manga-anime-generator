"""Minimal BytePlus ModelArk client (Python standard library only).

Request/response shapes match the official SDK (byteplus-python-sdk-v2, byteplussdkarkruntime).

Environment variables:
  ARK_API_KEY      required, created in the ModelArk console
  ARK_BASE_URL     optional, default https://ark.ap-southeast.bytepluses.com/api/v3
  ARK_IMAGE_MODEL  optional, Seedream model ID or endpoint ID (default: Seedream 5.0 Lite)
  ARK_VIDEO_MODEL  optional, Seedance model ID or endpoint ID

Model IDs change with new versions; always use what the ModelArk console shows.
"""

import base64
import json
import mimetypes
import os
import time
import urllib.error
import urllib.request

from i18n import t

DEFAULT_BASE_URL = "https://ark.ap-southeast.bytepluses.com/api/v3"
DEFAULT_IMAGE_MODEL = "seedream-5-0-260128"  # Seedream 5.0 Lite
DEFAULT_VIDEO_MODEL = "dreamina-seedance-2-5-260628"

# 2K-class pixel sizes for common aspect ratios
ASPECT_SIZES = {
    "1:1": "2048x2048",
    "4:3": "2304x1728",
    "3:4": "1728x2304",
    "16:9": "2560x1440",
    "9:16": "1440x2560",
    "3:2": "2496x1664",
    "2:3": "1664x2496",
    "21:9": "3024x1296",
}


class ArkError(RuntimeError):
    pass


def _base_url():
    return os.environ.get("ARK_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def _api_key():
    key = os.environ.get("ARK_API_KEY")
    if not key:
        raise ArkError(t("no_key"))
    return key


def image_model():
    return os.environ.get("ARK_IMAGE_MODEL", DEFAULT_IMAGE_MODEL)


def video_model():
    return os.environ.get("ARK_VIDEO_MODEL", DEFAULT_VIDEO_MODEL)


def _request(method, path, body=None, timeout=300, retries=3):
    url = _base_url() + path
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Authorization": f"Bearer {_api_key()}", "Content-Type": "application/json"}
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            # Retry 429 and 5xx; report everything else (balance, bad params, moderation) right away
            if (e.code == 429 or e.code >= 500) and attempt < retries:
                time.sleep(2 ** (attempt + 1))
                continue
            raise ArkError(t("http_error", code=e.code, path=path, detail=detail)) from None
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(2 ** (attempt + 1))
                continue
            raise ArkError(t("conn_error", url=url, reason=e.reason)) from None


def to_data_uri(path):
    """Encode a local image as a data URI so no image hosting is needed."""
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('ascii')}"


def size_for(aspect_or_size):
    if not aspect_or_size:
        return "2K"
    return ASPECT_SIZES.get(aspect_or_size, aspect_or_size)


def _short(obj):
    return json.dumps(obj, ensure_ascii=False)[:500]


def generate_image(prompt, out_path, ref_paths=(), size="2K", watermark=False, seed=None):
    """Seedream image generation. ref_paths map in order to image 1, image 2, ... in the prompt."""
    body = {
        "model": image_model(),
        "prompt": prompt,
        "size": size_for(size),
        "response_format": "b64_json",
        "watermark": watermark,
    }
    if seed is not None:
        body["seed"] = seed
    refs = [to_data_uri(p) for p in ref_paths]
    if len(refs) == 1:
        body["image"] = refs[0]
    elif refs:
        body["image"] = refs
    resp = _request("POST", "/images/generations", body)
    items = resp.get("data") or []
    if not items:
        raise ArkError(t("no_image", resp=_short(resp)))
    item = items[0]
    if item.get("b64_json"):
        raw = base64.b64decode(item["b64_json"])
    elif item.get("url"):
        raw = _download(item["url"])
    else:
        raise ArkError(t("bad_format", resp=_short(item)))
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(raw)
    return {"usage": resp.get("usage")}


def create_video_task(prompt, first_frame=None, last_frame=None, ref_paths=(),
                      duration=12, ratio="16:9", resolution=None,
                      generate_audio=True, watermark=False, seed=None, return_last_frame=False):
    """Create a Seedance task and return its id.

    first_frame/last_frame: image-to-video (first and optional last frame)
    ref_paths: reference-to-video, mapping in order to @Image1, @Image2, ... in the prompt
    The two modes are mutually exclusive.
    """
    if (first_frame or last_frame) and ref_paths:
        raise ArkError(t("mixed_modes"))
    content = [{"type": "text", "text": prompt}]
    if first_frame:
        content.append({"type": "image_url", "image_url": {"url": to_data_uri(first_frame)}, "role": "first_frame"})
    if last_frame:
        content.append({"type": "image_url", "image_url": {"url": to_data_uri(last_frame)}, "role": "last_frame"})
    for p in ref_paths:
        content.append({"type": "image_url", "image_url": {"url": to_data_uri(p)}, "role": "reference_image"})
    body = {
        "model": video_model(),
        "content": content,
        "duration": duration,
        "ratio": ratio,
        "generate_audio": generate_audio,
        "watermark": watermark,
    }
    if resolution:
        body["resolution"] = resolution
    if return_last_frame:
        body["return_last_frame"] = True
    if seed is not None:
        body["seed"] = seed
    resp = _request("POST", "/contents/generations/tasks", body)
    task_id = resp.get("id")
    if not task_id:
        raise ArkError(t("no_task_id", resp=_short(resp)))
    return task_id


def get_video_task(task_id):
    return _request("GET", f"/contents/generations/tasks/{task_id}")


def wait_video(task_id, out_path, poll_seconds=10, timeout_seconds=1800, last_frame_path=None):
    """Poll until done, then download the video (and the last frame when requested)."""
    deadline = time.time() + timeout_seconds
    while True:
        task = get_video_task(task_id)
        status = task.get("status")
        if status == "succeeded":
            content = task.get("content") or {}
            url = content.get("video_url")
            if not url:
                raise ArkError(t("no_video_url", resp=_short(task)))
            os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(_download(url))
            last_url = content.get("last_frame_url")
            if last_frame_path and last_url:
                os.makedirs(os.path.dirname(last_frame_path) or ".", exist_ok=True)
                with open(last_frame_path, "wb") as f:
                    f.write(_download(last_url))
            return task
        if status in ("failed", "cancelled", "expired"):
            raise ArkError(t("task_failed", tid=task_id, status=status, error=_short(task.get("error"))))
        if time.time() > deadline:
            raise ArkError(t("task_timeout", tid=task_id, status=status))
        time.sleep(poll_seconds)


def _download(url, timeout=600):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.read()

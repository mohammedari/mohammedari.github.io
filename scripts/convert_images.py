from pathlib import Path
from PIL import Image

# ===== 設定 =====
ROOT_DIR = Path("assets/images/gen/blog")
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

THUMB_WIDTH = 400
THUMB_HEIGHT = 225
QUALITY = 80
# =================


def center_crop_resize(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    src_w, src_h = img.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        # 横が余る → 横をクロップ
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        box = (left, 0, left + new_w, src_h)
    else:
        # 縦が余る → 縦をクロップ
        new_h = int(src_w / target_ratio)
        top = (src_h - new_h) // 2
        box = (0, top, src_w, top + new_h)

    img = img.crop(box)
    return img.resize((target_w, target_h), Image.LANCZOS)


for path in ROOT_DIR.rglob("*"):
    if path.suffix.lower() not in SUPPORTED_EXTS:
        continue

    out_path = path.with_name(path.stem + ".webp")
    thumb_path = path.with_name(path.stem + "-thumbnail.webp")

    if out_path.exists():
        print(f"Skip (exists): {out_path}")
        continue

    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            img.save(
                out_path,
                "WEBP",
                quality=QUALITY,
                method=6,
            )
            print(f"Generated: {out_path}")

            thumb = center_crop_resize(img, THUMB_WIDTH, THUMB_HEIGHT)
            thumb.save(
                thumb_path,
                "WEBP",
                quality=QUALITY,
                method=6,
            )
            print(f"Generated: {thumb_path}")
    except Exception as e:
        print(f"Failed: {path} ({e})")

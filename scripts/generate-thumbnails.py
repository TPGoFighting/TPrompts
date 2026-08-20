#!/usr/bin/env python3
"""Generate lightweight first-frame WebP previews for local prompt media."""

from pathlib import Path
import sys

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "images"
OUTPUT_DIR = SOURCE_DIR / "thumbs"
SUPPORTED = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
MAX_SIZE = (480, 320)


def main() -> int:
    sources = sorted(
        path
        for path in SOURCE_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    OUTPUT_DIR.mkdir(exist_ok=True)

    source_bytes = 0
    output_bytes = 0
    for source in sources:
        target = OUTPUT_DIR / f"{source.name}.webp"
        source_bytes += source.stat().st_size
        try:
            with Image.open(source) as opened:
                if getattr(opened, "is_animated", False):
                    opened.seek(0)
                image = ImageOps.exif_transpose(opened.copy())
                image.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
                if image.mode not in ("RGB", "RGBA"):
                    image = image.convert("RGBA" if "transparency" in opened.info else "RGB")
                image.save(target, "WEBP", quality=68, method=6)
            output_bytes += target.stat().st_size
        except Exception as error:  # pragma: no cover - reports a corrupt source asset
            print(f"缩略图生成失败: {source.relative_to(ROOT)} ({error})", file=sys.stderr)
            return 1

    print(
        f"缩略图生成完成：{len(sources)} 张，"
        f"{source_bytes / 1024 / 1024:.1f} MB → {output_bytes / 1024 / 1024:.1f} MB"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from pathlib import Path
from PIL import Image
import json

tippy_dir = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/assets/tippy')

manifest = []
for i in range(1, 73):
    name = f'tippy_{i:02d}.png'
    p = tippy_dir / name
    if p.exists():
        with Image.open(p) as img:
            w, h = img.size
            manifest.append({
                'id': i,
                'file': name,
                'size': f'{w}x{h}',
                'ratio': round(w/h, 2)
            })

print(json.dumps(manifest, indent=2))

import json, math, os, re, sys
from pathlib import Path

ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
CHUNK_DIR = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/chunks')
CHUNK_DIR.mkdir(exist_ok=True)

# 1. 提取全部 2112 条
items = []
for f in sorted(ROOT.rglob('*.md')):
    md = f.read_text(encoding='utf-8')
    m = re.match(r'^([a-z0-9]{20,})_', f.name)
    if not m:
        sm = re.search(r'prompts\.chat/prompts/([a-z0-9]+)', md)
        if not sm: continue
        iid = sm.group(1)
    else:
        iid = m.group(1)
    tm = re.match(r'^#\s+(.+)$', md, re.M)
    title = tm.group(1).strip() if tm else f.stem
    cat = f.parent.name
    pm = re.search(r'## Prompt Content\n+```[^\n]*\n(.*?)\n```', md, re.S)
    if not pm: continue
    prompt = pm.group(1).strip()
    items.append({'id': iid, 'title': title, 'cat': cat, 'prompt': prompt})

# 2. 读取当前 ndjson 并去重
done_ids = set()
unique_lines = []
if OUT_NDJSON.exists():
    for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
        try:
            d = json.loads(line)
            if d['id'] not in done_ids:
                done_ids.add(d['id'])
                unique_lines.append(json.dumps(d, ensure_ascii=False))
        except Exception: pass

# 重写去重后的 ndjson
OUT_NDJSON.write_text('\n'.join(unique_lines) + '\n', encoding='utf-8')

# 3. 找出剩余 todo 并均分到 10 个 chunk 文件
todo = [x for x in items if x['id'] not in done_ids]
print(f'总数: {len(items)}, 已完成: {len(done_ids)}, 剩余待译: {len(todo)}')

chunk_size = math.ceil(len(todo) / 10)
for i in range(10):
    c = todo[i*chunk_size : (i+1)*chunk_size]
    chunk_file = CHUNK_DIR / f'chunk_{i}.json'
    chunk_file.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Chunk {i}: {len(c)} 条 -> {chunk_file.name}')

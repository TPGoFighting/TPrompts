import json, math, os, re
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
CHUNK_DIR = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks')
CHUNK_DIR.mkdir(exist_ok=True)

# 1. 读出所有已完成的 id 并重写去重
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

OUT_NDJSON.write_text('\n'.join(unique_lines) + '\n', encoding='utf-8')

# 2. 扫描所有 2112 条
all_items = []
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
    all_items.append({'id': iid, 'title': title, 'cat': cat, 'prompt': prompt})

untranslated = [x for x in all_items if x['id'] not in done_ids]
print(f'已完成高质量翻译: {len(done_ids)} / {len(all_items)} | 剩余待翻译: {len(untranslated)}')

# 3. 均匀切分为 10 份
chunk_size = math.ceil(len(untranslated) / 10)
for i in range(10):
    c = untranslated[i*chunk_size : (i+1)*chunk_size]
    cf = CHUNK_DIR / f'agent_chunk_{i}.json'
    cf.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding='utf-8')
    # 清空对应输出文件
    out_f = CHUNK_DIR / f'agent_chunk_{i}_out.ndjson'
    out_f.write_text('', encoding='utf-8')
    print(f'Agent Chunk {i}: {len(c)} 条 -> {cf.name}')

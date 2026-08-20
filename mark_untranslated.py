import json, re
from pathlib import Path

ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
CHUNK_DIR = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/chunks')
UNTRANSLATED_FILE = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/untranslated_summary.json')

# 1. 统计全部 2112 条
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

# 2. 读取当前已完成的 ndjson 并去重规范化
done_ids = set()
unique_records = []
if OUT_NDJSON.exists():
    for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
        try:
            d = json.loads(line)
            if d['id'] not in done_ids:
                done_ids.add(d['id'])
                unique_records.append(d)
        except Exception: pass

# 重写去重文件
with open(OUT_NDJSON, 'w', encoding='utf-8') as f:
    for rec in unique_records:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'【总盘点】总提示词库: {len(all_items)} 条 | 已完成翻译: {len(done_ids)} 条 | 剩余未翻译: {len(all_items) - len(done_ids)} 条\n')

# 3. 分别统计 10 个 Chunk 的完成情况
stats = []
untranslated_list = []

for i in range(10):
    c_file = CHUNK_DIR / f'chunk_{i}.json'
    if not c_file.exists():
        continue
    c_items = json.loads(c_file.read_text(encoding='utf-8'))
    c_done = [x for x in c_items if x['id'] in done_ids]
    c_todo = [x for x in c_items if x['id'] not in done_ids]
    
    stats.append({
        'chunk_id': i,
        'total': len(c_items),
        'done': len(c_done),
        'remaining': len(c_todo)
    })
    
    for x in c_todo:
        untranslated_list.append({
            'chunk_id': i,
            'id': x['id'],
            'title': x['title'],
            'category': x['cat']
        })
    print(f'子 Agent {i} (Chunk {i}): 总分配 {len(c_items)} 条 | 已完成 {len(c_done)} 条 | 未翻译 {len(c_todo)} 条')

# 4. 导出未翻译清单文件供追踪
UNTRANSLATED_FILE.write_text(json.dumps({
    'total_untranslated': len(untranslated_list),
    'items': untranslated_list
}, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'\n已将 {len(untranslated_list)} 条未翻译详情导出并标记至: {UNTRANSLATED_FILE}')

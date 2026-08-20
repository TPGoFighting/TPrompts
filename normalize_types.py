import json
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
records = []
for l in OUT_NDJSON.read_text().splitlines():
    d = json.loads(l)
    if isinstance(d.get('zh'), list):
        d['zh'] = '\n'.join(str(x) for x in d['zh'])
    elif d.get('zh') is None:
        d['zh'] = ''
    if isinstance(d.get('usage'), list):
        d['usage'] = '\n'.join(str(x) for x in d['usage'])
    elif d.get('usage') is None:
        d['usage'] = ''
    records.append(json.dumps(d, ensure_ascii=False))

OUT_NDJSON.write_text('\n'.join(records) + '\n', encoding='utf-8')
print('ndjson 类型修复完成！')

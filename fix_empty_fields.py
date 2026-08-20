import json, os, urllib.request, urllib.parse, re, time
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
for line in open(env_path):
    if line.startswith('GEMINI_API_KEY='):
        API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")

# 找出正文或使用说明为空的条目
records = {}
for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
    try:
        d = json.loads(line)
        records[d['id']] = d
    except: pass

need_fix_ids = set()
for r in records.values():
    if not r.get('zh') or not r.get('usage') or len(r.get('usage', '').strip()) < 10:
        need_fix_ids.add(r['id'])

print(f'待补全空白/过短条数: {len(need_fix_ids)}')

md_map = {}
for f in ROOT.rglob('*.md'):
    m = f.name.split('_')[0]
    if m in need_fix_ids:
        md = f.read_text(encoding='utf-8')
        tm = re.match(r'^#\s+(.+)$', md, re.M)
        title = tm.group(1).strip() if tm else f.stem
        pm = re.search(r'## Prompt Content\n+```[^\n]*\n(.*?)\n```', md, re.S)
        if not pm: continue
        prompt = pm.group(1).strip()
        md_map[m] = {'id': m, 'title': title, 'cat': f.parent.name, 'prompt': prompt}

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={urllib.parse.quote(API_KEY)}'

for idx, (iid, item) in enumerate(md_map.items()):
    prompt_text = f"""你是专业的 AI 提示词本地化专家。请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【要求】
1. 保持代码、JSON、占位符原样，仅翻译自然语言。
2. 严格输出标准 JSON 格式（包含 title_zh, zh, usage 三个字段）：
{{"id": "{item['id']}", "title_zh": "...", "zh": "...", "usage": "..."}}

【待翻译内容】
ID: {item['id']}
标题: {item['title']}
分类: {item['cat']}
提示词:
{item['prompt']}
"""
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': prompt_text}]}],
        'generationConfig': {'maxOutputTokens': 8192, 'temperature': 0.1},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'}, method='POST')
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                res = json.loads(resp.read().decode())
                txt = res['candidates'][0]['content']['parts'][0]['text'].strip()
                txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt)
                m = re.search(r'\{[\s\S]*\}', txt)
                if m:
                    data = json.loads(m.group(0))
                    if data.get('zh') and data.get('usage'):
                        records[iid] = {
                            'id': iid,
                            'title_zh': data.get('title_zh', item['title']),
                            'zh': data['zh'],
                            'usage': data['usage']
                        }
                        print(f"[{idx+1}/{len(md_map)}] 补全成功: {data.get('title_zh')}")
                        break
        except Exception as e:
            time.sleep(2)

# 写回 ndjson
lines = [json.dumps(r, ensure_ascii=False) for r in records.values()]
OUT_NDJSON.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print("全部补全写入完成！")

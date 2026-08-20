import json, os, re, sys, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

MODEL = 'gemini-3.5-flash'
BASE = 'https://generativelanguage.googleapis.com/v1beta/models'

# 1. 扫描全部
all_items = {}
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
    all_items[iid] = {'id': iid, 'title': title, 'cat': cat, 'prompt': prompt}

done_ids = set()
if OUT_NDJSON.exists():
    for l in OUT_NDJSON.read_text().splitlines():
        try: done_ids.add(json.loads(l)['id'])
        except Exception: pass

todo = [v for k, v in all_items.items() if k not in done_ids]
print(f'剩余需要补齐的条数: {len(todo)}')

def translate_single(item):
    url = f'{BASE}/{MODEL}:generateContent?key={urllib.parse.quote(API_KEY)}'
    prompt_text = f"""你是专业的 AI 提示词本地化专家。请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【要求】
1. 忠实原意，语言自然流畅，不要机翻腔。
2. 保持代码、JSON、占位符（如 ${{var}}）原样，仅翻译自然语言。
3. 严格输出单行或标准 JSON 对象（不要 markdown 围栏）：
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
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json'}, method='POST')
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                res = json.loads(resp.read().decode())
                txt = res.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
                txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt.strip())
                m = re.search(r'\{[\s\S]*\}', txt)
                if m:
                    data = json.loads(m.group(0))
                    if 'title_zh' in data and 'zh' in data and 'usage' in data:
                        data['id'] = item['id']
                        return data
        except Exception as e:
            time.sleep(2 + attempt * 2)
    raise RuntimeError(f"Failed item {item['id']}")

success = 0
for idx, item in enumerate(todo):
    try:
        res = translate_single(item)
        with open(OUT_NDJSON, 'a', encoding='utf-8') as f:
            f.write(json.dumps(res, ensure_ascii=False) + '\n')
        success += 1
        print(f"[{idx+1}/{len(todo)}] 成功翻译: {res['title_zh']}")
    except Exception as e:
        print(f"[{idx+1}/{len(todo)}] 失败: {e}")

print(f"补齐完成！成功: {success}/{len(todo)}")

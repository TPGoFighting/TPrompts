import json, os, urllib.request, urllib.parse, re, time
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
for line in open(env_path):
    if line.startswith('GEMINI_API_KEY='):
        API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")

missing_ids = {'cmmx3jj8c000hk604w8fmzk8j', 'cmmx3kakv0017il04axj51zi2', 'cmj9l3pkq0001u10s1a0x9lcm'}

todo = []
for f in ROOT.rglob('*.md'):
    m = f.name.split('_')[0]
    if m in missing_ids:
        md = f.read_text(encoding='utf-8')
        tm = re.match(r'^#\s+(.+)$', md, re.M)
        title = tm.group(1).strip() if tm else f.stem
        pm = re.search(r'## Prompt Content\n+```[^\n]*\n(.*?)\n```', md, re.S)
        if not pm: continue
        prompt = pm.group(1).strip()
        todo.append({'id': m, 'title': title, 'cat': f.parent.name, 'prompt': prompt})

print(f"处理最后 3 条...")
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={urllib.parse.quote(API_KEY)}'

for it in todo:
    prompt_text = f"""你是专业的 AI 提示词本地化专家。请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【要求】
1. 保持代码、结构、变量占位符原样，仅翻译自然语言。
2. 输出标准 JSON 格式：
{{"id": "{it['id']}", "title_zh": "...", "zh": "...", "usage": "..."}}

【待翻译内容】
ID: {it['id']}
标题: {it['title']}
分类: {it['cat']}
提示词:
{it['prompt']}
"""
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': prompt_text}]}],
        'generationConfig': {'maxOutputTokens': 16384, 'temperature': 0.1},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'}, method='POST')
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                res = json.loads(resp.read().decode())
                txt = res['candidates'][0]['content']['parts'][0]['text'].strip()
                txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt)
                m = re.search(r'\{[\s\S]*\}', txt)
                if m:
                    data = json.loads(m.group(0))
                    data['id'] = it['id']
                    with open(OUT_NDJSON, 'a', encoding='utf-8') as f:
                        f.write(json.dumps(data, ensure_ascii=False) + '\n')
                    print(f"成功: {data['title_zh']}", flush=True)
                    break
        except Exception as e:
            print(f"重试: {e}", flush=True)
            time.sleep(3)

print("全部搞定！", flush=True)

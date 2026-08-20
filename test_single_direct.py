import os, json, urllib.request, urllib.parse, re, time

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
for line in open(env_path):
    if line.startswith('GEMINI_API_KEY='):
        API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")

with open('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json') as f:
    items = json.load(f)

# 取一个已有的未翻 item
out_done = set()
with open('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson') as f:
    for l in f:
        try: out_done.add(json.loads(l)['id'])
        except: pass

todo = [x for x in items if x['id'] not in out_done]
item = todo[0]
print(f"Translating item: {item['id']} ({item['title']})")

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={urllib.parse.quote(API_KEY)}'
prompt = f"""你是专业的 AI 提示词本地化专家。请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【要求】
1. 保持代码、JSON、占位符原样，仅翻译自然语言。
2. 严格输出单行或标准 JSON 对象（不要 markdown 围栏）：
{{"id": "{item['id']}", "title_zh": "...", "zh": "...", "usage": "..."}}

【待翻译内容】
ID: {item['id']}
标题: {item['title']}
分类: {item['cat']}
提示词:
{item['prompt']}
"""
body = {
    'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
    'generationConfig': {'maxOutputTokens': 8192, 'temperature': 0.1},
}
req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'}, method='POST')
t0 = time.time()
with urllib.request.urlopen(req, timeout=30) as resp:
    res = json.loads(resp.read().decode())
    txt = res['candidates'][0]['content']['parts'][0]['text']
    print(f"Done in {time.time()-t0:.2f}s!")
    print(txt[:300])

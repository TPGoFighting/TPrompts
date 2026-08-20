import json, os, urllib.request, urllib.parse

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

with open('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

item0 = items[0]
print(f"Item 0 prompt length: {len(item0['prompt'])} chars")

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={urllib.parse.quote(API_KEY)}'

prompt = f"""请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【要求】
1. 保持代码、结构、格式、标识符原样，仅翻译自然语言。
2. 严格输出单行或标准 JSON 对象（不要 markdown 围栏）：
{{"id": "{item0['id']}", "title_zh": "...", "zh": "...", "usage": "..."}}

【待翻译内容】
ID: {item0['id']}
标题: {item0['title']}
分类: {item0['cat']}
提示词:
{item0['prompt']}
"""

body = {
    'contents': [{'role': 'user', 'parts': [{'text': prompt}]}],
    'generationConfig': {'maxOutputTokens': 16384, 'temperature': 0.1},
}
req = urllib.request.Request(url, data=json.dumps(body).encode(),
    headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        res = json.loads(resp.read().decode())
        cand = res.get('candidates', [{}])[0]
        print("Finish reason:", cand.get('finishReason'))
        txt = cand.get('content', {}).get('parts', [{}])[0].get('text', '')
        print("Output length:", len(txt))
        print("Preview start:\n", txt[:200])
        print("Preview end:\n", txt[-200:])
except Exception as e:
    print("Error:", e)

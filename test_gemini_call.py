import os, json, urllib.request, urllib.parse

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

MODEL = 'gemini-2.5-flash'
BASE = 'https://generativelanguage.googleapis.com/v1beta'

url = f'{BASE}/models/{MODEL}:generateContent?key={urllib.parse.quote(API_KEY)}'
body = {
    'contents': [{'parts': [{'text': 'Hello, say 1 2 3 in JSON format: {"result": [1,2,3]}'}]}],
    'generationConfig': {'temperature': 0.2},
}
req = urllib.request.Request(url, data=json.dumps(body).encode(),
    headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode())
        print("Success! Result:", res.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', ''))
except Exception as e:
    print("Error calling Gemini:", e)

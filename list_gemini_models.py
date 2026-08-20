import os, json, urllib.request, urllib.parse

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

BASE = 'https://generativelanguage.googleapis.com/v1beta'
url = f'{BASE}/models?key={urllib.parse.quote(API_KEY)}'
req = urllib.request.Request(url, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode())
        print("Available models:")
        for m in res.get('models', []):
            if 'generateContent' in m.get('supportedGenerationMethods', []):
                print(m.get('name'))
except Exception as e:
    print("Error:", e)

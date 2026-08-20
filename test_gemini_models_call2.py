import os, json, urllib.request, urllib.parse

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

for model_name in ['gemini-3.5-flash', 'gemini-3.7-flash', 'gemini-3.1-pro-preview']:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={urllib.parse.quote(API_KEY)}'
    body = {
        'contents': [{'parts': [{'text': 'Say hello'}]}],
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode())
            print(f"Success with {model_name}:", res['candidates'][0]['content']['parts'][0]['text'].strip())
            break
    except urllib.error.HTTPError as e:
        print(f"Failed {model_name}: HTTP {e.code} - {e.read().decode()[:100]}")
    except Exception as e:
        print(f"Failed {model_name}: {e}")

# -*- coding: utf-8 -*-
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

input_file = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json"
output_file = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0_out.ndjson"

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

MODEL = 'gemini-3.5-flash'
BASE = 'https://generativelanguage.googleapis.com/v1beta/models'

SYSTEM_INSTRUCTION = """你是专业的 AI 提示词本地化专家。请将输入的英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

【翻译质量要求】：
1. 忠实原意，语言自然流畅，符合中文表达习惯，绝不要机翻腔。
2. 【关键】如果提示词包含代码/JSON/配置文件/结构化数据/占位符（如 ${var}），必须完整保留原有结构：
   - 代码、JSON 键名、变量名、函数名、URL、文件路径、技术标识符一律【不翻译】
   - 所有字符串值中的引号必须保持半角英文引号 "（绝不能改成中文引号“”）
   - 代码块内容逐行保留原结构，只把其中真正的自然语言提示文字翻译成中文
   - 花括号、方括号、冒号等标点保持半角
3. 标题（title_zh）翻译简洁准确（不超过 30 个汉字）。
4. 使用说明（usage）用中文写 100-200 字，贴合本条提示词的具体内容，说明：它能让 AI 做什么、适合什么人用、具体怎么用（步骤要点）、注意什么。不要空话套话，不要每条雷同。
5. 结果必须以标准单个 JSON 对象格式输出（不要任何 Markdown 围栏或额外注释）：
{"id": "...", "title_zh": "...", "zh": "...", "usage": "..."}"""

def call_gemini_single(item):
    url = f'{BASE}/{MODEL}:generateContent?key={urllib.parse.quote(API_KEY)}'
    
    prompt = f"""【待翻译内容】
ID: {item['id']}
标题: {item['title']}
分类: {item['cat']}
提示词:
{item['prompt']}
"""
    body = {
        'contents': [
            {'role': 'user', 'parts': [{'text': SYSTEM_INSTRUCTION + '\n\n' + prompt}]}
        ],
        'generationConfig': {
            'maxOutputTokens': 16384,
            'temperature': 0.1,
            'responseMimeType': 'application/json'
        },
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json'}, method='POST')
    
    backoff = [10, 20, 30, 45, 60, 90, 120]
    for attempt in range(len(backoff)):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read().decode())
                txt = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                if not txt:
                    raise ValueError('empty response from Gemini')
                txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt.strip())
                res = json.loads(txt)
                if isinstance(res, list) and len(res) > 0:
                    res = res[0]
                if not isinstance(res, dict) or 'zh' not in res or 'usage' not in res:
                    raise ValueError('Invalid JSON schema returned')
                res['id'] = item['id']
                return res
        except urllib.error.HTTPError as e:
            wait = backoff[attempt]
            print(f"[{item['id']}] Attempt {attempt+1} got HTTP {e.code}. Waiting {wait}s...")
            time.sleep(wait)
        except Exception as e:
            wait = backoff[attempt]
            print(f"[{item['id']}] Attempt {attempt+1} failed: {e}. Waiting {wait}s...")
            time.sleep(wait)
            
    raise RuntimeError(f"Failed to translate item {item['id']}")

def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        items = json.load(f)
    print(f"Total items in chunk 0: {len(items)}")
    
    done_ids = set()
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        done_ids.add(json.loads(line)['id'])
                    except Exception:
                        pass
    print(f"Already done: {len(done_ids)}")
    todo = [x for x in items if x['id'] not in done_ids]
    print(f"Remaining to process: {len(todo)}")
    
    t0 = time.time()
    for idx, item in enumerate(todo):
        current_num = len(done_ids) + idx + 1
        print(f"[{current_num}/{len(items)}] Translating: {item['id']} ({item['title'][:30]})...")
        res = call_gemini_single(item)
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(res, ensure_ascii=False) + '\n')
        print(f"-> Saved: {res.get('title_zh', '')} | Elapsed: {time.time()-t0:.1f}s")
        # Pacing: 5s pause to stay well within RPM limits
        time.sleep(5)

    print(f"\nALL {len(items)} ITEMS COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    main()

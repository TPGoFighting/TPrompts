#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
translate_chunk_0.py - High-concurrency item-by-item translator for agent_chunk_0
"""
import json, os, re, sys, time, threading
from pathlib import Path
import urllib.request, urllib.parse, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

IN_FILE = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json')
OUT_FILE = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0_out.ndjson')

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        line = line.strip()
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

MODEL = 'gemini-3.6-flash'
BASE = 'https://generativelanguage.googleapis.com/v1beta'
LOCK = threading.Lock()

SYSTEM_PROMPT = """你是专业的 AI 提示词本地化专家。你负责将分配给你的英文 AI 提示词进行高质量翻译和使用说明撰写。

【翻译质量要求】：
1. 忠实原意，语言自然流畅，符合中文表达习惯，绝不要机翻腔。
2. 【关键】如果提示词包含代码/JSON/配置文件/结构化数据/占位符（如 ${var}、<tag> 等），必须完整保留原有结构：
   - 代码、JSON 键名、变量名、函数名、URL、文件路径、技术标识符一律【不翻译】
   - 所有字符串值中的引号必须保持半角英文引号 "（绝不能改成中文引号“”）
   - 代码块内容逐行保留原结构，只把其中真正的自然语言提示文字翻译成中文
   - 花括号、方括号、冒号等标点保持半角
3. 标题（title_zh）翻译简洁准确（不超过 30 个汉字）。
4. 使用说明（usage）用中文写 100-200 字，贴合本条提示词的具体内容，说明：它能让 AI 做什么、适合什么人用、具体怎么用（步骤要点）、注意什么。不要空话套话，不要每条雷同。
5. 输入是一个 JSON 对象：{"id": "...", "title": "...", "cat": "...", "prompt": "..."}
6. 只输出单个合法 JSON 对象，严禁任何额外文字或 markdown 围栏，格式：
{
  "id": "...",
  "title_zh": "...",
  "zh": "...",
  "usage": "..."
}"""

def call_gemini(payload_text, max_out=16000):
    url = f'{BASE}/models/{MODEL}:generateContent?key={urllib.parse.quote(API_KEY)}'
    body = {
        'contents': [{'parts': [{'text': payload_text}]}],
        'generationConfig': {
            'maxOutputTokens': max_out,
            'temperature': 0.2,
            'responseMimeType': 'application/json'
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode('utf-8'))

def clean_json_str(txt):
    txt = txt.strip()
    if txt.startswith('```json'):
        txt = txt[7:]
    elif txt.startswith('```'):
        txt = txt[3:]
    if txt.endswith('```'):
        txt = txt[:-3]
    return txt.strip()

def translate_item(item):
    user_msg = json.dumps({'id': item['id'], 'title': item.get('title', ''), 'cat': item.get('cat', ''), 'prompt': item['prompt']}, ensure_ascii=False)
    
    for attempt in range(6):
        try:
            res = call_gemini(SYSTEM_PROMPT + '\n\n' + user_msg)
            txt = res['candidates'][0]['content']['parts'][0]['text']
            txt = clean_json_str(txt)
            obj = json.loads(txt)
            if isinstance(obj, list) and len(obj) > 0:
                obj = obj[0]
            if not isinstance(obj, dict) or 'id' not in obj or 'zh' not in obj or 'title_zh' not in obj or 'usage' not in obj:
                raise ValueError(f"Invalid format returned: {txt[:100]}")
            obj['id'] = item['id']
            return obj
        except Exception as e:
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Failed to translate item {item['id']}")

def main():
    if not IN_FILE.exists():
        print(f"Error: {IN_FILE} does not exist", flush=True)
        sys.exit(1)

    items = json.loads(IN_FILE.read_text(encoding='utf-8'))
    print(f"Total items in {IN_FILE.name}: {len(items)}", flush=True)

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    done_ids = set()
    if OUT_FILE.exists():
        for line in OUT_FILE.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                done_ids.add(data['id'])
            except Exception:
                pass
    
    todo = [x for x in items if x['id'] not in done_ids]
    print(f"Already done: {len(done_ids)}, Remaining to do: {len(todo)}", flush=True)
    
    if not todo:
        print("All items completed!", flush=True)
        return

    completed_count = len(done_ids)

    def worker(item):
        nonlocal completed_count
        res = translate_item(item)
        with LOCK:
            with open(OUT_FILE, 'a', encoding='utf-8') as f:
                f.write(json.dumps(res, ensure_ascii=False) + '\n')
            completed_count += 1
            print(f"[{completed_count}/{len(items)}] Done: {item['id']} - {res.get('title_zh', '')}", flush=True)
        return item['id']

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(worker, item): item['id'] for item in todo}
        for future in as_completed(futures):
            item_id = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error processing {item_id}: {e}", flush=True)

    # Final check
    final_done = set()
    if OUT_FILE.exists():
        for line in OUT_FILE.read_text(encoding='utf-8').splitlines():
            if line.strip():
                try:
                    final_done.add(json.loads(line)['id'])
                except Exception:
                    pass
    print(f"\nFinal completed count in {OUT_FILE.name}: {len(final_done)} / {len(items)}", flush=True)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
translate_worker.py - 单个 chunk 专用批量翻译执行器
"""
import argparse, json, os, re, sys, time, threading
from pathlib import Path
import urllib.request, urllib.parse, urllib.error

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8'):
        line = line.strip()
        if line.startswith('GEMINI_API_KEY='):
            API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

MODEL = 'gemini-3.5-flash-lite'
BASE = 'https://generativelanguage.googleapis.com/v1beta'
OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
LOCK = threading.Lock()

SYSTEM_PROMPT = """你是专业的 AI 提示词本地化专家。将英文 AI 提示词翻译为高质量中文，并为每条撰写使用说明。

翻译要求：
1. 忠实原意，语言自然流畅，符合中文表达习惯，不要机翻腔
2. 【关键】如果提示词包含代码/JSON/配置文件/结构化数据，必须完整保留结构：
   - 代码、JSON 键名、变量名、函数名、URL、文件路径、技术标识符一律【不翻译】
   - 所有字符串值中的引号必须保持半角英文引号 "（绝不能改成中文引号“”）
   - 代码块内容逐行保留原结构，只把其中真正的自然语言提示文字翻译成中文
   - 花括号、方括号、冒号等标点保持半角
3. 标题翻译简洁准确（不超过 30 个汉字）
4. 使用说明（usage）用中文写 100-200 字，贴合本条提示词的具体内容，说明：它能让 AI 做什么、适合什么人用、具体怎么用（步骤要点）、注意什么。不要空话套话，不要每条雷同。

输入是 JSON 数组：[{"id","title","category","prompt"}]
只输出 JSON 数组，格式：[{"id","title_zh","zh","usage"}]，不要输出任何其他文字、注释或 markdown 围栏。"""

def call_gemini(payload_text, max_out=8000):
    url = f'{BASE}/models/{MODEL}:generateContent?key={urllib.parse.quote(API_KEY)}'
    body = {
        'contents': [{'parts': [{'text': payload_text}]}],
        'generationConfig': {'maxOutputTokens': max_out, 'temperature': 0.2},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())

def translate_single_batch(batch):
    user_msg = json.dumps([{'id': x['id'], 'title': x['title'], 'category': x['cat'], 'prompt': x['prompt']} for x in batch], ensure_ascii=False)
    for attempt in range(6):
        try:
            data = call_gemini(SYSTEM_PROMPT + '\n\n' + user_msg)
            txt = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
            if not txt:
                raise ValueError('empty response')
            txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt.strip())
            arr = json.loads(txt)
            if not isinstance(arr, list):
                raise ValueError('not a list')
            ids = [x['id'] for x in arr]
            missing = [x['id'] for x in batch if x['id'] not in ids]
            if missing:
                raise ValueError(f'missing: {missing[:3]}')
            time.sleep(0.5)  # 礼貌间隔
            return arr
        except Exception as e:
            time.sleep(3 + attempt * 3)
    # 拆半
    if len(batch) > 1:
        mid = len(batch) // 2
        return translate_single_batch(batch[:mid]) + translate_single_batch(batch[mid:])
    raise RuntimeError('failed item')

def process_chunk(chunk_id):
    chunk_file = Path(f'/Users/tylertang/Developer/ai-coding/tprompts-site/chunks/chunk_{chunk_id}.json')
    if not chunk_file.exists():
        print(f'Chunk {chunk_id} not found')
        return
    items = json.loads(chunk_file.read_text(encoding='utf-8'))
    
    # 过滤掉可能已被其他写入的
    done_ids = set()
    if OUT_NDJSON.exists():
        for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
            try: done_ids.add(json.loads(line)['id'])
            except Exception: pass
    todo = [x for x in items if x['id'] not in done_ids]
    print(f'[Chunk {chunk_id}] 总数: {len(items)}, 待处理: {len(todo)}')

    batches = [todo[i:i+4] for i in range(0, len(todo), 4)]
    ok = err = 0
    t0 = time.time()
    for idx, b in enumerate(batches):
        try:
            arr = translate_single_batch(b)
            with LOCK:
                with open(OUT_NDJSON, 'a', encoding='utf-8') as f:
                    for rec in arr:
                        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            ok += len(arr)
        except Exception as e:
            err += len(b)
            print(f'[Chunk {chunk_id}] 批次 {idx+1}/{len(batches)} 失败: {e}')
        if (idx + 1) % 5 == 0 or idx + 1 == len(batches):
            print(f'[Chunk {chunk_id}] 进度: {idx+1}/{len(batches)} 批 | 成功: {ok} | 失败: {err} | 耗时: {time.time()-t0:.1f}s')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chunk', type=int, required=True)
    args = parser.parse_args()
    process_chunk(args.chunk)

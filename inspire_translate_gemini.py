#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inspire_translate_gemini.py - 免费翻译剩余提示词（Google AI Studio 免费层）
- 端点: generativelanguage.googleapis.com（native API）
- 模型: gemini-3.7-flash（免费层：15 RPM / 1500 RPD，足够翻完全部）
- 与 inspire_translate.py 共用 inspire_zh.ndjson 断点续传
- 策略: 低并发 + 每批 4 条 + 失败拆半重试，避免触发限流

用法: python3 inspire_translate_gemini.py [--limit N] [--dry]
"""
import argparse, json, os, re, sys, time, threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import urllib.request, urllib.parse, urllib.error

ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
OUT_NDJSON = Path(__file__).parent / 'inspire_zh.ndjson'
LOCK = threading.Lock()

def load_key():
    key = os.environ.get('GEMINI_API_KEY', '')
    if not key:
        env_path = os.path.expanduser('~/.hermes/.env')
        if os.path.exists(env_path):
            for line in open(env_path, encoding='utf-8'):
                line = line.strip()
                if line.startswith('GEMINI_API_KEY='):
                    key = line.split('=', 1)[1].strip().strip('"').strip("'")
                    break
    return key

API_KEY = load_key()
MODEL = 'gemini-3.5-flash-lite'
BASE = 'https://generativelanguage.googleapis.com/v1beta'

# 复用原脚本的提取逻辑
def extract_items(limit=None):
    items = []
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
        items.append({'id': iid, 'title': title, 'cat': cat, 'prompt': prompt})
    if limit:
        items = items[:limit]
    return items

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
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())

def translate_batch(batch):
    """失败时拆半批递归；单条仍失败抛出"""
    try:
        return _translate_once(batch)
    except Exception:
        if len(batch) > 1:
            mid = len(batch) // 2
            return translate_batch(batch[:mid]) + translate_batch(batch[mid:])
        raise

def _translate_once(batch):
    user_msg = json.dumps([{'id': x['id'], 'title': x['title'], 'category': x['cat'], 'prompt': x['prompt']} for x in batch], ensure_ascii=False)
    last_err = None
    for attempt in range(4):
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
            return arr
        except urllib.error.HTTPError as e:
            last_err = f'HTTP {e.code}: {e.read().decode()[:150]}'
            time.sleep(3 + attempt * 4)
        except Exception as e:
            last_err = str(e)
            time.sleep(3 + attempt * 4)
    raise RuntimeError(f'gemini batch failed: {last_err}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--batch', type=int, default=4)
    ap.add_argument('--workers', type=int, default=2)
    ap.add_argument('--dry', action='store_true', help='只统计剩余数量，不调用 API')
    args = ap.parse_args()

    if not API_KEY:
        print('❌ 找不到 GEMINI_API_KEY'); sys.exit(1)

    items = extract_items()
    done_ids = set()
    if OUT_NDJSON.exists():
        for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
            try: done_ids.add(json.loads(line)['id'])
            except Exception: pass
    todo = [x for x in items if x['id'] not in done_ids]
    print(f'总数 {len(items)} · 已完成 {len(done_ids)} · 剩余 {len(todo)}')
    if args.dry:
        return
    if args.limit:
        todo = todo[:args.limit]

    batches = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]
    ok = errs = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(translate_batch, b): b for b in batches}
        n = 0
        for fut in as_completed(futs):
            b = futs[fut]
            n += 1
            try:
                arr = fut.result()
                with LOCK:
                    with open(OUT_NDJSON, 'a', encoding='utf-8') as f:
                        for rec in arr:
                            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
                ok += len(arr)
            except Exception as e:
                errs += len(b)
                print(f'[失败] {n}/{len(batches)}: {e}', flush=True)
            if n % 20 == 0 or n == len(batches):
                print(f'进度 {n}/{len(batches)} 批 · 成功 {ok} · 失败 {errs} · {(time.time()-t0)/60:.1f}min', flush=True)
    print(f'完成！成功 {ok}，失败 {errs}，耗时 {(time.time()-t0)/60:.1f} 分钟', flush=True)

if __name__ == '__main__':
    main()

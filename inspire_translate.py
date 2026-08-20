#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inspire_translate.py - 大模型批量翻译 2112 条提示词（灵感板块数据管线）
- 源: prompt-templates/by-category/**/*.md
- 调: OpenAI 兼容 API (token.sensenova.cn/v1, deepseek-v4-flash)
- 输出: inspire_zh.ndjson（每行一条: id,title_zh,zh,usage），断点续传
- 并发: 多 worker 线程

用法: python3 inspire_translate.py [--batch N] [--workers W] [--limit M] [--model M]
"""
import argparse, json, os, re, sys, time, threading, yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
OUT_NDJSON = Path(__file__).parent / 'inspire_zh.ndjson'
LOCK = threading.Lock()

# ---------- API 配置（优先 DeepSeek 官方 API，key 从 ~/.hermes/.env 读取） ----------
def load_api():
    key = os.environ.get('DEEPSEEK_API_KEY', '')
    if not key:
        env_path = os.path.expanduser('~/.hermes/.env')
        if os.path.exists(env_path):
            for line in open(env_path, encoding='utf-8'):
                line = line.strip()
                if line.startswith('DEEPSEEK_API_KEY='):
                    key = line.split('=', 1)[1].strip().strip('"').strip("'")
                    break
    return 'https://api.deepseek.com/v1', key

BASE_URL, API_KEY = load_api()

# ---------- 数据提取 ----------
def extract_items(limit=None):
    items = []
    for f in sorted(ROOT.rglob('*.md')):
        md = f.read_text(encoding='utf-8')
        # id: 文件名第一个下划线之前（cmj..._Title.md）
        m = re.match(r'^([a-z0-9]{20,})_', f.name)
        if not m:
            # 兜底：从 Source URL 提取
            sm = re.search(r'prompts\.chat/prompts/([a-z0-9]+)', md)
            if not sm: continue
            iid = sm.group(1)
        else:
            iid = m.group(1)
        # 标题: 首行 # Title
        tm = re.match(r'^#\s+(.+)$', md, re.M)
        title = tm.group(1).strip() if tm else f.stem
        # 分类: 目录名（55 个英文分类）
        cat = f.parent.name
        # 正文: ## Prompt Content 代码块
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

def call_api(model, payload):
    import urllib.request
    req = urllib.request.Request(
        f'{BASE_URL}/chat/completions',
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'},
        method='POST')
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode())

def translate_batch(batch, model, retries=4):
    """翻译一批；失败时自动拆半批递归重试（长文本截断/限流自适应），单条仍失败才抛出"""
    try:
        return _translate_batch_once(batch, model, retries)
    except Exception:
        if len(batch) > 1:
            mid = len(batch) // 2
            left = translate_batch(batch[:mid], model, retries)
            right = translate_batch(batch[mid:], model, retries)
            return left + right
        raise

def _translate_batch_once(batch, model, retries=4):
    user_msg = json.dumps([{'id': x['id'], 'title': x['title'], 'category': x['cat'], 'prompt': x['prompt']} for x in batch], ensure_ascii=False)
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_msg},
        ],
        'temperature': 0.2,
        'max_tokens': 8000,
    }
    last_err = None
    for attempt in range(retries):
        try:
            data = call_api(model, payload)
            content = data['choices'][0]['message']['content'].strip()
            # 去掉可能的 ```json 围栏
            content = re.sub(r'^```(?:json)?\s*|\s*```$', '', content.strip())
            arr = json.loads(content)
            if not isinstance(arr, list):
                raise ValueError('not a list')
            # 校验 id 一一对应
            ids = [x['id'] for x in arr]
            missing = [x['id'] for x in batch if x['id'] not in ids]
            if missing:
                raise ValueError(f'missing ids: {missing[:3]}')
            return arr
        except Exception as e:
            last_err = e
            time.sleep(2 ** attempt * 3)
    raise RuntimeError(f'batch failed after {retries} retries: {last_err}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', type=int, default=5)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--model', default='deepseek-chat')
    ap.add_argument('--single', action='store_true', help='只跑一批（连通性测试）')
    args = ap.parse_args()

    items = extract_items(args.limit if args.limit else None)
    print(f'提取到 {len(items)} 条提示词', flush=True)

    # 断点续传：加载已完成 id
    done_ids = set()
    if OUT_NDJSON.exists():
        for line in OUT_NDJSON.read_text(encoding='utf-8').splitlines():
            try:
                done_ids.add(json.loads(line)['id'])
            except Exception:
                pass
    todo = [x for x in items if x['id'] not in done_ids]
    print(f'已完成 {len(done_ids)}，剩余 {len(todo)}', flush=True)
    if args.single:
        todo = todo[:args.batch]

    batches = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]
    ok = 0
    errs = 0
    t0 = time.time()

    def work(batch):
        return translate_batch(batch, args.model)

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(work, b): b for b in batches}
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
                print(f'[失败] 批次 {n}/{len(batches)}: {e}', flush=True)
            if n % 10 == 0 or n == len(batches):
                el = time.time() - t0
                print(f'进度 {n}/{len(batches)} 批 · 成功 {ok} 条 · 失败 {errs} · 耗时 {el/60:.1f}min', flush=True)

    print(f'完成！成功 {ok} 条，失败 {errs} 条，总耗时 {(time.time()-t0)/60:.1f} 分钟', flush=True)

if __name__ == '__main__':
    main()

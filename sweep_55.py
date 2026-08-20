#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, urllib.request, urllib.parse, re, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

OUT_NDJSON = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson')
ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')

API_KEY = ''
env_path = os.path.expanduser('~/.hermes/.env')
for line in open(env_path):
    if line.startswith('GEMINI_API_KEY='):
        API_KEY = line.split('=', 1)[1].strip().strip('"').strip("'")

# 全部 2112 条
all_items = {}
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
    all_items[iid] = {'id': iid, 'title': title, 'cat': cat, 'prompt': prompt}

done_ids = set()
if OUT_NDJSON.exists():
    for l in OUT_NDJSON.read_text().splitlines():
        try: done_ids.add(json.loads(l)['id'])
        except: pass

todo = [v for k, v in all_items.items() if k not in done_ids]
print(f"剩余待补齐总数: {len(todo)} 条", flush=True)

def translate_one(item):
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key={urllib.parse.quote(API_KEY)}'
    prompt_text = f"""你是专业的 AI 提示词本地化专家。请将以下 1 条英文 AI 提示词翻译为高质量中文，并编写 100-200 字的使用说明。

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
        'contents': [{'role': 'user', 'parts': [{'text': prompt_text}]}],
        'generationConfig': {'maxOutputTokens': 8192, 'temperature': 0.1},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'}, method='POST')
    
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                res = json.loads(resp.read().decode())
                txt = res['candidates'][0]['content']['parts'][0]['text'].strip()
                txt = re.sub(r'^```(?:json)?\s*|\s*```$', '', txt)
                m = re.search(r'\{[\s\S]*\}', txt)
                if m:
                    data = json.loads(m.group(0))
                    if 'title_zh' in data and 'zh' in data and 'usage' in data:
                        data['id'] = item['id']
                        return data
        except Exception as e:
            time.sleep(2 + attempt * 2)
    raise RuntimeError(f"Failed {item['id']}")

# 采用 4 个 worker 并发快速跑完这 55 条
success = 0
with ThreadPoolExecutor(max_workers=4) as ex:
    futs = {ex.submit(translate_one, it): it for it in todo}
    for fut in as_completed(futs):
        it = futs[fut]
        try:
            data = fut.result()
            with open(OUT_NDJSON, 'a', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')
            success += 1
            print(f"[{success}/{len(todo)}] 完成: {data['title_zh']}", flush=True)
        except Exception as e:
            print(f"失败 {it['id']}: {e}", flush=True)

print(f"全部补齐扫尾完毕！成功: {success}/{len(todo)}", flush=True)

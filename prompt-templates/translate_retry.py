#!/usr/bin/env python3
"""
重试翻译失败的文件 - 使用迭代代替递归，避免深度超限
"""

import os
import re
import json
import urllib.request
import urllib.parse
import time
import sys
from pathlib import Path

sys.setrecursionlimit(10000)

def translate_text(text, src_lang='en', dest_lang='zh-CN'):
    if not text or len(text.strip()) == 0:
        return ""
    
    # 使用迭代分块，不用递归
    chunks = [text]
    if len(text) > 4000:
        chunks = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        current = ""
        for s in sentences:
            if len(current) + len(s) < 4000:
                current += " " + s
            else:
                if current.strip():
                    chunks.append(current.strip())
                current = s
        if current.strip():
            chunks.append(current.strip())
    
    results = []
    for chunk in chunks:
        encoded = urllib.parse.quote(chunk)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src_lang}&tl={dest_lang}&dt=t&q={encoded}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode())
                results.append(''.join([item[0] for item in data[0] if item[0]]))
        except Exception as e:
            print(f"  [重试翻译失败] {e}")
            results.append(chunk)
        time.sleep(0.2)
    
    return " ".join(results)

def extract_prompt_content(content):
    m = re.search(r'## Prompt Content\n\n```\n(.*?)\n```', content, re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_metadata(content):
    meta = {}
    for key, pat in [('title', r'^# (.+)$'), ('category', r'\*\*Category:\*\* (.+)$'), ('tags', r'\*\*Tags:\*\* (.+)$')]:
        m = re.search(pat, content, re.MULTILINE)
        meta[key] = m.group(1).strip() if m else ""
    return meta

def gen_instructions(category, tags):
    scenarios = {
        "Coding": "适用于编程开发场景，可帮助生成代码、调试、代码审查、架构设计等",
        "Creative": "适用于创意写作、设计、艺术创作、内容生成等场景",
        "Education": "适用于教学、学习、知识解释、课程设计等场景",
        "Business": "适用于商业分析、营销策略、管理咨询、创业规划等场景",
        "Writing": "适用于各类写作任务，如文章、邮件、报告、文案等",
        "Data Science": "适用于数据分析、机器学习、可视化、数据处理等场景",
        "Design": "适用于UI/UX设计、图形设计、产品设计、品牌设计等场景",
        "Marketing": "适用于营销策略、内容营销、广告文案、SEO优化等场景",
        "Research": "适用于学术研究、市场调研、技术调研、文献综述等场景",
        "Health": "适用于医疗健康、心理咨询、健身指导、营养建议等场景",
        "Finance": "适用于投资分析、会计处理、预算规划、金融建模等场景",
        "Translation": "适用于翻译、本地化、多语言处理等场景",
    }
    s = scenarios.get(category, "适用于各类AI辅助任务")
    return f"""### 基本用法
1. 复制下方中文提示词内容
2. 粘贴到AI工具（如ChatGPT、Claude、Gemini等）中
3. 根据需要修改方括号或变量部分
4. 获取AI生成的响应

### 适用场景
{s}

### 相关标签
{tags if tags else '暂无标签'}

### 优化技巧
- 可根据具体需求调整提示词细节
- 添加更多上下文信息可获得更精准的回答
- 尝试不同AI模型对比效果"""

def process_file(fp):
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        meta = extract_metadata(content)
        prompt = extract_prompt_content(content)
        if not prompt:
            return False
        
        t_title = translate_text(meta['title'])
        time.sleep(0.15)
        t_content = translate_text(prompt)
        time.sleep(0.15)
        
        content = re.sub(r'\n## 中文翻译\n.*$', '', content, flags=re.DOTALL)
        
        new_section = f"""

## 中文翻译

### 标题
{t_title}

### 提示词内容

```
{t_content}
```

## 使用说明
{gen_instructions(meta['category'], meta['tags'])}
"""
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content.rstrip() + new_section + "\n")
        return True
    except Exception as e:
        print(f"  [错误] {e}")
        return False

def main():
    # 扫描所有文件，找出翻译失败的（没有中文翻译部分，或翻译内容太短）
    all_files = sorted(Path("by-category").rglob("*.md"))
    need_retry = []
    
    for fp in all_files:
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 没有中文翻译部分
            if "## 中文翻译" not in content:
                need_retry.append(fp)
                continue
            
            # 翻译内容太短（可能是用原文兜底的）
            m = re.search(r'### 提示词内容\n\n```\n(.*?)\n```', content, re.DOTALL)
            if m and len(m.group(1).strip()) < 30:
                need_retry.append(fp)
        except:
            need_retry.append(fp)
    
    print(f"需要重试的文件: {len(need_retry)}")
    
    done = 0
    for i, fp in enumerate(need_retry):
        print(f"[{i+1}/{len(need_retry)}] {fp.name}", end=" ... ")
        if process_file(fp):
            done += 1
            print("✓")
        else:
            print("✗")
        if (i+1) % 20 == 0:
            print(f"  --- 进度: {done}/{i+1} ---")
    
    print(f"\n重试完成: {done}/{len(need_retry)}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
批量翻译脚本 - 接收起始和结束索引，处理指定范围的文件
用法: python3 translate_batch.py <start_index> <end_index>
"""

import os
import re
import json
import urllib.request
import urllib.parse
import time
import sys
from pathlib import Path

def translate_text(text, src_lang='en', dest_lang='zh-CN'):
    if not text or len(text.strip()) == 0:
        return ""
    if len(text) > 4500:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks, current = [], ""
        for s in sentences:
            if len(current) + len(s) < 4500:
                current += " " + s
            else:
                chunks.append(current.strip())
                current = s
        if current:
            chunks.append(current.strip())
        return " ".join(translate_text(c, src_lang, dest_lang) for c in chunks)
    
    encoded = urllib.parse.quote(text)
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src_lang}&tl={dest_lang}&dt=t&q={encoded}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return ''.join([item[0] for item in data[0] if item[0]])
    except Exception as e:
        print(f"  [翻译失败] {e}")
        return text

def extract_prompt_content(content):
    m = re.search(r'## Prompt Content\n\n```\n(.*?)\n```', content, re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_metadata(content):
    meta = {}
    for key, pattern in [('title', r'^# (.+)$'), ('category', r'\*\*Category:\*\* (.+)$'), ('tags', r'\*\*Tags:\*\* (.+)$')]:
        m = re.search(pattern, content, re.MULTILINE)
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
        
        # 翻译标题
        t_title = translate_text(meta['title'])
        time.sleep(0.15)
        # 翻译内容
        t_content = translate_text(prompt)
        time.sleep(0.15)
        
        # 移除旧翻译
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
    if len(sys.argv) < 3:
        print("用法: python3 translate_batch.py <start> <end>")
        sys.exit(1)
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    all_files = sorted(Path("by-category").rglob("*.md"))
    batch = all_files[start:end]
    
    print(f"批次: {start+1}-{end} (共{len(batch)}个文件)")
    
    done = 0
    for i, fp in enumerate(batch):
        print(f"[{start+i+1}/{len(all_files)}] {fp.name}", end=" ... ")
        if process_file(fp):
            done += 1
            print("✓")
        else:
            print("✗")
        if (i+1) % 20 == 0:
            print(f"  --- 进度: {done}/{i+1} 完成 ---")
    
    print(f"\n完成: {done}/{len(batch)}")

if __name__ == "__main__":
    main()
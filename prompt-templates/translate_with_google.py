#!/usr/bin/env python3
"""
使用Google Translate API重新翻译所有提示词文件
"""

import os
import re
import json
import urllib.request
import urllib.parse
import time
from pathlib import Path

def translate_text(text, src_lang='en', dest_lang='zh-CN'):
    """使用Google Translate API翻译文本"""
    if not text or len(text.strip()) == 0:
        return ""
    
    # 如果文本太长，分段翻译
    if len(text) > 4500:
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current_chunk = ""
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < 4500:
                current_chunk += " " + sentence
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        translated_chunks = []
        for chunk in chunks:
            translated = translate_text(chunk, src_lang, dest_lang)
            translated_chunks.append(translated)
            time.sleep(0.2)
        return " ".join(translated_chunks)
    
    # URL编码文本
    encoded_text = urllib.parse.quote(text)
    
    # Google Translate API URL
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src_lang}&tl={dest_lang}&dt=t&q={encoded_text}"
    
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode())
            # 提取翻译结果
            translated = ''.join([item[0] for item in data[0] if item[0]])
            return translated
    except Exception as e:
        print(f"翻译错误: {e}")
        return text  # 返回原文

def extract_prompt_content(content):
    """从Markdown中提取提示词内容"""
    pattern = r'## Prompt Content\n\n```\n(.*?)\n```'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_metadata(content):
    """提取元数据"""
    metadata = {}
    
    # 提取标题
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    metadata['title'] = title_match.group(1) if title_match else "Untitled"
    
    # 提取类型
    type_match = re.search(r'\*\*Type:\*\* (.+)$', content, re.MULTILINE)
    metadata['type'] = type_match.group(1) if type_match else ""
    
    # 提取作者
    author_match = re.search(r'\*\*Author:\*\* (.+)$', content, re.MULTILINE)
    metadata['author'] = author_match.group(1) if author_match else ""
    
    # 提取分类
    category_match = re.search(r'\*\*Category:\*\* (.+)$', content, re.MULTILINE)
    metadata['category'] = category_match.group(1) if category_match else ""
    
    # 提取标签
    tags_match = re.search(r'\*\*Tags:\*\* (.+)$', content, re.MULTILINE)
    metadata['tags'] = tags_match.group(1) if tags_match else ""
    
    return metadata

def generate_usage_instructions(metadata, translated_content):
    """生成中文使用说明"""
    category = metadata.get('category', '')
    tags = metadata.get('tags', '')
    
    # 根据分类生成适用场景
    category_scenarios = {
        "Coding": "适用于编程开发场景，可帮助生成代码、调试、代码审查、架构设计等",
        "Creative": "适用于创意写作、设计、艺术创作、内容生成等场景",
        "Education": "适用于教学、学习、知识解释、课程设计等场景",
        "Business": "适用于商业分析、营销策略、管理咨询、创业规划等场景",
        "Writing": "适用于各类写作任务，如文章、邮件、报告、文案等",
        "Data Science": "适用于数据分析、机器学习、可视化、数据处理等场景",
        "Design": "适用于UI/UX设计、图形设计、产品设计、品牌设计等场景",
        "Marketing": "适用于营销策略、内容营销、广告文案、SEO优化等场景",
        "Research": "适用于学术研究、市场调研、技术调研、文献综述等场景",
        "Translation": "适用于翻译、本地化、多语言处理、跨文化交流等场景",
        "Health": "适用于医疗健康、心理咨询、健身指导、营养建议等场景",
        "Finance": "适用于投资分析、会计处理、预算规划、金融建模等场景",
        "Legal": "适用于法律咨询、合同审查、合规检查、法律文书等场景",
        "HR": "适用于人力资源、招聘筛选、绩效评估、培训发展等场景"
    }
    
    scenario = category_scenarios.get(category, "适用于各类AI辅助任务")
    
    instructions = f"""### 基本用法
1. 复制下方中文提示词内容
2. 粘贴到AI工具（如ChatGPT、Claude、Gemini等）中
3. 根据需要修改方括号或变量部分
4. 获取AI生成的响应

### 适用场景
{scenario}

### 相关标签
{tags if tags else '暂无标签'}

### 优化技巧
- 可根据具体需求调整提示词细节
- 添加更多上下文信息可获得更精准的回答
- 尝试不同AI模型对比效果
- 如果效果不佳，可以尝试简化或细化提示词"""
    
    return instructions

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经有完整的中文翻译（检查是否有"提示词内容"翻译）
        if "## 中文翻译" in content and "### 提示词内容" in content:
            # 检查翻译内容是否过短（少于50个字符可能是简单翻译）
            existing_translation = re.search(r'### 提示词内容\n\n```\n(.*?)\n```', content, re.DOTALL)
            if existing_translation and len(existing_translation.group(1).strip()) > 50:
                print(f"跳过 {os.path.basename(file_path)} - 已有完整翻译")
                return False
        
        # 提取元数据
        metadata = extract_metadata(content)
        
        # 提取提示词内容
        prompt_content = extract_prompt_content(content)
        if not prompt_content:
            print(f"警告: 未找到提示词内容 {file_path}")
            return False
        
        # 翻译标题
        print(f"翻译: {metadata['title']}")
        translated_title = translate_text(metadata['title'])
        time.sleep(0.3)
        
        # 翻译提示词内容
        translated_content = translate_text(prompt_content)
        time.sleep(0.3)
        
        # 生成使用说明
        usage_instructions = generate_usage_instructions(metadata, translated_content)
        
        # 构建新的翻译部分
        new_section = f"""

## 中文翻译

### 标题
{translated_title}

### 提示词内容

```
{translated_content}
```

## 使用说明
{usage_instructions}
"""
        
        # 移除旧的翻译部分（如果存在）
        content = re.sub(r'\n## 中文翻译\n.*$', '', content, flags=re.DOTALL)
        
        # 追加新的翻译部分
        content = content.rstrip() + new_section + "\n"
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"完成: {os.path.basename(file_path)}")
        return True
        
    except Exception as e:
        print(f"处理错误 {file_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("使用Google Translate API重新翻译所有提示词文件")
    print("=" * 60)
    
    # 查找所有Markdown文件
    md_files = list(Path("by-category").rglob("*.md"))
    print(f"\n找到 {len(md_files)} 个Markdown文件")
    
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for i, md_file in enumerate(md_files):
        print(f"\n[{i+1}/{len(md_files)}] 处理中...")
        
        if process_file(md_file):
            processed_count += 1
        else:
            skipped_count += 1
        
        # 每50个文件输出进度
        if (i + 1) % 50 == 0:
            print(f"\n{'='*40}")
            print(f"进度: {i+1}/{len(md_files)}")
            print(f"已处理: {processed_count}")
            print(f"已跳过: {skipped_count}")
            print(f"{'='*40}")
    
    print(f"\n{'='*60}")
    print(f"处理完成!")
    print(f"总文件数: {len(md_files)}")
    print(f"已处理: {processed_count}")
    print(f"已跳过: {skipped_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
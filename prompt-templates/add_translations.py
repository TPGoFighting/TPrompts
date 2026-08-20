#!/usr/bin/env python3
"""
Add Chinese translations and usage instructions to prompts.chat Markdown files.
"""

import os
import re
import json
import urllib.request
import urllib.parse
import time
from pathlib import Path

def translate_text(text, src_lang='en', dest_lang='zh-CN'):
    """Translate text using Google Translate API."""
    if not text or len(text.strip()) == 0:
        return ""
    
    # URL encode the text
    encoded_text = urllib.parse.quote(text)
    
    # Google Translate API URL
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src_lang}&tl={dest_lang}&dt=t&q={encoded_text}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            # Extract translated text
            translated = ''.join([item[0] for item in data[0] if item[0]])
            return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return f"[翻译失败: {text[:50]}...]"

def extract_prompt_content(content):
    """Extract the prompt content from Markdown."""
    # Find the prompt content between ``` markers
    pattern = r'## Prompt Content\n\n```\n(.*?)\n```'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def generate_usage_instructions(title, description, category, tags):
    """Generate Chinese usage instructions based on prompt metadata."""
    instructions = []
    
    # Basic usage
    instructions.append("## 使用说明\n")
    instructions.append("### 基本用法")
    instructions.append("1. 复制下方提示词原文")
    instructions.append("2. 粘贴到AI工具（如ChatGPT、Claude、Gemini等）中")
    instructions.append("3. 根据需要修改变量部分（如有）")
    instructions.append("4. 获取AI生成的响应\n")
    
    # Category-specific instructions
    if category:
        category_instructions = {
            "Coding": "适用于编程开发场景，可帮助生成代码、调试、代码审查等",
            "Creative": "适用于创意写作、设计、艺术创作等场景",
            "Education": "适用于教学、学习、知识解释等场景",
            "Business": "适用于商业分析、营销、管理等场景",
            "Writing": "适用于各类写作任务，如文章、邮件、报告等",
            "Data Science": "适用于数据分析、机器学习、可视化等场景",
            "Design": "适用于UI/UX设计、图形设计、产品设计等场景",
            "Marketing": "适用于营销策略、内容营销、广告文案等场景",
            "Research": "适用于学术研究、市场调研、技术调研等场景",
            "Translation": "适用于翻译、本地化、多语言处理等场景"
        }
        
        if category in category_instructions:
            instructions.append(f"### 适用场景")
            instructions.append(f"{category_instructions[category]}\n")
    
    # Tag-specific tips
    if tags:
        instructions.append("### 相关标签")
        instructions.append(f"标签: {', '.join(tags)}")
        instructions.append("可根据标签查找类似提示词\n")
    
    # Variables handling
    if "${" in str(title) or "${" in str(description):
        instructions.append("### 变量说明")
        instructions.append("提示词中包含变量（如 ${variable}），使用时请替换为实际内容")
        instructions.append("变量通常用方括号或花括号标记，表示需要用户填写的部分\n")
    
    # Model recommendations
    instructions.append("### 推荐模型")
    instructions.append("适用于大多数主流AI模型：ChatGPT、Claude、Gemini、Copilot等\n")
    
    # Tips
    instructions.append("### 优化技巧")
    instructions.append("- 可根据具体需求调整提示词细节")
    instructions.append("- 添加更多上下文信息可获得更精准的回答")
    instructions.append("- 尝试不同AI模型对比效果")
    
    return "\n".join(instructions)

def process_markdown_file(file_path):
    """Process a single Markdown file to add translations and usage instructions."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has Chinese translation
        if "## 中文翻译" in content:
            print(f"Skipping {file_path} - already has translation")
            return False
        
        # Extract metadata
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Untitled"
        
        # Extract prompt content
        prompt_content = extract_prompt_content(content)
        if not prompt_content:
            print(f"Warning: No prompt content found in {file_path}")
            return False
        
        # Extract category
        category_match = re.search(r'\*\*Category:\*\* (.+)$', content, re.MULTILINE)
        category = category_match.group(1) if category_match else ""
        
        # Extract tags
        tags_match = re.search(r'\*\*Tags:\*\* (.+)$', content, re.MULTILINE)
        tags = []
        if tags_match:
            tags = [tag.strip() for tag in tags_match.group(1).split(',')]
        
        # Translate title and content
        print(f"Translating {title}...")
        translated_title = translate_text(title)
        time.sleep(0.3)  # Be polite to API
        
        translated_content = translate_text(prompt_content)
        time.sleep(0.3)
        
        # Generate usage instructions
        usage_instructions = generate_usage_instructions(title, "", category, tags)
        
        # Build new content
        new_content = content.rstrip() + "\n\n"
        new_content += "## 中文翻译\n\n"
        new_content += f"### 标题\n{translated_title}\n\n"
        new_content += "### 提示词内容\n\n"
        new_content += f"```\n{translated_content}\n```\n\n"
        new_content += usage_instructions + "\n"
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Processed: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    print("Starting translation and usage instructions addition...")
    
    # Read file list from files_part_10.txt
    file_list_path = Path("files_part_10.txt")
    if not file_list_path.exists():
        print(f"Error: {file_list_path} not found")
        return
    
    with open(file_list_path, 'r', encoding='utf-8') as f:
        file_list = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(file_list)} files in {file_list_path}")
    
    processed_count = 0
    skipped_count = 0
    
    for i, file_path_str in enumerate(file_list):
        print(f"\n[{i+1}/{len(file_list)}] Processing {file_path_str}...")
        
        # Convert to Path object
        file_path = Path(file_path_str)
        
        if process_markdown_file(file_path):
            processed_count += 1
        else:
            skipped_count += 1
        
        # Progress update every 50 files
        if (i + 1) % 50 == 0:
            print(f"\nProgress: {i+1}/{len(file_list)} files processed")
            print(f"Processed: {processed_count}, Skipped: {skipped_count}")
    
    print(f"\nCompleted!")
    print(f"Total files: {len(file_list)}")
    print(f"Processed: {processed_count}")
    print(f"Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
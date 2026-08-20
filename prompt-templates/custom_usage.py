#!/usr/bin/env python3
"""
为每个提示词文件生成定制化使用说明
用法: python3 custom_usage.py <start_index> <end_index>
"""

import os
import re
import sys
from pathlib import Path

def extract_prompt_content(content):
    m = re.search(r'## Prompt Content\n\n```\n(.*?)\n```', content, re.DOTALL)
    return m.group(1).strip() if m else ""

def extract_metadata(content):
    meta = {}
    for key, pat in [
        ('title', r'^# (.+)$'),
        ('category', r'\*\*Category:\*\* (.+)$'),
        ('tags', r'\*\*Tags:\*\* (.+)$'),
        ('description', r'\*\*Description:\*\* (.+)$')
    ]:
        m = re.search(pat, content, re.MULTILINE)
        meta[key] = m.group(1).strip() if m else ""
    return meta

def generate_custom_usage(title, description, category, tags, prompt_content):
    """根据提示词的具体内容生成定制化使用说明"""
    
    # 分析提示词内容，提取关键信息
    content_lower = prompt_content.lower()
    title_lower = title.lower()
    
    # 1. 确定提示词的具体功能
    functionality = ""
    
    if any(w in content_lower for w in ['code', 'programming', 'function', 'implement', 'debug', 'review']):
        functionality = "编程代码生成与审查"
    elif any(w in content_lower for w in ['write', 'story', 'narrative', 'creative', 'fiction']):
        functionality = "创意写作与故事创作"
    elif any(w in content_lower for w in ['design', 'ui', 'ux', 'layout', 'visual']):
        functionality = "UI/UX设计与视觉创作"
    elif any(w in content_lower for w in ['marketing', 'seo', 'content', 'social media']):
        functionality = "营销内容与SEO优化"
    elif any(w in content_lower for w in ['data', 'analysis', 'chart', 'visualization', 'statistic']):
        functionality = "数据分析与可视化"
    elif any(w in content_lower for w in ['translate', 'translation', 'localization', 'multilingual']):
        functionality = "翻译与本地化"
    elif any(w in content_lower for w in ['teach', 'learn', 'education', 'explain', 'tutorial']):
        functionality = "教育与知识讲解"
    elif any(w in content_lower for w in ['business', 'plan', 'strategy', 'market', 'pitch']):
        functionality = "商业策划与战略分析"
    elif any(w in content_lower for w in ['image', 'photo', 'picture', 'render', 'illustration']):
        functionality = "图像生成与处理"
    elif any(w in content_lower for w in ['video', 'animation', 'motion', 'edit']):
        functionality = "视频与动画制作"
    elif any(w in content_lower for w in ['email', 'letter', 'communication', 'message']):
        functionality = "邮件与商务沟通"
    elif any(w in content_lower for w in ['research', 'survey', 'investigate', 'academic']):
        functionality = "学术研究与调研"
    elif any(w in content_lower for w in ['health', 'medical', 'fitness', 'nutrition']):
        functionality = "健康与医疗咨询"
    elif any(w in content_lower for w in ['finance', 'invest', 'budget', 'accounting']):
        functionality = "财务与投资分析"
    elif any(w in content_lower for w in ['game', 'play', 'puzzle', 'riddle']):
        functionality = "游戏与娱乐互动"
    elif any(w in content_lower for w in ['recipe', 'cook', 'food', 'ingredient']):
        functionality = "美食与食谱创作"
    elif any(w in content_lower for w in ['travel', 'trip', 'itinerary', 'destination']):
        functionality = "旅行规划与攻略"
    elif any(w in content_lower for w in ['music', 'song', 'lyrics', 'melody']):
        functionality = "音乐与歌词创作"
    elif any(w in content_lower for w in ['legal', 'law', 'contract', 'compliance']):
        functionality = "法律文书与合规"
    elif any(w in content_lower for w in ['hr', 'recruit', 'interview', 'talent']):
        functionality = "人力资源与招聘"
    else:
        functionality = "AI辅助任务"
    
    # 2. 确定目标用户
    user_type = ""
    if "developer" in title_lower or "programmer" in title_lower or "coding" in category.lower():
        user_type = "开发者/程序员"
    elif "writer" in title_lower or "creative" in category.lower():
        user_type = "写作者/创意人员"
    elif "designer" in title_lower or "design" in category.lower():
        user_type = "设计师"
    elif "marketer" in title_lower or "marketing" in category.lower():
        user_type = "营销人员"
    elif "teacher" in title_lower or "education" in category.lower():
        user_type = "教师/教育工作者"
    elif "business" in title_lower or "business" in category.lower():
        user_type = "商业人士/创业者"
    else:
        user_type = "通用用户"
    
    # 3. 提取变量信息
    variables = re.findall(r'\$\{(\w+)(?::([^}]*))?\}', prompt_content)
    var_section = ""
    if variables:
        var_lines = []
        for var_name, default in variables:
            if default:
                var_lines.append(f"- `${{{var_name}}}`: 可自定义（默认值: {default}）")
            else:
                var_lines.append(f"- `${{{var_name}}}`: 需要您填写")
        var_section = "\n### 可自定义变量\n" + "\n".join(var_lines)
    
    # 4. 生成定制化使用说明
    usage = f"""### 这个提示词能帮你做什么
这是一个**{functionality}**类的提示词。{description if description else f'它可以帮助你完成与{title}相关的任务。'}

### 适用人群
{user_type}

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问{var_section}

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整"""
    
    return usage

def process_file(fp):
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取信息
        meta = extract_metadata(content)
        prompt = extract_prompt_content(content)
        if not prompt:
            return False
        
        # 生成定制化使用说明
        custom_usage = generate_custom_usage(
            meta['title'], meta['description'], 
            meta['category'], meta['tags'], prompt
        )
        
        # 移除旧的使用说明部分
        content = re.sub(r'\n## 使用说明\n.*?(?=\n## |\Z)', '', content, flags=re.DOTALL)
        
        # 追加新的使用说明
        content = content.rstrip() + f"\n\n## 使用说明\n{custom_usage}\n"
        
        # 写回文件
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  [错误] {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("用法: python3 custom_usage.py <start> <end>")
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
        if (i+1) % 50 == 0:
            print(f"  --- 进度: {done}/{i+1} ---")
    
    print(f"\n完成: {done}/{len(batch)}")

if __name__ == "__main__":
    main()
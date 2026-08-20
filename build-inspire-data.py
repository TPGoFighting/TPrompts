#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-inspire-data.py - 生成灵感板块数据 inspire-data.js
- 英文原版: prompt-templates/by-category/**/*.md（## Prompt Content）
- 大模型翻译: inspire_zh.ndjson（inspire_translate.py 产出，断点续传）
- 未翻译完成的 id 暂时用 md 内机翻兜底（最终跑完翻译后重跑即全量替换）
- 输出: window.INSPIRE_DATA（浏览器 <script> 直接加载，兼容 file://）
"""
import json, re, sys
from pathlib import Path

ROOT = Path('/Users/tylertang/Developer/ai-coding/prompt-templates/by-category')
NDJSON = Path(__file__).parent / 'inspire_zh.ndjson'
OUT = Path(__file__).parent / 'inspire-data.js'

# 55 分类中文映射（与 index.html 中 CAT_ZH 保持一致）
CAT_ZH = {
    'academic-writing': '学术写作', 'agent-workflows': '智能体工作流', 'automation-workflows': '自动化工作流',
    'automations': '自动化', 'blog-writing': '博客写作', 'business': '商业', 'business-planning': '商业规划',
    'business-strategy': '商业策略', 'coding': '编程', 'copywriting': '文案写作', 'course-creation': '课程创作',
    'creative': '创意', 'data-science': '数据科学', 'design': '设计', 'devops': '运维开发', 'education': '教育',
    'email-communication': '邮件沟通', 'exam-preparation': '考试备考', 'finance-budgeting': '财务预算',
    'habits-routines': '习惯养成', 'health-wellness': '健康生活', 'hr': '人力资源', 'image-generation': '图像生成',
    'journaling-reflection': '日记反思', 'kids-early-learning': '儿童早教', 'language-learning': '语言学习',
    'leadership-management': '领导管理', 'learning-skills': '学习技能', 'market-analysis': '市场分析',
    'marketing': '市场营销', 'marketing-sales': '营销销售', 'meeting-collaboration': '会议协作',
    'mindset-motivation': '心态激励', 'mobile-development': '移动开发', 'music': '音乐', 'note-taking': '笔记方法',
    'productivity': '效率提升', 'research-analysis': '研究分析', 'sales': '销售', 'self-improvement': '自我提升',
    'skill': '技能', 'sponsors': '赞助商', 'startup-entrepreneurship': '创业', 'stem-science': '科学工程',
    'teaching-instruction': '教学指导', 'technical-writing': '技术写作', 'tutoring-homework-help': '辅导作业',
    'uncategorized': '未分类', 'vibe': 'Vibe 编程', 'video-generation': '视频生成', 'web-development': '网页开发',
    'workflows': '工作流', 'writing': '写作'
}

def extract_en(md):
    """英文原版：## Prompt Content 代码块"""
    m = re.search(r'## Prompt Content\n+```[^\n]*\n(.*?)\n```', md, re.S)
    return m.group(1).strip() if m else ''

def extract_zh_old(md):
    """md 内旧机翻：## 中文翻译 → ### 提示词内容 代码块"""
    m = re.search(r'### 提示词内容\n+```[^\n]*\n(.*?)\n```', md, re.S)
    return m.group(1).strip() if m else ''

def extract_usage_old(md):
    """md 内旧使用说明：## 使用说明 之后到文件尾/下一个 ##"""
    m = re.search(r'## 使用说明\n(.*?)(?=\n## |\Z)', md, re.S)
    return m.group(1).strip() if m else ''

def extract_title_zh_old(md):
    m = re.search(r'### 标题\n(.+)', md)
    return m.group(1).strip() if m else ''

def make_desc(zh):
    """列表卡摘要：zh 前 90 字符（去换行）"""
    if not zh:
        return ''
    return re.sub(r'\s+', ' ', zh).strip()[:90]

# 加载大模型翻译结果
translations = {}
if NDJSON.exists():
    for line in NDJSON.read_text(encoding='utf-8').splitlines():
        try:
            r = json.loads(line)
            translations[r['id']] = r
        except Exception:
            pass

items = []
for f in sorted(ROOT.rglob('*.md')):
    md = f.read_text(encoding='utf-8')
    m = re.match(r'^([a-z0-9]{20,})_', f.name)
    iid = m.group(1) if m else ''
    if not iid:
        sm = re.search(r'prompts\.chat/prompts/([a-z0-9]+)', md)
        if not sm: continue
        iid = sm.group(1)
    tm = re.match(r'^#\s+(.+)$', md, re.M)
    title = tm.group(1).strip() if tm else f.stem
    cat = f.parent.name
    en = extract_en(md)
    if not en: continue
    tr = translations.get(iid)
    if tr:
        title_zh = tr.get('title_zh', '') or title
        zh = tr.get('zh', '')
        usage = tr.get('usage', '')
        ai = True
    else:
        title_zh = extract_title_zh_old(md) or title
        zh = extract_zh_old(md)
        usage = extract_usage_old(md)
        ai = False
    items.append({
        'id': iid,
        'title': title,
        'titleZh': title_zh,
        'cat': cat,
        'catZh': CAT_ZH.get(cat, cat),
        'en': en,
        'zh': zh,
        'usage': usage,
        'ai': ai,
        'descZh': make_desc(zh),
    })

payload = f"""/* 由 build-inspire-data.py 自动生成 · {__import__('datetime').datetime.now().isoformat()} */
/* 大模型翻译 {len(translations)} 条（inspire_zh.ndjson）+ 旧数据兜底 {len(items) - len(translations)} 条 */
window.INSPIRE_DATA = {json.dumps(items, ensure_ascii=False)};"""

OUT.write_text(payload, 'utf-8')
print(f'✓ 生成 {OUT}')
print(f'  总数: {len(items)}')
print(f'  大模型翻译: {len(translations)}（{len(translations)/len(items)*100:.0f}%）')
print(f'  旧数据兜底: {len(items) - len(translations)}')
print(f'  文件大小: {payload.__len__()/1024/1024:.2f} MB')

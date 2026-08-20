#!/usr/bin/env python3
"""清理index.html中所有和prompts.chat/灵感相关的代码"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 删除导航栏中的"灵感"链接
content = content.replace('      <a href="#/inspire" data-route="inspire">灵感</a>\n', '')

# 2. 删除灵感页相关的CSS（第122-191行）
# 找到灵感页CSS的开始和结束
css_start = content.find('/* ===== 灵感页（文本优先，无封面） ===== */')
css_end = content.find('/* ===== 分页 ===== */')
if css_start > 0 and css_end > 0:
    content = content[:css_start] + content[css_end:]

# 3. 删除inspire-data.js的引用
content = content.replace('<script src="inspire-data.js"></script>\n', '')

# 4. 删除灵感板块数据变量
content = re.sub(r'const ID = window\.INSPIRE_DATA \|\| \[\];\n', '', content)

# 5. 删除灵感板块的CAT_ZH映射（一大段）
cat_zh_start = content.find('/* 灵感页：分类中文映射 */')
if cat_zh_start > 0:
    # 找到下一个函数定义
    next_func = content.find('function catZh(')
    if next_func > cat_zh_start:
        content = content[:cat_zh_start] + content[next_func:]

# 6. 删除灵感页相关函数
functions_to_remove = [
    'function getInspireFiltered()',
    'function inspireCardHTML(',
    'function renderInspireList()',
    'function renderInspireDetail(',
    'function renderInspireContent(',
]

for func in functions_to_remove:
    start = content.find(func)
    if start > 0:
        # 找到函数开始的位置（往回找function关键字）
        func_start = content.rfind('function', 0, start)
        if func_start > 0 and start - func_start < 10:
            start = func_start
        # 找到函数结束的位置（找下一个function或const定义）
        end_patterns = ['\nfunction ', '\nconst ', '\nasync function ']
        end = len(content)
        for pattern in end_patterns:
            pos = content.find(pattern, start + 10)
            if pos > 0 and pos < end:
                end = pos
        content = content[:start] + content[end:]

# 7. 删除灵感板块的renderInspire函数调用
content = re.sub(r'renderInspire\(\);?\n', '', content)

# 8. 删除灵感板块的事件处理代码
# 删除灵感板块复制按钮
inspire_copy_start = content.find('/* 灵感板块复制按钮 */')
if inspire_copy_start > 0:
    # 找到下一个板块的开始
    next_section = content.find('/* ', inspire_copy_start + 10)
    if next_section > inspire_copy_start:
        content = content[:inspire_copy_start] + content[next_section:]

# 9. 删除灵感板块的路由处理
content = re.sub(r'if \(path === \'inspire\'\) \{[^}]*\}', '', content)

# 10. 删除首页的"每日灵感"按钮
content = re.sub(r'<button class="btn" style="font-size:15px;padding:12px 20px" data-nav="#/inspire">每日灵感 ✦</button>', '', content)

# 11. 删除灵感板块的state变量
content = content.replace('inspireCat: \'全部\', inspireQ: \'\', inspirePage: 1', '')

# 12. 清理多余的空行
content = re.sub(r'\n{3,}', '\n\n', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('清理完成！')

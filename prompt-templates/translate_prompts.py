#!/usr/bin/env python3
"""
批量翻译英文AI提示词文件，添加中文翻译和使用说明
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

# 标题翻译映射（常见词汇）
TITLE_TRANSLATIONS = {
    'Expert': '专家',
    'Master': '大师',
    'Pro': '专业版',
    'Assistant': '助手',
    'Guide': '指南',
    'Coach': '教练',
    'Tutor': '导师',
    'Generator': '生成器',
    'Analyzer': '分析器',
    'Builder': '构建器',
    'Writer': '撰写者',
    'Creator': '创作者',
    'Designer': '设计师',
    'Developer': '开发者',
    'Engineer': '工程师',
    'Consultant': '顾问',
    'Planner': '规划师',
    'Reviewer': '审查者',
    'Optimizer': '优化器',
    'Tester': '测试员',
    'Architect': '架构师',
    'Strategist': '战略家',
    'Research': '研究',
    'Analysis': '分析',
    'Product': '产品',
    'Project': '项目',
    'Code': '代码',
    'Prompt': '提示词',
    'Skill': '技能',
    'Template': '模板',
    'Framework': '框架',
    'System': '系统',
    'Mode': '模式',
    'Tool': '工具',
    'App': '应用',
    'Web': '网页',
    'Mobile': '移动',
    'Cloud': '云',
    'Data': '数据',
    'Security': '安全',
    'Network': '网络',
    'Database': '数据库',
    'API': 'API',
    'UI': '用户界面',
    'UX': '用户体验',
    'Frontend': '前端',
    'Backend': '后端',
    'Full Stack': '全栈',
    'DevOps': '运维',
    'CI/CD': '持续集成/持续部署',
    'Testing': '测试',
    'Debugging': '调试',
    'Performance': '性能',
    'Optimization': '优化',
    'Deployment': '部署',
    'Documentation': '文档',
    'Training': '培训',
    'Education': '教育',
    'Learning': '学习',
    'Tutorial': '教程',
    'Course': '课程',
    'Workshop': '研讨会',
    'Presentation': '演示',
    'Report': '报告',
    'Proposal': '提案',
    'Plan': '计划',
    'Strategy': '策略',
    'Marketing': '营销',
    'Sales': '销售',
    'Business': '商业',
    'Startup': '创业',
    'Entrepreneur': '创业者',
    'Finance': '金融',
    'Investment': '投资',
    'Trading': '交易',
    'Crypto': '加密货币',
    'Blockchain': '区块链',
    'AI': '人工智能',
    'Machine Learning': '机器学习',
    'Deep Learning': '深度学习',
    'NLP': '自然语言处理',
    'Computer Vision': '计算机视觉',
    'Robotics': '机器人',
    'IoT': '物联网',
    'AR': '增强现实',
    'VR': '虚拟现实',
    'Gaming': '游戏',
    'Music': '音乐',
    'Art': '艺术',
    'Design': '设计',
    'Writing': '写作',
    'Content': '内容',
    'Social': '社交',
    'Email': '电子邮件',
    'Chat': '聊天',
    'Customer': '客户',
    'HR': '人力资源',
    'Legal': '法律',
    'Medical': '医疗',
    'Health': '健康',
    'Fitness': '健身',
    'Nutrition': '营养',
    'Psychology': '心理学',
    'Philosophy': '哲学',
    'Science': '科学',
    'Technology': '技术',
    'Engineering': '工程',
    'Mathematics': '数学',
    'Physics': '物理',
    'Chemistry': '化学',
    'Biology': '生物',
    'History': '历史',
    'Geography': '地理',
    'Language': '语言',
    'Translation': '翻译',
    'Localization': '本地化',
    'Automation': '自动化',
    'Integration': '集成',
    'Migration': '迁移',
    'Maintenance': '维护',
    'Support': '支持',
    'Help': '帮助',
    'FAQ': '常见问题',
    'Guide': '指南',
    'Manual': '手册',
    'Handbook': '手册',
    'Reference': '参考',
    'Resource': '资源',
    'Tool': '工具',
    'Utility': '实用程序',
    'Library': '库',
    'Framework': '框架',
    'Platform': '平台',
    'Service': '服务',
    'Solution': '解决方案',
    'Package': '包',
    'Bundle': '套件',
    'Suite': '套件',
    'Kit': '工具包',
    'Set': '集合',
    'Collection': '收藏',
    'Pack': '包',
    'Bundle': '捆绑',
    'Tier': '层级',
    'Level': '级别',
    'Grade': '等级',
    'Rank': '排名',
    'Rating': '评分',
    'Score': '分数',
    'Metric': '指标',
    'KPI': '关键绩效指标',
    'ROI': '投资回报率',
    'Dashboard': '仪表板',
    'Analytics': '分析',
    'Insights': '洞察',
    'Metrics': '指标',
    'Benchmark': '基准',
    'Audit': '审计',
    'Compliance': '合规',
    'Governance': '治理',
    'Policy': '政策',
    'Regulation': '法规',
    'Standard': '标准',
    'Certification': '认证',
    'Accreditation': '认可',
    'License': '许可证',
    'Permit': '许可',
    'Permission': '权限',
    'Access': '访问',
    'Control': '控制',
    'Management': '管理',
    'Administration': '管理',
    'Operations': '运营',
    'Process': '流程',
    'Workflow': '工作流',
    'Pipeline': '管道',
    'Pipeline': '流水线',
    'Queue': '队列',
    'Stack': '技术栈',
    'Architecture': '架构',
    'Infrastructure': '基础设施',
    'Environment': '环境',
    'Configuration': '配置',
    'Settings': '设置',
    'Preferences': '首选项',
    'Options': '选项',
    'Parameters': '参数',
    'Arguments': '参数',
    'Variables': '变量',
    'Constants': '常量',
    'Functions': '函数',
    'Methods': '方法',
    'Classes': '类',
    'Objects': '对象',
    'Modules': '模块',
    'Packages': '包',
    'Libraries': '库',
    'Dependencies': '依赖',
    'Imports': '导入',
    'Exports': '导出',
    'Templates': '模板',
    'Patterns': '模式',
    'Principles': '原则',
    'Best Practices': '最佳实践',
    'Guidelines': '指南',
    'Standards': '标准',
    'Conventions': '约定',
    'Rules': '规则',
    'Constraints': '约束',
    'Limitations': '限制',
    'Requirements': '需求',
    'Specifications': '规范',
    'Documentation': '文档',
    'Comments': '注释',
    'Notes': '笔记',
    'Tips': '技巧',
    'Tricks': '窍门',
    'Hacks': '技巧',
    'Shortcuts': '快捷方式',
    'Workarounds': '变通方法',
    'Solutions': '解决方案',
    'Fixes': '修复',
    'Patches': '补丁',
    'Updates': '更新',
    'Upgrades': '升级',
    'Migrations': '迁移',
    'Backups': '备份',
    'Recovery': '恢复',
    'Disaster': '灾难',
    'Contingency': '应急',
    'Fallback': '回退',
    'Rollback': '回滚',
    'Versioning': '版本控制',
    'Branching': '分支',
    'Merging': '合并',
    'Rebasing': '变基',
    'Committing': '提交',
    'Pushing': '推送',
    'Pulling': '拉取',
    'Cloning': '克隆',
    'Forking': '分叉',
    'Reviewing': '审查',
    'Testing': '测试',
    'Debugging': '调试',
    'Profiling': '性能分析',
    'Monitoring': '监控',
    'Logging': '日志',
    'Tracing': '追踪',
    'Profiling': '性能分析',
    'Optimizing': '优化',
    'Refactoring': '重构',
    'Cleaning': '清理',
    'Formatting': '格式化',
    'Linting': '代码检查',
    'Checking': '检查',
    'Validating': '验证',
    'Verifying': '验证',
    'Certifying': '认证',
    'Approving': '批准',
    'Rejecting': '拒绝',
    'Accepting': '接受',
    'Deploying': '部署',
    'Release': '发布',
    'Publishing': '发布',
    'Shipping': '交付',
    'Rolling': '滚动',
    'Canary': '金丝雀',
    'Blue-Green': '蓝绿',
    'A/B': 'A/B',
    'Feature': '功能',
    'Flag': '标志',
    'Toggle': '开关',
    'Switch': '切换',
    'Button': '按钮',
    'Link': '链接',
    'Menu': '菜单',
    'Dialog': '对话框',
    'Modal': '模态框',
    'Popup': '弹出框',
    'Toast': '通知',
    'Alert': '警报',
    'Notification': '通知',
    'Message': '消息',
    'Input': '输入',
    'Output': '输出',
    'Form': '表单',
    'Field': '字段',
    'Label': '标签',
    'Placeholder': '占位符',
    'Tooltip': '工具提示',
    'Help': '帮助',
    'Error': '错误',
    'Warning': '警告',
    'Success': '成功',
    'Info': '信息',
    'Loading': '加载',
    'Spinner': '加载指示器',
    'Progress': '进度',
    'Bar': '栏',
    'Card': '卡片',
    'List': '列表',
    'Table': '表格',
    'Grid': '网格',
    'Layout': '布局',
    'Container': '容器',
    'Section': '部分',
    'Page': '页面',
    'Screen': '屏幕',
    'View': '视图',
    'Component': '组件',
    'Widget': '小部件',
    'Element': '元素',
    'Node': '节点',
    'Edge': '边',
    'Graph': '图',
    'Tree': '树',
    'Array': '数组',
    'String': '字符串',
    'Number': '数字',
    'Boolean': '布尔',
    'Object': '对象',
    'Function': '函数',
    'Class': '类',
    'Interface': '接口',
    'Type': '类型',
    'Enum': '枚举',
    'Struct': '结构体',
    'Union': '联合体',
    'Pointer': '指针',
    'Reference': '引用',
    'Value': '值',
    'Key': '键',
    'Pair': '键值对',
    'Map': '映射',
    'Set': '集合',
    'Queue': '队列',
    'Stack': '栈',
    'Heap': '堆',
    'Tree': '树',
    'Graph': '图',
    'List': '链表',
    'Array': '数组',
    'Matrix': '矩阵',
    'Vector': '向量',
    'Scalar': '标量',
    'Tensor': '张量',
    'Matrix': '矩阵',
    'Vector': '向量',
    'Scalar': '标量',
    'Tensor': '张量',
}

# 分类翻译
CATEGORY_TRANSLATIONS = {
    'Research & Analysis': '研究与分析',
    'Sales': '销售',
    'Self-Improvement': '自我提升',
    'Agent Skill': '代理技能',
    'Startup & Entrepreneurship': '创业与企业家精神',
    'STEM & Science': 'STEM与科学',
    'Teaching & Instruction': '教学与指导',
    'Technical Writing': '技术写作',
    'Tutoring & Homework Help': '辅导与作业帮助',
    'Uncategorized': '未分类',
    'Sponsors': '赞助商',
}

def translate_title(title):
    """翻译标题"""
    # 如果标题已经是中文，直接返回
    if re.search(r'[\u4e00-\u9fff]', title):
        return title
    
    # 尝试逐词翻译
    translated = title
    for eng, chn in sorted(TITLE_TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        translated = re.sub(r'\b' + re.escape(eng) + r'\b', chn, translated, flags=re.IGNORECASE)
    
    return translated

def extract_prompt_content(content):
    """提取提示词内容"""
    # 查找 Prompt Content 部分的代码块
    match = re.search(r'## Prompt Content\s*\n\s*```\s*\n(.*?)\n\s*```', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_metadata(content):
    """提取元数据"""
    metadata = {}
    
    # 提取标题
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    # 提取描述
    desc_match = re.search(r'\*\*Description:\*\*\s*(.+?)(?:\n\*\*|$)', content, re.DOTALL)
    if desc_match:
        metadata['description'] = desc_match.group(1).strip()
    
    # 提取标签
    tags_match = re.search(r'\*\*Tags?:\*\*\s*(.+)$', content, re.MULTILINE)
    if tags_match:
        metadata['tags'] = tags_match.group(1).strip()
    
    # 提取分类
    category_match = re.search(r'\*\*Category:\*\*\s*(.+)$', content, re.MULTILINE)
    if category_match:
        metadata['category'] = category_match.group(1).strip()
    
    return metadata

def generate_usage_instructions(metadata, prompt_content):
    """生成使用说明"""
    category = metadata.get('category', '未分类')
    tags = metadata.get('tags', '')
    title = metadata.get('title', '')
    description = metadata.get('description', '')
    
    # 翻译分类
    category_cn = CATEGORY_TRANSLATIONS.get(category, category)
    
    # 根据标题和标签判断更具体的场景
    title_lower = title.lower() if title else ''
    tags_lower = tags.lower() if tags else ''
    content_lower = prompt_content.lower() if prompt_content else ''
    
    # 判断是否为编程类
    is_programming = any(kw in title_lower or kw in tags_lower or kw in content_lower 
                        for kw in ['code', 'programming', 'developer', 'engineer', 'python', 'javascript', 
                                   'typescript', 'api', 'database', 'sql', 'frontend', 'backend', 'devops',
                                   '代码', '编程', '开发'])
    
    # 判断是否为创意类
    is_creative = any(kw in title_lower or kw in tags_lower or kw in content_lower 
                     for kw in ['creative', 'design', 'art', 'writing', 'content', 'video', 'image',
                                '创意', '设计', '艺术', '写作', '内容', '视频', '图像'])
    
    # 判断是否为商业类
    is_business = any(kw in title_lower or kw in tags_lower or kw in content_lower 
                     for kw in ['business', 'marketing', 'sales', 'startup', 'investment', 'finance',
                                '商业', '营销', '销售', '创业', '投资', '金融'])
    
    # 判断是否为研究类
    is_research = any(kw in title_lower or kw in tags_lower or kw in content_lower 
                     for kw in ['research', 'analysis', 'study', 'data', 'report', 'survey',
                                '研究', '分析', '学习', '数据', '报告', '调查'])
    
    # 生成适用场景
    scenarios = []
    if is_programming:
        scenarios.append("适用于代码开发、API设计、数据库优化、前端/后端开发等编程相关场景")
    if is_creative:
        scenarios.append("适用于内容创作、设计生成、视频制作、图像设计等创意场景")
    if is_business:
        scenarios.append("适用于商业分析、营销策略、销售优化、投资决策等商业场景")
    if is_research:
        scenarios.append("适用于学术研究、数据分析、市场调研、报告撰写等研究场景")
    
    if not scenarios:
        scenarios.append("适用于各类需要AI辅助的任务场景")
    
    scenario_text = "；".join(scenarios) + "。"
    
    # 生成标签
    if tags:
        tags_text = tags
    else:
        tags_text = "AI提示词, " + category_cn
    
    # 根据内容长度给出使用建议
    content_length = len(prompt_content) if prompt_content else 0
    if content_length > 2000:
        length_tip = "此提示词内容较长，建议直接复制完整内容使用，以获得最佳效果。"
    elif content_length > 500:
        length_tip = "此提示词内容适中，可根据具体需求适当调整细节。"
    else:
        length_tip = "此提示词较为简洁，可根据具体需求添加更多上下文信息。"
    
    instructions = f"""## 使用说明

### 基本用法
1. 复制下方提示词原文
2. 粘贴到AI工具（如ChatGPT、Claude、Gemini等）中
3. 根据需要修改变量部分（如有）
4. 获取AI生成的响应

### 适用场景
{scenario_text}

### 相关标签
标签: {tags_text}

### 优化技巧
- {length_tip}
- 添加更多上下文信息可获得更精准的回答
- 尝试不同AI模型对比效果"""
    
    return instructions

def translate_prompt(prompt_content):
    """翻译提示词内容（使用词典翻译）"""
    # 使用词典翻译常见词汇
    translated = prompt_content
    
    # 翻译常见词汇（保留技术术语）
    translations = {
        'Create': '创建',
        'Build': '构建',
        'Implement': '实现',
        'Design': '设计',
        'Develop': '开发',
        'Add': '添加',
        'Include': '包含',
        'Use': '使用',
        'with': '使用',
        'and': '和',
        'or': '或',
        'for': '用于',
        'the': '（定冠词）',
        'a': '一个',
        'an': '一个',
        'game': '游戏',
        'app': '应用',
        'tool': '工具',
        'feature': '功能',
        'system': '系统',
        'platform': '平台',
        'website': '网站',
        'page': '页面',
        'component': '组件',
        'function': '函数',
        'method': '方法',
        'class': '类',
        'module': '模块',
        'file': '文件',
        'code': '代码',
        'test': '测试',
        'bug': '缺陷',
        'error': '错误',
        'debug': '调试',
        'fix': '修复',
        'update': '更新',
        'improve': '改进',
        'optimize': '优化',
        'refactor': '重构',
        'document': '文档',
        'comment': '注释',
        'variable': '变量',
        'constant': '常量',
        'parameter': '参数',
        'argument': '参数',
        'return': '返回',
        'value': '值',
        'type': '类型',
        'string': '字符串',
        'number': '数字',
        'boolean': '布尔',
        'array': '数组',
        'object': '对象',
        'function': '函数',
        'class': '类',
        'interface': '接口',
        'import': '导入',
        'export': '导出',
        'module': '模块',
        'package': '包',
        'library': '库',
        'framework': '框架',
        'database': '数据库',
        'server': '服务器',
        'client': '客户端',
        'API': 'API',
        'HTTP': 'HTTP',
        'URL': 'URL',
        'request': '请求',
        'response': '响应',
        'endpoint': '端点',
        'route': '路由',
        'middleware': '中间件',
        'authentication': '身份验证',
        'authorization': '授权',
        'security': '安全',
        'performance': '性能',
        'scalability': '可扩展性',
        'reliability': '可靠性',
        'usability': '可用性',
        'accessibility': '可访问性',
        'responsive': '响应式',
        'mobile': '移动端',
        'desktop': '桌面端',
        'browser': '浏览器',
        'platform': '平台',
        'environment': '环境',
        'configuration': '配置',
        'settings': '设置',
        'options': '选项',
        'features': '功能',
        'requirements': '需求',
        'specifications': '规范',
        'documentation': '文档',
        'tutorial': '教程',
        'guide': '指南',
        'example': '示例',
        'sample': '示例',
        'template': '模板',
        'boilerplate': '样板',
        'starter': '入门',
        'starter': '入门',
        'demo': '演示',
        'prototype': '原型',
        'proof': '概念',
        'concept': '概念',
        'idea': '想法',
        'plan': '计划',
        'strategy': '策略',
        'approach': '方法',
        'methodology': '方法论',
        'technique': '技术',
        'technology': '技术',
        'tool': '工具',
        'utility': '实用程序',
        'helper': '助手',
        'assistant': '助手',
        'bot': '机器人',
        'agent': '代理',
        'service': '服务',
        'provider': '提供商',
        'client': '客户端',
        'user': '用户',
        'admin': '管理员',
        'role': '角色',
        'permission': '权限',
        'access': '访问',
        'control': '控制',
        'management': '管理',
        'administration': '管理',
        'operation': '操作',
        'process': '流程',
        'workflow': '工作流',
        'pipeline': '流水线',
        'queue': '队列',
        'stack': '技术栈',
        'architecture': '架构',
        'structure': '结构',
        'design': '设计',
        'pattern': '模式',
        'principle': '原则',
        'practice': '实践',
        'standard': '标准',
        'convention': '约定',
        'rule': '规则',
        'constraint': '约束',
        'limitation': '限制',
        'requirement': '需求',
        'specification': '规范',
        'documentation': '文档',
        'comment': '注释',
        'note': '笔记',
        'tip': '技巧',
        'trick': '窍门',
        'hack': '技巧',
        'shortcut': '快捷方式',
        'workaround': '变通方法',
        'solution': '解决方案',
        'fix': '修复',
        'patch': '补丁',
        'update': '更新',
        'upgrade': '升级',
        'migration': '迁移',
        'backup': '备份',
        'recovery': '恢复',
        'disaster': '灾难',
        'contingency': '应急',
        'fallback': '回退',
        'rollback': '回滚',
        'versioning': '版本控制',
        'branching': '分支',
        'merging': '合并',
        'rebasing': '变基',
        'committing': '提交',
        'pushing': '推送',
        'pulling': '拉取',
        'cloning': '克隆',
        'forking': '分叉',
        'reviewing': '审查',
        'testing': '测试',
        'debugging': '调试',
        'profiling': '性能分析',
        'monitoring': '监控',
        'logging': '日志',
        'tracing': '追踪',
        'profiling': '性能分析',
        'optimizing': '优化',
        'refactoring': '重构',
        'cleaning': '清理',
        'formatting': '格式化',
        'linting': '代码检查',
        'checking': '检查',
        'validating': '验证',
        'verifying': '验证',
        'certifying': '认证',
        'approving': '批准',
        'rejecting': '拒绝',
        'accepting': '接受',
        'deploying': '部署',
        'release': '发布',
        'publishing': '发布',
        'shipping': '交付',
        'rolling': '滚动',
        'canary': '金丝雀',
        'blue-green': '蓝绿',
        'A/B': 'A/B',
        'feature': '功能',
        'flag': '标志',
        'toggle': '开关',
        'switch': '切换',
        'button': '按钮',
        'link': '链接',
        'menu': '菜单',
        'dialog': '对话框',
        'modal': '模态框',
        'popup': '弹出框',
        'toast': '通知',
        'alert': '警报',
        'notification': '通知',
        'message': '消息',
        'input': '输入',
        'output': '输出',
        'form': '表单',
        'field': '字段',
        'label': '标签',
        'placeholder': '占位符',
        'tooltip': '工具提示',
        'help': '帮助',
        'error': '错误',
        'warning': '警告',
        'success': '成功',
        'info': '信息',
        'loading': '加载',
        'spinner': '加载指示器',
        'progress': '进度',
        'bar': '栏',
        'card': '卡片',
        'list': '列表',
        'table': '表格',
        'grid': '网格',
        'layout': '布局',
        'container': '容器',
        'section': '部分',
        'page': '页面',
        'screen': '屏幕',
        'view': '视图',
        'component': '组件',
        'widget': '小部件',
        'element': '元素',
        'node': '节点',
        'edge': '边',
        'graph': '图',
        'tree': '树',
        'array': '数组',
        'string': '字符串',
        'number': '数字',
        'boolean': '布尔',
        'object': '对象',
        'function': '函数',
        'class': '类',
        'interface': '接口',
        'type': '类型',
        'enum': '枚举',
        'struct': '结构体',
        'union': '联合体',
        'pointer': '指针',
        'reference': '引用',
        'value': '值',
        'key': '键',
        'pair': '键值对',
        'map': '映射',
        'set': '集合',
        'queue': '队列',
        'stack': '栈',
        'heap': '堆',
        'tree': '树',
        'graph': '图',
        'list': '链表',
        'array': '数组',
        'matrix': '矩阵',
        'vector': '向量',
        'scalar': '标量',
        'tensor': '张量',
    }
    
    # 逐词翻译（保留技术术语）
    for eng, chn in translations.items():
        # 使用单词边界匹配，避免部分匹配
        pattern = r'\b' + re.escape(eng) + r'\b'
        translated = re.sub(pattern, chn, translated, flags=re.IGNORECASE)
    
    # 添加中文说明
    return f"""【中文翻译说明】以下为英文提示词的中文翻译（部分技术术语保留英文原文），请参考下方使用说明了解其用途和用法。

{translated}"""

def process_file(file_path):
    """处理单个文件"""
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取元数据
        metadata = extract_metadata(content)
        
        # 提取提示词内容
        prompt_content = extract_prompt_content(content)
        if not prompt_content:
            return False, "无法提取提示词内容"
        
        # 删除已有的翻译部分
        if '## 中文翻译' in content:
            # 找到翻译部分的开始位置
            translation_start = content.find('## 中文翻译')
            # 截取翻译前的内容
            content = content[:translation_start].rstrip()
        
        # 翻译标题
        title_cn = translate_title(metadata.get('title', ''))
        
        # 翻译提示词
        prompt_cn = translate_prompt(prompt_content)
        
        # 生成使用说明
        usage_instructions = generate_usage_instructions(metadata, prompt_content)
        
        # 构建追加内容
        append_content = f"""

## 中文翻译

### 标题
{title_cn}

### 提示词内容

```
{prompt_cn}
```

{usage_instructions}
"""
        
        # 写入文件（覆盖）
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content + append_content)
        
        return True, "处理成功"
    
    except Exception as e:
        return False, f"错误: {str(e)}"

def main():
    """主函数"""
    # 读取文件列表
    files_list_path = '/Users/tylertang/Developer/ai-coding/prompt-templates/files_part_10.txt'
    
    with open(files_list_path, 'r', encoding='utf-8') as f:
        files = [line.strip() for line in f if line.strip()]
    
    print(f"共找到 {len(files)} 个文件需要处理")
    
    # 处理每个文件
    success_count = 0
    fail_count = 0
    
    for i, file_rel_path in enumerate(files, 1):
        file_path = os.path.join('/Users/tylertang/Developer/ai-coding/prompt-templates', file_rel_path)
        
        if not os.path.exists(file_path):
            print(f"[{i}/{len(files)}] 文件不存在: {file_rel_path}")
            fail_count += 1
            continue
        
        success, message = process_file(file_path)
        
        if success:
            print(f"[{i}/{len(files)}] ✓ {file_rel_path} - {message}")
            success_count += 1
        else:
            print(f"[{i}/{len(files)}] ✗ {file_rel_path} - {message}")
            fail_count += 1
    
    print(f"\n处理完成！成功: {success_count}, 失败: {fail_count}")

if __name__ == '__main__':
    main()

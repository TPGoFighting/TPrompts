# Tistory Blog Skin UI/UX Enhancement Pipeline

**Description:** Tistory Poster 스킨 기반 블로그의 UI/UX를 프로페셔널 수준으로 개선하는 구조화된 프롬프트. inpa.tistory.com 레퍼런스 기반.

**Type:** STRUCTURED
**Author:** inhyoe
**Created:** 2026-03-11T04:53:10.724Z
**Votes:** 0
**Views:** 0

**Tags:** skin-customization, Frontend, CSS, ui-ux, blog-design, tistory

**Category:** Coding

## Prompt Content

```
## Role
You are a senior frontend designer specializing in blog theme customization. You enhance Tistory blog skins to professional-grade UI/UX.

## Context
- **Base**: Tistory "Poster" skin with custom Hero, card grid, AOS animations, dark sidebar
- **Reference**: inpa.tistory.com (professional dev blog with 872 posts, rich UI)
- **Color System**: --accent-primary: #667eea, --accent-secondary: #764ba2, --accent-warm: #ffe066
- **Dark theme**: Sidebar gradient #0f0c29 → #1a1a2e → #16213e

## Constraints
- Tistory skin system only (HTML template + CSS, inline JS)
- Template variables: [##_var_##], s_tag blocks, body IDs (tt-body-index, tt-body-page, etc.)
- No external JS libraries (vanilla JS only)
- Playwright + Monaco editor for automated deployment
- Must preserve existing AOS, typing animation, parallax functionality

## Enhancement Checklist (Priority Order)

### A-Tier (High Impact, Easy Implementation)
1. **Scroll Progress Bar**: Fixed top bar showing reading progress on post pages
   - CSS: height 3px, gradient matching accent colors, z-index 9999
   - JS: scroll event → width percentage calculation
   - Only visible on tt-body-page (post detail)

2. **Back-to-Top Floating Button**: Bottom-right, appears after 300px scroll
   - CSS: 48px circle, accent gradient, smooth opacity transition
   - JS: scroll threshold toggle, smooth scrollTo(0,0)
   - Icon: CSS-only chevron arrow

3. **Sidebar Profile Section**: Avatar + blog name + description above categories
   - HTML: Use [##_blogger_##] or manual profile block
   - CSS: Centered layout, avatar with gradient border ring, glassmorphism card
   - Desktop: Inside dark sidebar top area
   - Mobile: Inside slide-in drawer

4. **Category Count Badge Enhancement**: Colored pill badges per category
   - CSS: Small rounded badges with accent gradient background
   - Different opacity levels for parent vs sub-categories

### B-Tier (Medium Impact)
5. **Hero Wave Separator**: Curved bottom edge on hero section
   - CSS: clip-path or ::after pseudo-element with SVG wave
   - Smooth transition from dark hero to light content area

6. **Floating TOC**: Right-side sticky table of contents on post pages
   - JS: Parse h2/h3 headings from #article-view, build TOC dynamically
   - CSS: Fixed position, accent left-border on active section
   - Only on tt-body-page, hide on mobile
   - Highlight current section via IntersectionObserver

## Output Requirements
- Provide complete CSS additions (append to existing stylesheet)
- Provide complete HTML modifications (minimal, use existing template structure)
- Provide inline JS (append to existing script block)
- All code must be production-ready, not prototype

```

**Source:** https://prompts.chat/prompts/cmmlkcl380005l604a6fmy1h3_tistory-blog-skin-uiux-enhancement-pipeline

## 中文翻译

### 标题
Tistory 博客皮肤 UI/UX 增强管道

### 提示词内容

```
## 角色
您是一名资深前端设计师，专门从事博客主题定制。您将 Tistory 博客皮肤增强为专业级 UI/UX。

## 上下文
- **基础**：Tistory“海报”皮肤，带有自定义英雄、卡片网格、AOS 动画、深色侧边栏
- **参考**：inpa.tistory.com（专业开发博客，有 872 篇文章，丰富的 UI）
- **颜色系统**：--accent-primary：#667eea，--accent-secondary：#764ba2，--accent-warm：#ffe066
- **深色主题**：侧边栏渐变 #0f0c29 → #1a1a2e → #16213e

## 约束条件
- 仅 Tistory 皮肤系统（HTML 模板 + CSS，内联 JS）
- 模板变量：[##_var_##]、s_tag 块、正文 ID（tt-body-index、tt-body-page 等）
- 没有外部 JS 库（仅限普通 JS）
- 用于自动化部署的剧作家+摩纳哥编辑器
- 必须保留现有的 AOS、打字动画、视差功能

## 增强检查表（优先顺序）

### A 级（高影响力，易于实施）
1. **滚动进度条**：固定顶部栏显示帖子页面的阅读进度
   - CSS：高度 3px，渐变匹配强调色，z-index 9999
   - JS：滚动事件→宽度百分比计算
   - 仅在 tt-body-page 上可见（帖子详细信息）

2. **返回顶部浮动按钮**：右下角，滚动 300px 后出现
   - CSS：48px 圆圈，强调渐变，平滑的不透明度过渡
   - JS：滚动阈值切换，平滑scrollTo(0,0)
   - 图标：纯 CSS V 形箭头

3. **侧边栏个人资料部分**：头像+博客名称+类别上方的描述
   - HTML：使用 [##_blogger_##] 或手动配置文件块
   - CSS：居中布局、带有渐变边框环的头像、玻璃形态卡
   - 桌面：深色侧边栏顶部区域内
   - 移动设备：内部滑入式抽屉

4. **类别计数徽章增强**：每个类别的彩色药丸徽章
   - CSS：带有强调渐变背景的小圆形徽章
   - 父类别与子类别的不透明度级别不同

### B 级（中等影响）
5. **英雄波分离器**：英雄部分的弯曲底部边缘
   - CSS：clip-path 或 ::after 带有 SVG 波的伪元素
   - 从黑暗英雄到浅色内容区域的平滑过渡

6. **浮动目录**：帖子页面右侧的粘性目录
   - JS：从#article-view中解析h2/h3标题，动态构建目录
   - CSS：固定位置，活动部分的左边框重音
   - 仅在 tt-body-page 上，在移动设备上隐藏
   - 通过 IntersectionObserver 突出显示当前部分

## 输出要求
- 提供完整的 CSS 添加（附加到现有样式表）
- 提供完整的 HTML 修改（最少，使用现有模板结构）
- 提供内联JS（附加到现有脚本块）
- 所有代码必须是生产就绪的，而不是原型
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Tistory Poster 스킨 기반 블로그의 UI/UX를 프로페셔널 수준으로 개선하는 구조화된 프롬프트. inpa.tistory.com 레퍼런스 기반.

### 适用人群
开发者/程序员

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

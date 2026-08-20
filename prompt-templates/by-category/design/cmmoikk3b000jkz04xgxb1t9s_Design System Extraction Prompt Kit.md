# Design System Extraction Prompt Kit

**Description:** This prompt instructs Claude to crawl the entire codebase and extract every design-related token, pattern, and component into a raw inventory. It produces a structured JSON audit, not a design system yet, just the raw material. Run this first before any organization or documentation happens.

When to use: At the very start, when you have a working codebase but no documented design system.

**Type:** TEXT
**Author:** gokbeyinac
**Created:** 2026-03-13T06:26:41.976Z
**Votes:** 2
**Views:** 0

**Tags:** design, ui-ux

**Category:** Design

## Prompt Content

```
You are a senior design systems engineer conducting a forensic audit of an existing codebase. Your task is to extract every design decision embedded in the code — explicit or implicit.

## Project Context
- **Framework:** [Next.js / React / etc.]
- **Styling approach:** [Tailwind / CSS Modules / Styled Components / etc.]
- **Component library:** [shadcn/ui / custom / MUI / etc.]
- **Codebase location:** [path or "uploaded files"]

## Extraction Scope

Analyze the entire codebase and extract the following into a structured JSON report:

### 1. Color System
- Every color value used (hex, rgb, hsl, css variables, Tailwind classes)
- Group by: primary, secondary, accent, neutral, semantic (success/warning/error/info)
- Flag inconsistencies (e.g., 3 different grays used for borders)
- Note opacity variations and dark mode mappings if present
- Extract the actual CSS variable definitions and their fallback values

### 2. Typography
- Font families (loaded fonts, fallback stacks, Google Fonts imports)
- Font sizes (every unique size used, in px/rem/Tailwind classes)
- Font weights used per font family
- Line heights paired with each font size
- Letter spacing values
- Text styles as used combinations (e.g., "heading-large" = Inter 32px/700/1.2)
- Responsive typography rules (mobile vs desktop sizes)

### 3. Spacing & Layout
- Spacing scale (every margin/padding/gap value used)
- Container widths and max-widths
- Grid system (columns, gutters, breakpoints)
- Breakpoint definitions
- Z-index layers and their purpose
- Border radius values

### 4. Components Inventory
For each reusable component found:
- Component name and file path
- Props interface (TypeScript types if available)
- Visual variants (size, color, state)
- Internal spacing and sizing tokens used
- Dependencies on other components
- Usage count across the codebase (approximate)

### 5. Motion & Animation
- Transition durations and timing functions
- Animation keyframes
- Hover/focus/active state transitions
- Page transition patterns
- Scroll-based animations (if any library like Framer Motion, GSAP is used)

### 6. Iconography & Assets
- Icon system (Lucide, Heroicons, custom SVGs, etc.)
- Icon sizes used
- Favicon and logo variants

### 7. Inconsistencies Report
- Duplicate values that should be tokens (e.g., `#1a1a1a` used 47 times but not a variable)
- Conflicting patterns (e.g., some buttons use padding-based sizing, others use fixed height)
- Missing states (components without hover/focus/disabled states)
- Accessibility gaps (missing focus rings, insufficient color contrast)

## Output Format

Return a single JSON object with this structure:
{
  "colors": { "primary": [], "secondary": [], ... },
  "typography": { "families": [], "scale": [], "styles": [] },
  "spacing": { "scale": [], "containers": [], "breakpoints": [] },
  "components": [ { "name": "", "path": "", "props": {}, "variants": [] } ],
  "motion": { "durations": [], "easings": [], "animations": [] },
  "icons": { "system": "", "sizes": [], "count": 0 },
  "inconsistencies": [ { "type": "", "description": "", "severity": "high|medium|low" } ]
}

Do NOT attempt to organize or improve anything yet.
Do NOT suggest token names or restructuring.
Just extract what exists, exactly as it is.
```

**Source:** https://prompts.chat/prompts/cmmoikk3b000jkz04xgxb1t9s_design-system-extraction-prompt-kit

## 中文翻译

### 标题
设计系统提取提示套件

### 提示词内容

```
您是一名高级设计系统工程师，对现有代码库进行取证审计。您的任务是提取代码中嵌入的每个设计决策（显式或隐式）。

## 项目背景
- **框架：** [Next.js / React / 等]
- **样式方法：** [Tailwind / CSS 模块 / 样式组件 / 等]
- **组件库：** [shadcn/ui/自定义/MUI/等]
- **代码库位置：** [路径或“上传的文件”]

## 提取范围

分析整个代码库并将以下内容提取到结构化 JSON 报告中：

### 1. 色彩系统
- 使用的每个颜色值（十六进制、RGB、HSL、CSS 变量、Tailwind 类）
- 分组依据：主要、次要、重音、中性、语义（成功/警告/错误/信息）
- 标记不一致（例如，边框使用 3 种不同的灰色）
- 注意不透明度变化和暗模式映射（如果存在）
- 提取实际的 CSS 变量定义及其后备值

### 2. 版式
- 字体系列（加载字体、后备堆栈、Google 字体导入）
- 字体大小（使用的每个独特大小，以 px/rem/Tailwind 类为单位）
- 每个字体系列使用的字体粗细
- 行高与每个字体大小配对
- 字母间距值
- 使用组合的文本样式（例如，“heading-large”= Inter 32px/700/1.2）
- 响应式排版规则（移动与桌面尺寸）

### 3. 间距和布局
- 间距比例（使用的每个边距/填充/间隙值）
- 容器宽度和最大宽度
- 网格系统（列、装订线、断点）
- 断点定义
- Z 索引层及其用途
- 边界半径值

### 4. 零部件库存
对于找到的每个可重用组件：
- 组件名称和文件路径
- Props 接口（TypeScript 类型，如果可用）
- 视觉变体（尺寸、颜色、状态）
- 使用内部间距和尺寸标记
- 对其他组件的依赖
- 整个代码库的使用计数（大约）

### 5. 动作与动画
- 过渡持续时间和计时功能
- 动画关键帧
- 悬停/焦点/活动状态转换
- 页面过渡模式
- 基于滚动的动画（如果使用任何像 Framer Motion、GSAP 这样的库）

### 6. 图像和资产
- 图标系统（Lucide、Heroicons、自定义 SVG 等）
- 使用的图标尺寸
- 网站图标和徽标变体

### 7. 不一致报告
- 应该是标记的重复值（例如，“#1a1a1a”使用了 47 次，但不是变量）
- 冲突的模式（例如，一些按钮使用基于填充的尺寸，其他按钮使用固定高度）
- 缺少状态（没有悬停/焦点/禁用状态的组件）
- 可访问性差距（缺少对焦环、色彩对比度不足）

## 输出格式

返回具有以下结构的单个 JSON 对象：
{
  “颜色”：{ “主要”：[]，“次要”：[]，... }，
  “版式”：{“家庭”：[]，“规模”：[]，“样式”：[]}，
  “间距”：{“规模”：[]，“容器”：[]，“断点”：[]}，
  “组件”：[{“名称”：“”，“路径”：“”，“道具”：{}，“变体”：[]}]，
  “运动”：{“持续时间”：[]，“缓动”：[]，“动画”：[]}，
  “图标”：{“系统”：“”，“尺寸”：[]，“计数”：0 }，
  “不一致”：[ {“类型”：“”，“描述”：“”，“严重性”：“高|中|低”}]
}

暂时不要尝试组织或改进任何事情。
请勿建议代币名称或重组。
只需提取存在的内容，原样提取即可。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt instructs Claude to crawl the entire codebase and extract every design-related token, pattern, and component into a raw inventory. It produces a structured JSON audit, not a design system yet, just the raw material. Run this first before any organization or documentation happens.

### 适用人群
设计师

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

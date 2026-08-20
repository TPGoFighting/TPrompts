# Design Brief

**Type:** TEXT
**Author:** fariasandreluiz
**Created:** 2026-06-05T23:05:19.118Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
This is a ${page_type:dashboard} of a modern ${focus:government audit} app called ${brand:AuditFlow}.

Thoroughly analyze the UI in this screenshot and describe it in as much detail as you can to hand over from a UI designer to a developer. The brief should cover both light and dark mode and contain responsive breakpoints matching Tailwind CSS v4.3 defaults.

Output characteristics as structured JSONC.

For colors, extract a rough palette and only detail accents and complex media. The goal is to use only 2 palettes: primary and secondary similar to Tailwind colors. Alongside these 2, you can define any number of grays and accent colors for more complex UI (gradients, shadows, SVGs, etc.).

End with a prompt explaining how to implement the UI for a developer, but don't mention any tech specs; only a brief of the UI to be implemented and the token rules + usage. Output the prompt as a Markdown code block.

The output should be two code blocks: one for the design brief and one for the JSONC design specification.
```

**Source:** https://prompts.chat/prompts/cmq1j8cge0001jv04l5usduv3_design-brief

## 中文翻译

### 标题
设计简介

### 提示词内容

```
这是一个名为 ${brand:AuditFlow} 的现代 ${focus:governmentaudit} 应用程序的 ${page_type:dashboard}。

彻底分析此屏幕截图中的 UI，并尽可能详细地描述它，然后将其从 UI 设计师移交给开发人员。简介应涵盖浅色和深色模式，并包含与 Tailwind CSS v4.3 默认值匹配的响应断点。

输出特征为结构化 JSONC。

对于颜色，提取粗略的调色板，仅提取细节强调和复杂的媒体。目标是仅使用 2 个调色板：主要调色板和次要调色板，类似于 Tailwind 颜色。除了这 2 个之外，您还可以为更复杂的 UI（渐变、阴影、SVG 等）定义任意数量的灰色和强调色。

最后提示解释如何为开发人员实现 UI，但不要提及任何技术规格；仅简要介绍要实现的 UI 和令牌规则 + 用法。将提示输出为 Markdown 代码块。

输出应该是两个代码块：一个用于设计概要，另一个用于 JSONC 设计规范。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Design Brief相关的任务。

### 适用人群
通用用户

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问
### 可自定义变量
- `${page_type}`: 可自定义（默认值: dashboard）
- `${focus}`: 可自定义（默认值: government audit）
- `${brand}`: 可自定义（默认值: AuditFlow）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

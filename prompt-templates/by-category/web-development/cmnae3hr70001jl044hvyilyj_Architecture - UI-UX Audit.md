# Architecture & UI/UX Audit

**Description:** It asks an AI to assume the persona of a Senior Frontend Engineer & Product Reviewer to perform a high-level critique of a Next.js (App Router) project. Instead of writing code, the prompt focuses on evaluating the architecture (folder structure, scalability), UI/UX (hierarchy, consistency), and design system (component reuse) of a developer community platform to identify anti-patterns and suggest high-impact improvements.

**Type:** TEXT
**Author:** surendharnadh280709
**Created:** 2026-03-28T13:52:23.202Z
**Votes:** 3
**Views:** 0

**Category:** Web Development

## Prompt Content

```
Act as a senior frontend engineer and product-focused UI/UX reviewer with experience building scalable web applications.

Your task is NOT to write code yet.

First, carefully analyze the project based on:

1. Folder structure (Next.js App Router architecture, route groups, component organization)
2. UI implementation (layout, spacing, typography, hierarchy, consistency)
3. Component reuse and design system consistency
4. Separation of concerns (layout vs pages vs components)
5. Scalability and maintainability of the current structure

Context:
This is a modern Next.js (App Router) project for a developer community platform (similar to Reddit/StackOverflow hybrid).

Instructions:

* Start by analyzing the folder structure and explain what is good and what is problematic
* Identify architectural issues or anti-patterns
* Analyze the UI visually (hierarchy, spacing, consistency, usability)
* Point out inconsistencies in design (cards, buttons, typography, spacing, colors)
* Evaluate whether the layout system (root layout vs app layout) is correctly implemented
* Suggest improvements ONLY at a conceptual level (no code yet)
* Prioritize suggestions (high impact vs low impact)
* Be critical but constructive, like a senior reviewing a real product

Output format:

1. Overall assessment (brief)
2. Folder structure review
3. UI/UX review
4. Design system issues
5. Top 5 high-impact improvements

Do NOT generate code yet.
Focus only on analysis and recommendations.
```

**Source:** https://prompts.chat/prompts/cmnae3hr70001jl044hvyilyj_architecture-uiux-audit

## 中文翻译

### 标题
架构和 UI/UX 审计

### 提示词内容

```
担任高级前端工程师和以产品为中心的 UI/UX 审核员，拥有构建可扩展 Web 应用程序的经验。

您的任务还不是编写代码。

首先，根据以下内容仔细分析该项目：

1.文件夹结构（Next.js App Router架构、路由组、组件组织）
2. UI实现（布局、间距、排版、层次结构、一致性）
3. 组件复用和设计系统一致性
4. 关注点分离（布局、页面、组件）
5、现有结构的可扩展性和可维护性

背景：
这是一个面向开发者社区平台的现代 Next.js (App Router) 项目（类似于 Reddit/StackOverflow 混合平台）。

说明：

* 从分析文件夹结构开始，解释什么是好的，什么是有问题的
* 识别架构问题或反模式
* 直观地分析 UI（层次结构、间距、一致性、可用性）
* 指出设计中的不一致之处（卡片、按钮、排版、间距、颜色）
* 评估布局系统（根布局 vs 应用布局）是否正确实现
* 仅在概念层面提出改进建议（尚无代码）
* 对建议进行优先排序（高影响与低影响）
* 保持批判性但具有建设性，就像高级人员审查真实产品一样

输出格式：

1.总体评价（简要）
2. 文件夹结构回顾
3. UI/UX 审查
4.设计系统问题
5. 5 个最有影响力的改进

暂时不要生成代码。
只关注分析和建议。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。It asks an AI to assume the persona of a Senior Frontend Engineer & Product Reviewer to perform a high-level critique of a Next.js (App Router) project. Instead of writing code, the prompt focuses on evaluating the architecture (folder structure, scalability), UI/UX (hierarchy, consistency), and design system (component reuse) of a developer community platform to identify anti-patterns and suggest high-impact improvements.

### 适用人群
通用用户

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

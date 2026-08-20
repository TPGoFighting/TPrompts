# karpathy-guidelines

**Description:** Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.

**Type:** SKILL
**Author:** yazz4444
**Created:** 2026-04-14T04:37:45.110Z
**Votes:** 2
**Views:** 0

**Tags:** refactoring, Best Practices, LLM, guidelines, coding

## Prompt Content

```
---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
license: MIT
---

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" -> "Write tests for invalid inputs, then make them pass"
- "Fix the bug" -> "Write a test that reproduces it, then make it pass"
- "Refactor X" -> "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
\
Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.
```

**Source:** https://prompts.chat/prompts/cmny4rpjq0003jy08nopcvben_karpathy-guidelines

## 中文翻译

### 标题
karpathy-指南

### 提示词内容

```
---
名称：karpathy指南
描述：减少常见 LLM 编码错误的行为指南。在编写、审查或重构代码时使用，以避免过度复杂化，进行外科手术更改，提出假设并定义可验证的成功标准。
许可证：麻省理工学院
---

# 卡帕蒂指南

减少常见 LLM 编码错误的行为指南，源自 [Andrej Karpathy 对 LLM 编码陷阱的观察](https://x.com/karpathy/status/2015883857489522876)。

**权衡：** 这些指南偏重于谨慎而非速度。对于琐碎的任务，请运用判断力。

## 1. 编码前思考

**不要假设。不要隐藏困惑。表面权衡。**

实施前：
- 明确陈述你的假设。如果不确定，请询问。
- 如果存在多种解释，请提出它们 - 不要默默地选择。
- 如果存在更简单的方法，请说出来。在有必要的时候进行反击。
- 如果有什么不清楚，就停下来。说出令人困惑的地方。问。

## 2.简单第一

**解决问题的最少代码。没有什么推测性的。**

- 没有超出要求的功能。
- 没有一次性代码的抽象。
- 没有未要求的“灵活性”或“可配置性”。
- 对于不可能的情况没有错误处理。
- 如果你写了 200 行，而实际可能是 50 行，那就重写它。

问问自己：“高级工程师会说这过于复杂吗？”如果是，请简化。

## 3. 手术改变

**仅触摸您必须触摸的内容。只清理你自己的烂摊子。**

编辑现有代码时：
- 不要“改进”相邻的代码、注释或格式。
- 不要重构未损坏的东西。
- 匹配现有风格，即使您会采取不同的做法。
- 如果您发现不相关的死代码，请提及它 - 不要删除它。

当您的更改产生孤儿时：
- 删除您的更改未使用的导入/变量/函数。
- 除非有要求，否则不要删除预先存在的死代码。

测试：每条更改的行都应该直接跟踪到用户的请求。

## 4. 目标驱动执行

**定义成功标准。循环直到验证为止。**

将任务转化为可验证的目标：
-“添加验证”->“为无效输入编写测试，然后使它们通过”
-“修复错误”->“编写一个重现该错误的测试，然后使其通过”
-“重构X”->“确保测试前后通过”

对于多步骤任务，请陈述一个简要计划：
\
强大的成功标准让您可以独立循环。薄弱的标准（“使其发挥作用”）需要不断澄清。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.

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

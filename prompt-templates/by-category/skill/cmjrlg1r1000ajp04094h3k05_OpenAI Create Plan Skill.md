# OpenAI Create Plan Skill

**Description:** OpenAI's experimental skill Codex AI Coding Assistant. Source: https://github.com/openai/skills

**Type:** TEXT
**Author:** beratcmn
**Created:** 2025-12-29T20:11:21.950Z
**Votes:** 1
**Views:** 0

**Tags:** Skill, Planning

**Category:** Agent Skill

## Prompt Content

```
---
name: create-plan
description: Create a concise plan. Use when a user explicitly asks for a plan related to a coding task.
metadata:
  short-description: Create a plan
---

# Create Plan

## Goal

Turn a user prompt into a **single, actionable plan** delivered in the final assistant message.

## Minimal workflow

Throughout the entire workflow, operate in read-only mode. Do not write or update files.

1. **Scan context quickly**
   - Read `README.md` and any obvious docs (`docs/`, `CONTRIBUTING.md`, `ARCHITECTURE.md`).
   - Skim relevant files (the ones most likely touched).
   - Identify constraints (language, frameworks, CI/test commands, deployment shape).

2. **Ask follow-ups only if blocking**
   - Ask **at most 1–2 questions**.
   - Only ask if you cannot responsibly plan without the answer; prefer multiple-choice.
   - If unsure but not blocked, make a reasonable assumption and proceed.

3. **Create a plan using the template below**
   - Start with **1 short paragraph** describing the intent and approach.
   - Clearly call out what is **in scope** and what is **not in scope** in short.
   - Then provide a **small checklist** of action items (default 6–10 items).
      - Each checklist item should be a concrete action and, when helpful, mention files/commands.
      - **Make items atomic and ordered**: discovery → changes → tests → rollout.
      - **Verb-first**: “Add…”, “Refactor…”, “Verify…”, “Ship…”.
   - Include at least one item for **tests/validation** and one for **edge cases/risk** when applicable.
   - If there are unknowns, include a tiny **Open questions** section (max 3).

4. **Do not preface the plan with meta explanations; output only the plan as per template**

## Plan template (follow exactly)

```markdown
# Plan

<1–3 sentences: what we’re doing, why, and the high-level approach.>

## Scope
- In:
- Out:

## Action items
[ ] <Step 1>
[ ] <Step 2>
[ ] <Step 3>
[ ] <Step 4>
[ ] <Step 5>
[ ] <Step 6>

## Open questions
- <Question 1>
- <Question 2>
- <Question 3>
```

## Checklist item guidance
Good checklist items:
- Point to likely files/modules: src/..., app/..., services/...
- Name concrete validation: “Run npm test”, “Add unit tests for X”
- Include safe rollout when relevant: feature flag, migration plan, rollback note

Avoid:
- Vague steps (“handle backend”, “do auth”)
- Too many micro-steps
- Writing code snippets (keep the plan implementation-agnostic)
```

**Source:** https://prompts.chat/prompts/cmjrlg1r1000ajp04094h3k05_openai-create-plan-skill

## 中文翻译

### 标题
OpenAI 创建计划技能

### 提示词内容

```
---
名称：创建计划
描述：创建一个简洁的计划。当用户明确要求提供与编码任务相关的计划时使用。
元数据：
  简短描述：制定计划
---

# 创建计划

## 目标

将用户提示转变为最终助理消息中传递的**单一、可操作的计划**。

## 最小工作流程

在整个工作流程中，以只读模式操作。不要写入或更新文件。

1. **快速扫描上下文**
   - 阅读“README.md”和任何明显的文档（“docs/”、“CONTRIBUTING.md”、“ARCHITECTURE.md”）。
   - 浏览相关文件（最有可能接触的文件）。
   - 识别约束（语言、框架、CI/测试命令、部署形式）。

2. **仅在受阻时才询问后续行动**
   - 提出**最多 1-2 个问题**。
   - 仅在没有答案的情况下无法负责任地计划时才询问；更喜欢多项选择。
   - 如果不确定但未被阻止，请做出合理的假设并继续。

3. **使用下面的模板创建计划**
   - 从 **1 短段** 描述意图和方法开始。
   - 简而言之，清楚地指出什么是**在范围内**，什么是**不在范围内**。
   - 然后提供一份行动项目的**小清单**（默认 6-10 项）。
      - 每个清单项目都应该是一个具体的行动，如果有帮助，请提及文件/命令。
      - **使项目原子化和有序**：发现→更改→测试→推出。
      - **动词优先**：“添加...”、“重构...”、“验证...”、“发送...”。
   - 至少包括一项用于**测试/验证**的项目和一项用于**边缘情况/风险**的项目（如果适用）。
   - 如果存在未知问题，请添加一个很小的 ​​*开放问题** 部分（最多 3 个）。

4. **不要在计划前加上元解释；仅根据模板输出计划**

## 计划模板（严格遵循）
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。OpenAI's experimental skill Codex AI Coding Assistant. Source: https://github.com/openai/skills

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

# High-Stakes Decision Support System

**Description:** Major life and business decisions — changing careers, raising a round, ending a relationship, relocating — paralyze people not because they lack information but because the stakes are high enough that being wrong feels catastrophic. Structured analysis that forces clarity on trade-offs makes the decision-making process feel competent even when the outcome is uncertain.

**Type:** TEXT
**Author:** mmanisaligil
**Created:** 2026-03-19T19:17:36.577Z
**Votes:** 0
**Views:** 0

**Category:** Vibe Coding

## Prompt Content

```
Build a high-stakes decision support system called "Pivot" — a structured thinking tool for major life and business decisions.
This is distinct from a simple pros/cons list. The value is in the structured analytical process, not the output document.
Core features:
- Decision intake: user describes the decision (what they're choosing between), their constraints (time, money, relationships, obligations), their stated values (top 3), their current leaning, and their deadline
- Mandatory clarifying questions: [LLM API] generates 5 questions designed to surface hidden assumptions and unstated trade-offs in the user's specific decision. User must answer all 5 before proceeding. The quality of these questions is the quality of the product
- Six analytical frames (each run as a separate API call, shown in tabs):
  (1) Expected value — probability-weighted outcomes under each option  (2) Regret minimization — which option you're least likely to regret at age 80  (3) Values coherence — which option is most consistent with stated values, with specific evidence  (4) Reversibility index — how easily each option can be undone if it's wrong  (5) Second-order effects — what follows from each option in 6 months and 3 years  (6) Advice to a friend — if a trusted friend described this exact situation, what would you tell them?
- Devil's advocate brief: a separate analysis arguing as strongly as possible against the user's current leaning — shown after the 6 frames
- Decision record: stored with all analysis and the final decision made. User updates with actual outcome at 90 days and 1 year

Stack: React, [LLM API] with one carefully crafted prompt per analytical frame, localStorage. Focused, serious design — no gamification, no encouragement. This handles real decisions.

```

**Source:** https://prompts.chat/prompts/cmmxur2dd000hjs04zn6fdjqr_high-stakes-decision-support-system

## 中文翻译

### 标题
高风险决策支持系统

### 提示词内容

```
建立一个名为“Pivot”的高风险决策支持系统——一种用于重大生活和商业决策的结构化思维工具。
这与简单的优缺点列表不同。该值存在于结构化分析过程中，而不是输出文档中。
核心特点：
- 决策摄入：用户描述决策（他们正在选择什么）、他们的限制（时间、金钱、关系、义务）、他们规定的价值观（前 3 个）、他们当前的倾向和他们的截止日期
- 强制性澄清问题：[LLM API] 生成 5 个问题，旨在揭示用户具体决策中隐藏的假设和未说明的权衡。用户必须回答全部 5 个问题才能继续。这些问题的质量就是产品的质量
- 六个分析框架（每个分析框架作为单独的 API 调用运行，显示在选项卡中）：
  (1) 期望值 — 每个选项下的概率加权结果 (2) 遗憾最小化 — 哪个选项是您在 80 岁时最不可能后悔的选项 (3) 价值观一致性 — 哪个选项与规定的价值观最一致，并有具体证据 (4) 可逆性指数 — 每个选项错误时撤销的容易程度 (5) 二阶效应 — 每个选项在 6 个月和 3 年内会产生什么结果 (6) 给朋友的建议 — 如果值得信赖的朋友描述了这一点具体情况，你会告诉他们什么？
- 魔鬼代言人简介：单独的分析尽可能强烈地反对用户当前的倾向 - 在 6 帧之后显示
- 决策记录：存储所有分析和做出的最终决策。用户更新 90 天和 1 年的实际结果

Stack：React，[LLM API]，每个分析框架都有一个精心设计的提示，localStorage。专注、严肃的设计——没有游戏化，没有鼓励。这处理真正的决定。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Major life and business decisions — changing careers, raising a round, ending a relationship, relocating — paralyze people not because they lack information but because the stakes are high enough that being wrong feels catastrophic. Structured analysis that forces clarity on trade-offs makes the decision-making process feel competent even when the outcome is uncertain.

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

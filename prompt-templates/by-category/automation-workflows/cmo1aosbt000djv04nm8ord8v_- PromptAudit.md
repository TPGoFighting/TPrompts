# 🧠 PromptAudit

**Description:** PromptAudit is a production-grade framework for advanced prompt evaluation and optimization. It systematically analyzes clarity, consistency, missing constraints, contradictions, and output reliability. Its three-stage structure (Issues → Recommendations → Optimized Prompt) identifies problems and delivers actionable solutions, making prompts more predictable, stable, and production-ready.


**Type:** TEXT
**Author:** gunebak4n
**Created:** 2026-04-16T09:46:44.969Z
**Votes:** 0
**Views:** 0

**Tags:** Prompt Engineering, audit, optimization

**Category:** Automation & Workflows

## Prompt Content

```
Act as a senior prompt engineer performing a strict and practical quality audit of the prompt enclosed below.

---PROMPT START---
${paste_prompt_here}
---PROMPT END---

Evaluate the prompt for clarity, completeness, ambiguity, missing constraints, weak instructions, conflicting directions, context gaps, output-format weaknesses, and any other issue that could reduce output quality, reliability, consistency, or usability. Prioritize issues based on their combined impact on output quality and likelihood of failure. Focus primarily on issues that directly or predictably affect correctness, reliability, or usability, but include low-probability, high-impact edge cases if they may affect real-world performance. Limit analysis to high-value insights.

In the first section (Issues), identify the most significant problems and explain clearly why each one may cause failure, inconsistency, ambiguity, or suboptimal outputs. Present issues in strict priority order using numbered points. Be comprehensive in identifying issues, but limit explanations to what is necessary to understand their impact.

In the second section (Recommendations), provide specific, practical, and directly applicable improvements. Ensure each recommendation explicitly maps to a corresponding issue (e.g., Issue 1 → Recommendation 1). Do not introduce unrelated recommendations, unless they clearly resolve multiple identified issues.

In the third section (Optimized Prompt), rewrite the prompt in a production-ready form that preserves the original intent while improving clarity, control, precision, completeness, and reliability. The result should be optimized for consistent, unambiguous, format-compliant, and clearly testable outputs in repeated use. Include explicit success criteria only when they improve testability. You may restructure the prompt if necessary, but do not introduce new intent. If essential elements are missing (such as context, constraints, or output format), explicitly account for them using clear placeholders such as ${insert_context_here}. Only make assumptions when required to make the prompt executable; otherwise explicitly identify missing information.

Structure the response using exactly these three section titles: Issues, Recommendations, and Optimized Prompt.

Use English only for the three required section titles. Write everything else in Turkish. Strictly enforce numbering and clear mapping between sections. Avoid unnecessary repetition.

```

**Source:** https://prompts.chat/prompts/cmo1aosbt000djv04nm8ord8v_promptaudit



---

## 中文翻译

### 标题
🧠 即时审计

### 提示词内容

```
充当高级提示工程师，对下面所附的提示进行严格且实用的质量审核。

---立即开始---
${paste_prompt_here}
---提示结束---

评估提示的清晰度、完整性、模糊性、缺少约束、指令薄弱、方向冲突、上下文差距、输出格式弱点以及任何其他可能降低输出质量、可靠性、一致性或可用性的问题。根据问题对输出质量和失败可能性的综合影响来确定问题的优先级。主要关注直接或可预测影响正确性、可靠性或可用性的问题，但也包括可能影响实际性能的低概率、高影响的边缘情况。将分析限制为高价值见解。

在第一部分（问题）中，确定最重要的问题，并清楚地解释为什么每个问题可能会导致失败、不一致、模糊或输出不理想。使用编号点按严格的优先顺序提出问题。在识别问题时要全面，但解释仅限于了解其影响所需的内容。

在第二部分（建议）中，提供具体的、实用的、直接适用的改进措施。确保每项建议明确映射到相应的问题（例如，问题 1 → 建议 1）。不要引入不相关的建议，除非它们明确解决了多个已确定的问题。

在第三部分（优化提示）中，以可投入生产的形式重写提示，保留原始意图，同时提高清晰度、控制力、精确度、完整性和可靠性。结果应进行优化，以便在重复使用时获得一致、明确、格式兼容且清晰可测试的输出。仅在提高可测试性时才包含明确的成功标准。如有必要，您可以重组提示，但不要引入新的意图。如果缺少基本元素（例如上下文、约束或输出格式），请使用清晰的占位符（例如 ${insert_context_here}）明确说明它们。仅在需要使提示可执行时才做出假设；否则明确识别缺失的信息。

准确使用以下三个部分标题来构建响应：问题、建议和优化提示。

仅对三个必需的部分标题使用英文。用土耳其语写下其他所有内容。严格执行编号并明确各部分之间的映射。避免不必要的重复。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。PromptAudit is a production-grade framework for advanced prompt evaluation and optimization. It systematically analyzes clarity, consistency, missing constraints, contradictions, and output reliability. Its three-stage structure (Issues → Recommendations → Optimized Prompt) identifies problems and delivers actionable solutions, making prompts more predictable, stable, and production-ready.

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
- `${paste_prompt_here}`: 需要您填写
- `${insert_context_here}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

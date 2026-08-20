# Academic analyst and exam pattern extractor

**Description:** This prompt is designed to analyze a combined question paper PDF (CT + Final exams) and automatically organize all questions into a structured, syllabus-aligned classification.

**Type:** TEXT
**Author:** helix-77
**Created:** 2026-03-29T20:27:02.338Z
**Votes:** 1
**Views:** 0

**Tags:** Academic

**Category:** Exam Preparation

## Prompt Content

```
ROLE: Act as an expert academic analyst and exam pattern extractor.

GOAL:
Given a question paper PDF (containing class test and final exam questions), classify ALL questions into a structured format for study and pattern recognition.

OUTPUT FORMAT (STRICT — MUST FOLLOW EXACTLY):

Classification of Questions by Chapter and Type

Chapter X: [Chapter Name]

X.1 Definition & Conceptual Questions

[Year/Exam].[Question No]: [Full question text]

[Year/Exam].[Question No]: [Full question text]

X.2 Mathematical/Analytical Questions

[Year/Exam].[Question No]: [Full question text]

...

X.3 Algorithm / Procedural Questions

...

X.4 Programming / Implementation Questions

...

X.5 Comparison / Justification Questions

...

--------------------------------------------------

INSTRUCTIONS:

1. FIRST, identify chapters based on syllabus-level grouping (Syllabus can be found in the pdf).
2. THEN group questions under appropriate chapters.
3. WITHIN each chapter, classify into types:
   - Definition & Conceptual
   - Mathematical / Numerical
   - Algorithm / Step-based
   - Programming / Code
   - Comparison / Justification

4. PRESERVE original wording of each question. (Paraphrase to shorten without losing context)
5. INCLUDE exact reference in this format:
   - class test (CT) 2023 Q1
   - Final 2023 Q2(a)

6. DO NOT skip any question.
7. Merge questions only if they are extremely same and add a number tag of how many of that ques was merged — else keep each separately listed.
8. DO NOT explain anything — ONLY classification output.
9. Maintain clean spacing and readability.

10. If a question has multiple subparts (a, b, c), list them separately:
   Example:
   2023 Q2(a): ...
   2023 Q2(b): ...

11. If chapter is unclear, infer based on topic intelligently.

12. Prioritize accuracy over speed.

13. Add frequency tags like [Repeated X times], [High Frequency]

14. If the document is noisy or contains formatting issues, carefully reconstruct questions before classification.
```

**Source:** https://prompts.chat/prompts/cmnc7mvd00001k004hrf70exi_academic-analyst-and-exam-pattern-extractor

## 中文翻译

### 标题
学术分析师和考试模式提取器

### 提示词内容

```
角色：担任专家学术分析师和考试模式提取者。

目标：
给定一份试卷 PDF（包含课堂测试和期末考试问题），将所有问题分类为结构化格式，以供学习和模式识别。

输出格式（严格 — 必须完全遵循）：

按章节和类型对问题进行分类

第十章：[章节名称]

X.1 定义和概念问题

[年份/考试].[问题编号]：[完整问题文本]

[年份/考试].[问题编号]：[完整问题文本]

X.2 数学/分析问题

[年份/考试].[问题编号]：[完整问题文本]

...

X.3 算法/程序问题

...

X.4 编程/实现问题

...

X.5 比较/论证问题

...

--------------------------------------------------

说明：

1. 首先，根据教学大纲级别分组确定章节（教学大纲可以在 pdf 中找到）。
2. 然后将问题分组到适当的章节下。
3. 在每一章中，分为以下类型：
   - 定义和概念
   - 数学/数值
   - 基于算法/步骤
   - 编程/代码
   - 比较/论证

4. 保留每个问题的原始措辞。 （在不失去上下文的情况下缩短释义）
5. 采用以下格式包含准确的参考文献：
   - 班级测试（CT）2023年第一季度
   - 2023 年第二季度最终结果(a)

6. 不要跳过任何问题。
7. 仅当问题极其相同时才合并问题，并添加一个数字标签来表明合并了多少个问题 - 否则将每个问题单独列出。
8. 不要解释任何东西——仅解释分类输出。
9. 保持清晰的间距和可读性。

10. 如果一个问题有多个子部分（a、b、c），请分别列出：
   示例：
   2023 年第二季度(a)：...
   2023 年第二季度(b)：...

11. 如果章节不清楚，可以根据主题进行智能推断。

12. 优先考虑准确性而不是速度。

13.添加频率标签，如[重复X次]、[高频]

14. 如果文档有噪音或包含格式问题，请在分类之前仔细重构问题。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt is designed to analyze a combined question paper PDF (CT + Final exams) and automatically organize all questions into a structured, syllabus-aligned classification.

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

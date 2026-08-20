# Chat Summary and Export Instructions

**Description:** This prompt guides you to summarize and export key information, instructions, and contextual details from a chat. It organizes the content into structured categories with dates, ensuring all relevant information is captured for easy sharing and review.

**Type:** TEXT
**Author:** turhancan97
**Created:** 2026-06-25T06:08:05.372Z
**Votes:** 0
**Views:** 0

**Category:** Meeting & Collaboration

## Prompt Content

```
Summarize and export all important points, instructions, and contextual information exchanged in this chat, structured per your requirements.

- Use section headers for each major category (e.g., Task Instructions, Preferences, System Guidelines, etc.).
- For each entry within a category, list one entry per line, formatted as: [YYYY-MM-DD] - Entry content here.
- Sort entries by oldest date first within each category.
- If no date is known for an entry, use [unknown] instead of a date.
- When preserving user content, use the original wording verbatim where possible, particularly for direct instructions, requirements, or preferences.
- Wrap the entire export in a single code block (backticks, language unspecified) for easy copying.
- After the code block, clearly state whether this is the complete set or if more entries remain.

Persist in checking all prior conversation turns to ensure all relevant context is captured exhaustively. Think step-by-step to avoid missing any category or detail.

## Output Format:
- The export must be wrapped in a single code block.
- Use markdown section headers within the code block for each category.
- Each entry in a category must be a single line, formatted as: [YYYY-MM-DD] - Entry content here.
- If needed, use [unknown] if the date for an entry cannot be determined.
- After the code block, add a plain text statement: "This is the complete set." or "More entries remain." (as appropriate).

## Example

```
# Task Instructions
[2024-06-13] - I will move this chant to another AI agent to also support my projects. I want you to prepare detailed list of important points which were discussed in this chat. Please preapare.

# Format Specifications
[2024-06-13] - Use section headers for each category. Within each category, list one entry per line, sorted by oldest date first. Format each line as: [YYYY-MM-DD] - Entry content here.
[2024-06-13] - If no date is known, use [unknown] instead.

# Output Instructions
[2024-06-13] - Wrap the entire export in a single code block for easy copying.
[2024-06-13] - After the code block, state whether this is the complete set or if more remain.
```

(Real exports may be longer and contain more categories/entries as appropriate.)

---

**Reminder:** Carefully review all prior turns to ensure nothing is missed, using verbatim wording for user requirements and instructions. Produce the export exactly as described above, including the final completeness statement.
```

**Source:** https://prompts.chat/prompts/cmqt3p7uk0001jv04ucl71c5o_chat-summary-and-export-instructions

## 中文翻译

### 标题
聊天摘要和导出说明

### 提示词内容

```
总结并导出在此聊天中交换的所有要点、说明和上下文信息，并根据您的要求进行结构化。

- 使用每个主要类别的节标题（例如，任务说明、首选项、系统指南等）。
- 对于类别中的每个条目，每行列出一个条目，格式为：[YYYY-MM-DD] - 此处的条目内容。
- 在每个类别中首先按最早的日期对条目进行排序。
- 如果条目的日期未知，请使用 [unknown] 而不是日期。
- 保留用户内容时，尽可能逐字使用原始措辞，特别是直接指示、要求或偏好。
- 将整个导出包装在单个代码块中（反引号，未指定语言）以便于复制。
- 在代码块之后，清楚地说明这是否是完整的集合，或者是否还剩下更多条目。

坚持检查所有先前的对话，以确保详尽捕获所有相关上下文。逐步思考以避免遗漏任何类别或细节。

## 输出格式：
- 导出必须包装在单个代码块中。
- 在每个类别的代码块中使用 Markdown 节标题。
- 类别中的每个条目必须是单行，格式为：[YYYY-MM-DD] - 此处的条目内容。
- 如果需要，如果无法确定条目的日期，请使用[未知]。
- 在代码块之后，添加纯文本语句：“这是完整的集合。”或“还有更多条目。” （视情况而定）。

＃＃ 例子
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt guides you to summarize and export key information, instructions, and contextual details from a chat. It organizes the content into structured categories with dates, ensuring all relevant information is captured for easy sharing and review.

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

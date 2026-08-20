# Language Detection

**Description:** This (part of a) prompt guides the AI to detect the language of a conversation using some standard methods
Several versions are given for reference.
- using user's metadata if available, fallback to user's first response
- using standard language detection method used by LLM system prompt

**Type:** TEXT
**Author:** s-celles
**Created:** 2025-12-28T08:52:18.394Z
**Votes:** 0
**Views:** 0

**Tags:** Languages

## Prompt Content

```
**Important - Language Detection:** 

- **Primary method:** If location metadata is available (e.g., user locale, browser language, or system language settings), use it to determine the conversation language from the start.

- **Fallback method:** If no metadata is available, detect the language of my first response and continue the entire conversation in that language.
```

**Source:** https://prompts.chat/prompts/cmjphqx5m0001l5044ryxxnyj_language-detection

## 中文翻译

### 标题
语言检测

### 提示词内容

```
**重要 - 语言检测：** 

- **主要方法：** 如果位置元数据可用（例如，用户区域设置、浏览器语言或系统语言设置），请使用它从一开始就确定对话语言。

- **后备方法：** 如果没有可用的元数据，请检测我的第一个响应的语言并以该语言继续整个对话。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**数据分析与可视化**类的提示词。This (part of a) prompt guides the AI to detect the language of a conversation using some standard methods

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

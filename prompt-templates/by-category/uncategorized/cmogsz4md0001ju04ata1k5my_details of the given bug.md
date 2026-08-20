# details of the given bug

**Type:** TEXT
**Author:** dishantpatel624
**Created:** 2026-04-27T06:15:13.189Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
Act as a senior software analyst.

## Goal
From the given input text, extract and structure the following three elements:

1. describ_feature → What feature or system is being discussed
2. what_should_happen → Expected behavior
3. what_is_happen → Actual behavior / issue

---

## Input
${paste_any_raw_text_here}
- Could be messy
- Could include logs, chat, code comments, or mixed explanations

---

## Instructions

- Read the entire input carefully
- Infer missing context when reasonably possible
- Do NOT hallucinate unclear details
- If something is missing, return "UNCLEAR"

---

## Extraction Rules

### 1. describ_feature
- Summarize the feature/system in 1–2 lines
- Focus on purpose, not implementation details

### 2. what_should_happen
- Describe ideal/expected behavior
- Include conditions if mentioned

### 3. what_is_happen
- Describe actual issue or incorrect behavior
- Be precise and factual
- Include errors, unexpected results, or failures

---

## Output Format (STRICT)

## Output Format (STRICT)

Return ONLY this points: "describ_feature": "...",


 "what_should_happen": "...",


 "what_is_happen": "..."

---

## Constraints
- No extra text 
- No explanations
- No assumptions beyond reasonable inference
- Keep each field concise but complete
```

**Source:** https://prompts.chat/prompts/cmogsz4md0001ju04ata1k5my_details-of-the-given-bug

## 中文翻译

### 标题
给定错误的详细信息

### 提示词内容

```
担任高级软件分析师。

## 目标
从给定的输入文本中，提取并构造以下三个元素：

1.describ_feature → 正在讨论什么功能或系统
2. What_should_happen → 预期行为
3.发生了什么→实际行为/问题

---

## 输入
${此处粘贴_any_raw_text_}
- 可能会很乱
- 可以包括日志、聊天、代码注释或混合解释

---

## 说明

- 仔细阅读整个输入
- 在合理可能的情况下推断缺失的上下文
- 不要对不清楚的细节产生幻觉
- 如果缺少某些内容，请返回“UNCLEAR”

---

## 提取规则

### 1. 描述特征
- 用 1-2 行总结功能/系统
- 关注目的，而不是实施细节

### 2.应该发生什么
- 描述理想/预期的行为
- 如果提到的话，请包括条件

### 3.发生了什么
- 描述实际问题或不正确的行为
- 准确、真实
- 包括错误、意外结果或失败

---

## 输出格式（严格）

## 输出格式（严格）

仅返回这一点：“describ_feature”：“...”，


 "what_should_happen": "...",


 “发生了什么”：“……”

---

## 约束条件
- 没有额外的文字 
- 没有解释
- 没有超出合理推论的假设
- 保持每个字段简洁但完整
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与details of the given bug相关的任务。

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
- `${paste_any_raw_text_here}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

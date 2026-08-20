# AI Grounding Prompt

**Description:** A basic prompt outline to ground an AI when searching for information. Initially designed to ensure accuracy in searching uploaded documents, it can be modified slightly for other workflows where data accuracy is required.  The prompt grounds an AI and help prevent hallucinations.

**Type:** TEXT
**Author:** roshinau
**Created:** 2026-02-25T22:29:39.798Z
**Votes:** 0
**Views:** 0

**Category:** Agent Workflows

## Prompt Content

```
1. Base your answer ONLY on the uploaded documents. Nothing else.
2. If info isn't found, say "Not found." Don't guess.
3. For each claim, cite: [Document, Page/Section, Quote]
4. If uncertain, mark as [Unverified]
5. [Your question]

Re-scan the document. For each claim, give me the exact quote that supports it,  If you can't find a quote, take the claim back.
```

**Source:** https://prompts.chat/prompts/cmm2lxb2u0001l2047r4ztp0f_ai-grounding-prompt



---

## 中文翻译

### 标题
AI接地提示

### 提示词内容

```
1. 仅根据上传的文件做出回答。没有别的了。
2. 如果未找到信息，请说“未找到”。别猜了。
3. 对于每项声明，请引用：[文档、页/节、引用]
4. 如果不确定，请标记为[未验证]
5.【你的问题】

重新扫描文档。对于每项索赔，请给我支持它的确切报价，如果您找不到报价，请收回索赔。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**AI辅助任务**类的提示词。A basic prompt outline to ground an AI when searching for information. Initially designed to ensure accuracy in searching uploaded documents, it can be modified slightly for other workflows where data accuracy is required.  The prompt grounds an AI and help prevent hallucinations.

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

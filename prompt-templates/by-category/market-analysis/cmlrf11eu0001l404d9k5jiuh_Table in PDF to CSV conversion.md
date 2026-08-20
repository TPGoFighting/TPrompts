# Table in PDF to CSV conversion

**Description:** For table data and information extraction from PDF

**Type:** TEXT
**Author:** bornduck
**Created:** 2026-02-18T02:31:08.646Z
**Votes:** 0
**Views:** 0

**Category:** Market Analysis

## Prompt Content

```
"Attached is an image of a table listing the model parameters for the ${insert_model_name} model (from [Insert Author/Paper Name]).
Please extract the data and convert it into a CSV code block that I can copy and save directly.
Requirements:
Use the first row as the header.
If cells are merged, repeat the value for each row to ensure the CSV is flat and processable.
Do not include units in the numeric columns (e.g., remove 'ms' or '%'), or keep them consistent in a separate column.
If any text is unclear due to image quality, mark it as '${unclear}' rather than guessing.
Ensure all fields containing commas are properly quoted."

```

**Source:** https://prompts.chat/prompts/cmlrf11eu0001l404d9k5jiuh_table-in-pdf-to-csv-conversion

## 中文翻译

### 标题
PDF 到 CSV 中的表格转换

### 提示词内容

```
“随附的表格图像列出了 ${insert_model_name} 模型的模型参数（来自 [插入作者/论文名称]）。
请提取数据并将其转换为 CSV 代码块，我可以直接复制并保存。
要求：
使用第一行作为标题。
如果合并单元格，请重复每行的值，以确保 CSV 平坦且可处理。
不要在数字列中包含单位（例如，删除“ms”或“%”），或在单独的列中保持它们一致。
如果任何文本由于图像质量而不清楚，请将其标记为“${unclear}”而不是猜测。
确保所有包含逗号的字段都被正确引用。”
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。For table data and information extraction from PDF

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
- `${insert_model_name}`: 需要您填写
- `${unclear}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

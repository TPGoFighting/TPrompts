# Node Web App for Czech Invoice PDF Generation

**Description:** Develop a Node.js web application to generate Czech invoices in PDF format using node-isdoc-pdf and calculate provisions based on order XML data.

**Type:** TEXT
**Author:** ddann
**Created:** 2025-12-30T05:15:27.814Z
**Votes:** 0
**Views:** 0

**Tags:** Node.js, Web Development, Finance

**Category:** Web Development

## Prompt Content

```
Act as a Full Stack Developer. You are tasked with creating a Node.js web application to generate Czech invoices in PDF format. You will: 
- Utilize the GitHub repository https://github.com/deltazero-cz/node-isdoc-pdf.git for PDF generation.
- Fetch XML data containing orders to calculate provisions.
- Implement a baseline provision rate of 7% from the price of the order without VAT.
- Prepare the app to accommodate additional rules for determining provision percentages.
- Generate a PDF of a CSV table containing order details.
- Create a second PDF for an invoice using node-isdoc-pdf.
Rules:
- Maintain code modularity for scalability.
- Ensure the application can be extended with new provision rules.
- Include error handling for XML data parsing and PDF generation.
Variables:
- ${xmlData} - XML data with order details
- ${provisionRules} - Additional provision rules to apply
- ${outputPath} - Directory for saving generated PDFs
```

**Source:** https://prompts.chat/prompts/cmjs4vrgm0001ju04om3vv6k2_node-web-app-for-czech-invoice-pdf-generation

## 中文翻译

### 标题
用于生成捷克发票 PDF 的 Node Web 应用程序

### 提示词内容

```
充当全栈开发人员。您的任务是创建一个 Node.js Web 应用程序来生成 PDF 格式的捷克发票。您将： 
- 利用 GitHub 存储库 https://github.com/deltazero-cz/node-isdoc-pdf.git 生成 PDF。
- 获取包含订单的 XML 数据以计算规定。
- 执行不含增值税订单价格 7% 的基准拨备率。
- 准备应用程序以适应确定供应百分比的附加规则。
- 生成包含订单详细信息的 CSV 表的 PDF。
- 使用node-isdoc-pdf 为发票创建第二个PDF。
规则：
- 保持代码模块化以实现可扩展性。
- 确保应用程序可以通过新的规定规则进行扩展。
- 包括 XML 数据解析和 PDF 生成的错误处理。
变量：
- ${xmlData} - 包含订单详细信息的 XML 数据
- ${provisionRules} - 要应用的附加规定规则
- ${outputPath} - 保存生成的 PDF 的目录
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Develop a Node.js web application to generate Czech invoices in PDF format using node-isdoc-pdf and calculate provisions based on order XML data.

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
- `${xmlData}`: 需要您填写
- `${provisionRules}`: 需要您填写
- `${outputPath}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

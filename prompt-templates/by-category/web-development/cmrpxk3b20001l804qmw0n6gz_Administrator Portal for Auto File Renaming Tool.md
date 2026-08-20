# Administrator Portal for Auto File Renaming Tool

**Description:** Develop a secure and responsive Administrator Portal using Google Apps Script to manage an Auto File Renaming Tool. The portal should process bulk document uploads and rename files based on employee information.

**Type:** TEXT
**Author:** ramsham355
**Created:** 2026-07-18T05:32:32.319Z
**Votes:** 0
**Views:** 0

**Tags:** Web Development, dashboard, Automation

**Category:** Web Development

## Prompt Content

```
Act as a web developer tasked with creating a modern Administrator Portal for an Auto File Renaming Tool. Your task is to develop a secure, responsive web-based interface using Google Apps Script, HTML, CSS, and JavaScript.

Your responsibilities include:
- Implementing secure administrator login with session management and automatic timeout.
- Creating a dashboard to display metrics such as total CSV records uploaded, total files uploaded, successfully renamed files, unmatched files, duplicate matches, processing status, download history, and recent activity.
- Designing a file renaming system that matches employee information from CSV files using any two fields (Employee ID, First Name, Middle Name, or Surname).
- Allowing administrators to define a renaming template.
- Generating a ZIP archive of successfully renamed files with a naming convention: `SalarySlips_Renamed_${month}_${year}.zip`.
- Producing a processing report with detailed statistics and errors, exportable in Excel and CSV formats.

Rules and Constraints:
- Ensure all uploaded files (PDF and JPG) are renamed according to the template.
- Handle errors by logging and including failed/skipped files in the report.
- Maintain a clean and professional user interface.
- Provide options to download ZIP and processing reports after completion.

You will use variables such as `${month}` and `${year}` in file naming for flexibility.
```

**Source:** https://prompts.chat/prompts/cmrpxk3b20001l804qmw0n6gz_administrator-portal-for-auto-file-renaming-tool

## 中文翻译

### 标题
自动文件重命名工具的管理员门户

### 提示词内容

```
担任 Web 开发人员，负责为自动文件重命名工具创建现代管理员门户。您的任务是使用 Google Apps 脚本、HTML、CSS 和 JavaScript 开发安全、响应灵敏的基于网络的界面。

您的职责包括：
- 通过会话管理和自动超时实现安全管理员登录。
- 创建仪表板来显示指标，例如上传的 CSV 记录总数、上传的文件总数、成功重命名的文件、不匹配的文件、重复匹配、处理状态、下载历史记录和最近的活动。
- 设计一个文件重命名系统，使用任意两个字段（员工 ID、名字、中间名或姓氏）来匹配 CSV 文件中的员工信息。
- 允许管理员定义重命名模板。
- 使用命名约定生成成功重命名的文件的 ZIP 存档：`SalarySlips_Renamed_${month}_${year}.zip`。
- 生成包含详细统计数据和错误的处理报告，可导出为 Excel 和 CSV 格式。

规则和限制：
- 确保所有上传的文件（PDF 和 JPG）根据模板重命名。
- 通过记录并在报告中包含失败/跳过的文件来处理错误。
- 保持干净和专业的用户界面。
- 提供下载 ZIP 和完成后处理报告的选项。

为了灵活性，您将在文件命名中使用“${month}”和“${year}”等变量。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Develop a secure and responsive Administrator Portal using Google Apps Script to manage an Auto File Renaming Tool. The portal should process bulk document uploads and rename files based on employee information.

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
- `${month}`: 需要您填写
- `${year}`: 需要您填写
- `${month}`: 需要您填写
- `${year}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

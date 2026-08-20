# Note Guru

**Description:** analyze loads of messy files with random notes in them and create new files with the same notes only organized into beautiful easy to find and access topic sorted documents 

**Type:** TEXT
**Author:** sigmasauer07
**Created:** 2026-01-26T23:48:32.465Z
**Votes:** 0
**Views:** 0

**Tags:** Note Taking, Organization, Efficiency, Data Analysis, Content Creation

**Category:** Note Taking

## Prompt Content

```
Analyze all files in the folder named '${main_folder}` located at `${path_to_folder}`/ and perform the following tasks:

## Task 1: Extract Sensitive Data
Review every file thoroughly and identify all sensitive information including API keys, passwords, tokens, credentials, private keys, secrets, connection strings, and any other confidential data. Create a new file called `secrets.md` containing all discovered sensitive information with clear references to their source files.

## Task 2: Organize by Topic
After completing the secrets extraction, analyze the content of each file again. Many files contain multiple unrelated notes written at different times. Your job is to:

1. Identify the '${topic_max}' most prominent topics across all files based on content frequency and importance
2. Create '${topic_max}' new markdown files, one for each topic, named `${topic:#}.md` where you choose descriptive topic names
3. For each note segment in the original files:
   - Copy it to the appropriate topic file
   - Add a reference number in the original file next to that note (e.g., `${topic:2}` or `→ Security:2`)
   - This reference helps verify the migration later

## Task 3: Archive Original Files
Once all notes from an original file have been copied to their respective topic files and reference numbers added, move that original file into a new folder called `${archive_folder:old}`.

## Expected Final Structure
```
${main_folder}/
├── secrets.md (1 file)
├── ${topic:1}.md (topic files total)
├── ${topic:2}.md
├── ..... (more topic files)
├── ${topic:#}.md
└── ${archive_folder:old}/
      └── (all original files)
```

## Important Guidelines
- Be thorough in your analysis—read every file completely
- Maintain the original content when copying to topic files
- Choose topic names that accurately reflect the content clusters you find
- Ensure every note segment gets categorized
- Keep reference numbers clear and consistent
- Only move files to the archive folder after confirming all content has been properly migrated

Begin with `${path_to_folder}` and let me know when you need clarification on any ambiguous content during the organization process.

```

**Source:** https://prompts.chat/prompts/cmkvtj6tt0008kz04x1yv6d7h_note-guru

## 中文翻译

### 标题
笔记大师

### 提示词内容

```
分析位于“${path_to_folder}”/ 的名为“${main_folder}”的文件夹中的所有文件并执行以下任务：

## 任务 1：提取敏感数据
彻底审查每个文件并识别所有敏感信息，包括 API 密钥、密码、令牌、凭据、私钥、秘密、连接字符串和任何其他机密数据。创建一个名为“secrets.md”的新文件，其中包含所有发现的敏感信息以及对其源文件的明确引用。

## 任务 2：按主题组织
完成秘密提取后，再次分析每个文件的内容。许多文件包含在不同时间编写的多个不相关的注释。你的工作是：

1. 根据内容频率和重要性识别所有文件中“${topic_max}”最突出的主题
2. 创建“${topic_max}”新 Markdown 文件，每个主题一个，命名为“${topic:#}.md”，您可以在其中选择描述性主题名称
3. 对于原始文件中的每个音符片段：
   - 将其复制到相应的主题文件中
   - 在原始文件中该注释旁边添加参考号（例如“${topic:2}”或“→ Security:2”）
   - 此参考有助于稍后验证迁移

## 任务 3：存档原始文件
将原始文件中的所有注释复制到各自的主题文件并添加参考号后，将该原始文件移动到名为“${archive_folder:old}”的新文件夹中。

## 预期的最终结构
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。analyze loads of messy files with random notes in them and create new files with the same notes only organized into beautiful easy to find and access topic sorted documents

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
- `${main_folder}`: 需要您填写
- `${path_to_folder}`: 需要您填写
- `${topic_max}`: 需要您填写
- `${topic_max}`: 需要您填写
- `${topic}`: 可自定义（默认值: #）
- `${topic}`: 可自定义（默认值: 2）
- `${archive_folder}`: 可自定义（默认值: old）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

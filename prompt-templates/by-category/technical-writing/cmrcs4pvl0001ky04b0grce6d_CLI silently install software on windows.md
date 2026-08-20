# CLI silently install software on windows

**Description:** This prompt guides an IT technician through creating PowerShell commands to silently install or update software on Windows 10/11 systems using tools like Winget, Chocolatey, or GitHub. It outlines a decision workflow to determine the best installation method based on software availability.

**Type:** TEXT
**Author:** sxlderek
**Created:** 2026-07-09T00:39:36.706Z
**Votes:** 0
**Views:** 0

**Category:** Technical Writing

## Prompt Content

```
Ask me for the name of the software as your next question. 

- You are an IT expert technican. I want you to research, verify and then write powershell commands to silently install or update the software on a Windows 10/11 x86_64 computer.
Workflow:
- If the software is officially available on winget. use winget to install it.
- Elseif the software is available on chocolatey, use chocolatey to install it. 
- Elseif the software is from github. I prefer using dra (https://github.com/devmatteini/dra) to download and install the software.
- Elseif the software is not silently installable, download the software to user's default download folder first and then guide user how to install it and print a url link to the official installation guide.
- Assume winget, chocolatey and dra were already available and on user's computer.
- Always download the software to user's default Download folder. (check registry to find the correct path).
- output the commands in a code box.

```

**Source:** https://prompts.chat/prompts/cmrcs4pvl0001ky04b0grce6d_cli-silently-install-software-on-windows

## 中文翻译

### 标题
CLI 在 Windows 上静默安装软件

### 提示词内容

```
下一个问题请向我询问该软件的名称。 

- 您是一名 IT 专家技术人员。我希望您研究、验证然后编写 powershell 命令，以在 Windows 10/11 x86_64 计算机上静默安装或更新软件。
工作流程：
- 如果该软件在 winget 上正式可用。使用winget来安装它。
- 否则，如果该软件在 Chocolatey 上可用，请使用 Chocolatey 来安装它。 
- Elseif 该软件来自 github。我更喜欢使用 dra (https://github.com/devmatteini/dra) 下载并安装软件。
- 否则，如果该软件无法静默安装，请先将该软件下载到用户的默认下载文件夹，然后指导用户如何安装它并打印官方安装指南的 url 链接。
- 假设 winget、chocolatey 和 dra 已经可用并且位于用户的计算机上。
- 始终将软件下载到用户的默认下载文件夹。 （检查注册表以找到正确的路径）。
- 在代码框中输出命令。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt guides an IT technician through creating PowerShell commands to silently install or update software on Windows 10/11 systems using tools like Winget, Chocolatey, or GitHub. It outlines a decision workflow to determine the best installation method based on software availability.

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

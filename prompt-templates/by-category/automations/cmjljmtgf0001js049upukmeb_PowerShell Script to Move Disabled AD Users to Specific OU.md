# PowerShell Script to Move Disabled AD Users to Specific OU

**Description:** This prompt provides a PowerShell script to identify disabled user accounts in Active Directory and move them to a specified Organizational Unit (OU).

**Type:** TEXT
**Author:** darkvalerikspb
**Created:** 2025-12-25T14:34:01.504Z
**Votes:** 0
**Views:** 0

**Tags:** Automation

**Category:** Automations

## Prompt Content

```
Act as a System Administrator. You are tasked with managing user accounts in Active Directory (AD). Your task is to create a PowerShell script that:

- Identifies all disabled user accounts in the AD.
- Moves these accounts to a designated Organizational Unit (OU) specified by the variable ${targetOU}.

Rules:
- Ensure that the script is efficient and handles errors gracefully.
- Include comments in the script to explain each section.

Example PowerShell Script:
```
# Define the target OU
$targetOU = "OU=DisabledUsers,DC=yourdomain,DC=com"

# Get all disabled user accounts
$disabledUsers = Get-ADUser -Filter {Enabled -eq $false}

# Move each disabled user to the target OU
foreach ($user in $disabledUsers) {
    try {
        Move-ADObject -Identity $user.DistinguishedName -TargetPath $targetOU
        Write-Host "Moved: $($user.SamAccountName) to $targetOU"
    } catch {
        Write-Host "Failed to move $($user.SamAccountName): $_"
    }
}
```
Variables:
- ${targetOU} - The distinguished name of the target Organizational Unit where disabled users will be moved.
```

**Source:** https://prompts.chat/prompts/cmjljmtgf0001js049upukmeb_powershell-script-to-move-disabled-ad-users-to-specific-ou



---

## 中文翻译

### 标题
将禁用的 AD 用户移动到特定 OU 的 PowerShell 脚本

### 提示词内容

```
担任系统管理员。您的任务是管理 Active Directory (AD) 中的用户帐户。您的任务是创建一个 PowerShell 脚本：

- 识别 AD 中所有禁用的用户帐户。
- 将这些帐户移动到由变量 ${targetOU} 指定的指定组织单位 (OU)。

规则：
- 确保脚本高效并妥善处理错误。
- 在脚本中包含注释以解释每个部分。

PowerShell 脚本示例：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。This prompt provides a PowerShell script to identify disabled user accounts in Active Directory and move them to a specified Organizational Unit (OU).

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
- `${targetOU}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

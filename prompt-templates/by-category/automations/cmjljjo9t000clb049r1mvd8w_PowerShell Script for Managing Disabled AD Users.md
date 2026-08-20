# PowerShell Script for Managing Disabled AD Users

**Description:** This prompt provides a PowerShell script to identify all disabled user accounts in Active Directory and move them to a specified Organizational Unit (OU).

**Type:** TEXT
**Author:** darkvalerikspb
**Created:** 2025-12-25T14:31:34.817Z
**Votes:** 0
**Views:** 0

**Tags:** Automation

**Category:** Automations

## Prompt Content

```
Act as a System Administrator. You are managing Active Directory (AD) users. Your task is to create a PowerShell script that identifies all disabled user accounts and moves them to a designated Organizational Unit (OU).

You will:
- Use PowerShell to query AD for disabled user accounts.
- Move these accounts to a specified OU.

Rules:
- Ensure that the script has error handling for non-existing OUs or permission issues.
- Log actions performed for auditing purposes.

Example:
```powershell
# Import the Active Directory module
Import-Module ActiveDirectory

# Define the target OU
$TargetOU = "OU=DisabledUsers,DC=example,DC=com"

# Find all disabled user accounts
$DisabledUsers = Get-ADUser -Filter {Enabled -eq $false}

# Move each disabled user to the target OU
foreach ($User in $DisabledUsers) {
    try {
        Move-ADObject -Identity $User.DistinguishedName -TargetPath $TargetOU
        Write-Host "Moved $($User.SamAccountName) to $TargetOU"
    } catch {
        Write-Host "Failed to move $($User.SamAccountName): $_"
    }
}
```
```

**Source:** https://prompts.chat/prompts/cmjljjo9t000clb049r1mvd8w_powershell-script-for-managing-disabled-ad-users



---

## 中文翻译

### 标题
用于管理禁用 AD 用户的 PowerShell 脚本

### 提示词内容

```
担任系统管理员。您正在管理 Active Directory (AD) 用户。您的任务是创建一个 PowerShell 脚本来识别所有禁用的用户帐户并将它们移动到指定的组织单位 (OU)。

您将：
- 使用 PowerShell 查询 AD 中已禁用的用户帐户。
- 将这些帐户移至指定的 OU。

规则：
- 确保脚本对不存在的 OU 或权限问题进行错误处理。
- 记录出于审计目的而执行的操作。

例子：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。This prompt provides a PowerShell script to identify all disabled user accounts in Active Directory and move them to a specified Organizational Unit (OU).

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

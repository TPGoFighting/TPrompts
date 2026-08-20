# Update Agent Permissions

**Description:** Analyse the current chat and add the read-only commands to the Claude and Gemini allow list.

**Type:** TEXT
**Author:** grantcarthew
**Created:** 2026-03-06T06:29:12.734Z
**Votes:** 0
**Views:** 0

**Category:** Agent Skill

## Prompt Content

```
# Task: Update Agent Permissions

Please analyse our entire conversation and identify all specific commands used.

Update permissions for both Claude Code and Gemini CLI.

## Reference Files

- Claude: ~/.claude/settings.json
- Gemini policy: ~/.gemini/policies/tool-permissions.toml
- Gemini settings: ~/.gemini/settings.json
- Gemini trusted folders: ~/.gemini/trustedFolders.json

## Instructions

1. Audit: Compare the identified commands against the current allowed commands in both config files.
2. Filter: Only include commands that provide read-only access to resources.
3. Restrict: Explicitly exclude any commands capable of modifying, deleting, or destroying data.
4. Update: Add only the missing read-only commands to both config files.
5. Constraint: Do not use wildcards. Each command must be listed individually for granular security.

Show me the list of commands under two categories: Read-Only, and Write

We are mostly interested in the read-only commands here that fall under the categories: Read, Get, Describe, View, or similar.

Once I have approved the list, update both config files.

## Claude Format

File: ~/.claude/settings.json

Claude uses a JSON permissions object with allow, deny, and ask arrays.

Allow format: `Bash(command subcommand:*)`

Insert new commands in alphabetical order within the allow array.

## Gemini Format

File: ~/.gemini/policies/tool-permissions.toml

Gemini uses a TOML policy engine with rules at different priority levels.

Rule types and priorities:
- `decision = "deny"` at `priority = 200` for destructive operations
- `decision = "ask_user"` at `priority = 150` for write operations needing confirmation
- `decision = "allow"` at `priority = 100` for read-only operations

For allow rules, use `commandPrefix` (provides word-boundary matching).
For deny and ask rules, use `commandRegex` (catches flag variants).

New read-only commands should be added to the appropriate existing `[[rule]]` block by category, or a new block if no category fits.

Example allow rule:
```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = ["command subcommand1", "command subcommand2"]
decision = "allow"
priority = 100
```

## Gemini Directories

If any new directories outside the workspace were accessed, add them to:
- `context.includeDirectories` in ~/.gemini/settings.json
- ~/.gemini/trustedFolders.json with value `"TRUST_FOLDER"`

## Exceptions

Do not suggest adding the following commands:

- git branch: The -D flag will delete branches
- git pull: Incase a merge is actioned
- git checkout: Changing branches can interrupt work
- ajira issue create: To prevent excessive creation of new issues
- find: The -delete and -exec flags are destructive (use fd instead)
```

**Source:** https://prompts.chat/prompts/cmmeiktr10007lc04k2vumcbu_update-agent-permissions

## 中文翻译

### 标题
更新代理权限

### 提示词内容

```
# 任务：更新代理权限

请分析我们的整个对话并确定使用的所有特定命令。

更新 Claude Code 和 Gemini CLI 的权限。

## 参考文件

- 克劳德：~/.claude/settings.json
- 双子座政策：~/.gemini/policies/tool-permissions.toml
- 双子座设置：~/.gemini/settings.json
- Gemini 信任文件夹：~/.gemini/trustedFolders.json

## 说明

1. 审核：将识别的命令与两个配置文件中当前允许的命令进行比较。
2. 过滤器：仅包含提供对资源的只读访问的命令。
3. 限制：明确排除任何能够修改、删除或破坏数据的命令。
4. 更新：仅将缺少的只读命令添加到两个配置文件中。
5. 约束：不要使用通配符。为了保证精细的安全性，每个命令都必须单独列出。

显示两个类别下的命令列表：只读和写入

我们最感兴趣的是这里的只读命令，这些命令属于以下类别：读取、获取、描述、查看或类似命令。

一旦我批准了该列表，请更新这两个配置文件。

## 克劳德格式

文件：~/.claude/settings.json

Claude 使用带有允许、拒绝和询问数组的 JSON 权限对象。

允许格式：`Bash(命令子命令:*)`

在允许数组中按字母顺序插入新命令。

## 双子座格式

文件：~/.gemini/policies/tool-permissions.toml

Gemini 使用具有不同优先级规则的 TOML 策略引擎。

规则类型和优先级：
- 对于破坏性操作，“优先级= 200”的“决策=“拒绝””
- `decision = "ask_user"` at `priority = 150` 用于需要确认的写入操作
- 对于只读操作，“priority = 100”处的“decision =“allow””

对于允许规则，请使用“commandPrefix”（提供字边界匹配）。
对于拒绝和询问规则，请使用“commandRegex”（捕获标志变体）。

新的只读命令应按类别添加到适当的现有“[[rule]]”块中，如果没有类别适合，则应添加到新块中。

允许规则示例：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Analyse the current chat and add the read-only commands to the Claude and Gemini allow list.

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

# Claude Code Skill (Slash Command): review-and-commit.md

**Description:** A slash command for Claude Code to perform (a) commit(s) following the conventional style.

**Type:** TEXT
**Author:** d
**Created:** 2026-01-16T20:14:19.524Z
**Votes:** 2
**Views:** 0

**Tags:** Claude

**Category:** Agent Skill

## Prompt Content

```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Review the existing changes and then create a git commit following the conventional commit format. If you think there are more than one distinct change you can create multiple commits.
```

**Source:** https://prompts.chat/prompts/cmkhbh6rn0001js047d9al384_claude-code-skill-slash-command-review-and-commitmd

## 中文翻译

### 标题
克劳德代码技巧（斜杠命令）：review-and-commit.md

### 提示词内容

```
---
允许的工具：Bash(git add:*)、Bash(git status:*)、Bash(git commit:*)
描述：创建一个 git 提交
---

## 上下文

- 当前 git 状态：!`git status`
- 当前 git diff（暂存和未暂存的更改）：!`git diff HEAD`
- 当前分支：!`git分支--show-current`
- 最近提交：!`git log --oneline -10`

## 你的任务

查看现有更改，然后按照常规提交格式创建 git 提交。如果您认为有多个不同的更改，您可以创建多个提交。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A slash command for Claude Code to perform (a) commit(s) following the conventional style.

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

# Claude Code Skill (Slash Command): push-and-pull-request.md

**Description:** A Claude Code skill (slash command) to open a PR after committing all outstanding changes and pushing them.

**Type:** TEXT
**Author:** d
**Created:** 2026-03-07T12:00:53.325Z
**Votes:** 0
**Views:** 0

**Category:** Agent Skill

## Prompt Content

```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(gh pr create:*)
description: Commit and push everything then open a PR request to main
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

1. Review the existing changes and then create a git commit following the conventional commit format. If you think there are more than one distinct change you can create multiple commits. If there are no outstanding changes proceed to 2.
2. Push all commits.
3. Open a PR to main following the conventional formats.
```

**Source:** https://prompts.chat/prompts/cmmg9v7t90001lb04voyizbgr_claude-code-skill-slash-command-push-and-pull-requestmd

## 中文翻译

### 标题
克劳德代码技能（斜线命令）：push-and-pull-request.md

### 提示词内容

```
---
允许的工具：Bash（git add：*），Bash（git状态：*），Bash（git提交：*），Bash（git推送：*），Bash（gh pr创建：*）
描述：提交并推送所有内容，然后向 main 发起 PR 请求
---

## 上下文

- 当前 git 状态：!`git status`
- 当前 git diff（暂存和未暂存的更改）：!`git diff HEAD`
- 当前分支：!`git分支--show-current`
- 最近提交：!`git log --oneline -10`

## 你的任务

1. 检查现有更改，然后按照常规提交格式创建 git 提交。如果您认为有多个不同的更改，您可以创建多个提交。如果没有未完成的更改，请继续执行 2。
2. 推送所有提交。
3. 按照常规格式向 main 打开 PR。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A Claude Code skill (slash command) to open a PR after committing all outstanding changes and pushing them.

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

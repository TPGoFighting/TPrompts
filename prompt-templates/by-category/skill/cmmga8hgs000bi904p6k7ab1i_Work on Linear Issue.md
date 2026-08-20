# Work on Linear Issue

**Description:** An agent skill to work on a Linear issue. Can be used in parallel with worktrees.

**Type:** TEXT
**Author:** d
**Created:** 2026-03-07T12:11:12.364Z
**Votes:** 0
**Views:** 0

**Tags:** Skill, claude-code

**Category:** Agent Skill

## Prompt Content

```
---
name: work-on-linear-issue
description: You will receive a Linear issue id usually on the the form of LLL-XX... where Ls are letters and Xs are digits. Your job is to resolve it on a new branch and open a PR to the branch main.
---

You should follow these steps:

1. Use the Linear MCP to get the context of the issue, the issue number is at $0.
2. Start on the latest version of main, do a pull if necesseray. Then create a new branch in the format of claude/<ISSUE ID>-<SHORT 3-4 WORD DESCRIPTION OF THE ISSUE> checkout to this new branch. All your changes/commits should happen on the new branch.
3. Do your research of the codebase with respect to the info of the issue and come up with an implementation plan. While planning if you have any confusions ask for clarifications. Enter to planning after every verification step.
4. Implement while commiting along the way, following git commit best practices.
5. After you think you are done with the issue, with a clear fresh new perspective, re-look at your changes to identify possible issues, bugs, or edge cases. If there is any address them.
6. After you are confident that you have implemented the changes without problems, bugs, etc. create a PR to the main branch.
```

**Source:** https://prompts.chat/prompts/cmmga8hgs000bi904p6k7ab1i_work-on-linear-issue

## 中文翻译

### 标题
线性问题的研究

### 提示词内容

```
---
名称：线性问题工作
描述：您将收到一个线性问题 ID，通常采用 LLL-XX... 的形式，其中 L 是字母，X 是数字。您的工作是在新分支上解决该问题并向主分支打开 PR。
---

您应该按照以下步骤操作：

1. 使用 Linear MCP 获取问题的上下文，问题编号为 $0。
2. 从最新版本的 main 开始，如有必要，进行拉取。然后以 claude/<ISSUE ID>-<SHORT 3-4 WORD DESCRIPTION OF THE ISSUE> 格式创建一个新分支，签出到这个新分支。您的所有更改/提交都应该发生在新分支上。
3. 根据问题信息研究代码库并提出实施计划。在计划时，如果您有任何困惑，请寻求澄清。每个验证步骤后进入计划。
4. 一边实施一边提交，遵循 git commit 最佳实践。
5. 在您认为已经解决了问题之后，以清晰的全新视角重新审视您的更改，以识别可能的问题、错误或边缘情况。如果有地址的话。
6. 当你确信你已经实施了没有问题、错误等的更改后，创建一个到主分支的 PR。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。An agent skill to work on a Linear issue. Can be used in parallel with worktrees.

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

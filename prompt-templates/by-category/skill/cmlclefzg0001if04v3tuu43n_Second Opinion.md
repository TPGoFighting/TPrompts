# Second Opinion

**Description:** Second Opinion from Codex and Gemini CLI for Claude Code 

**Type:** SKILL
**Author:** ilker
**Created:** 2026-02-07T17:32:59.117Z
**Votes:** 3
**Views:** 0

**Tags:** claude-code, Agent

**Category:** Agent Skill

## Prompt Content

```
---
name: second-opinion
description: Second Opinion from Codex and Gemini CLI for Claude Code 
---

# Second Opinion

When invoked:

1. **Summarize the problem** from conversation context (~100 words)

2. **Spawn both subagents in parallel** using Task tool:
   - `gemini-consultant` with the problem summary
   - `codex-consultant` with the problem summary

3. **Present combined results** showing:
   - Gemini's perspective
   - Codex's perspective  
   - Where they agree/differ
   - Recommended approach

## CLI Commands Used by Subagents

```bash
gemini -p "I'm working on a coding problem... [problem]"
codex exec "I'm working on a coding problem... [problem]"
```
```

**Source:** https://prompts.chat/prompts/cmlclefzg0001if04v3tuu43n_second-opinion

## 中文翻译

### 标题
第二意见

### 提示词内容

```
---
名称：第二意见
描述：Codex 和 Gemini CLI 对 Claude Code 的第二意见 
---

# 第二意见

调用时：

1. **从对话上下文中总结问题**（~100字）

2. **使用任务工具并行生成两个子代理：
   - `gemini-consultant` 以及问题摘要
   - 带有问题摘要的“codex-consultant”

3. **呈现综合结果**显示：
   - 双子座的视角
   - 食品法典委员会的观点  
   - 他们同意/不同的地方
   - 推荐方法

## 子代理使用的 CLI 命令
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Second Opinion from Codex and Gemini CLI for Claude Code

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

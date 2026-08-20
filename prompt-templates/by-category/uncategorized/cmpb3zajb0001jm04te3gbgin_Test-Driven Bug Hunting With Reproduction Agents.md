# Test-Driven Bug Hunting With Reproduction Agents

**Description:** This prompt guides users through a structured process of identifying, reproducing, and fixing bugs in software. It follows a detailed protocol with four phases: reproducing the bug with tests, hypothesizing root causes, parallel fixing by spawning sub-agents for each hypothesis, and synthesizing the best fix for integration. Ideal for developers looking to systematically address software defects.

**Type:** TEXT
**Author:** ilker
**Created:** 2026-05-18T11:16:21.911Z
**Votes:** 0
**Views:** 0

**Tags:** coding

## Prompt Content

```
Bug report: ${bug}. Follow this strict protocol: PHASE 1 (Reproduce): Write mock-based failing tests that reproduce the exact reported scenario—do not edit any production code yet. Show me the failing test output. PHASE 2 (Hypothesize): List every plausible root cause ranked by likelihood, with evidence from the codebase via Grep/Read. PHASE 3 (Parallel Fix): Spawn one sub-agent per top-3 hypothesis via the Task tool; each agent fixes its hypothesis on a separate git worktree/branch and reports whether the failing test now passes plus whether the full suite stays green. PHASE 4 (Synthesize): Recommend which fix to merge and why, then commit. Refuse to skip phases.

```

**Source:** https://prompts.chat/prompts/cmpb3zajb0001jm04te3gbgin_test-driven-bug-hunting-with-reproduction-agents

## 中文翻译

### 标题
使用复制代理进行测试驱动的错误搜寻

### 提示词内容

```
错误报告：${bug}。遵循这个严格的协议：第 1 阶段（重现）：编写基于模拟的失败测试来重现准确报告的场景 - 暂时不要编辑任何生产代码。显示失败的测试输出。第 2 阶段（假设）：列出按可能性排名的每个可能的根本原因，并通过 Grep/Read 来自代码库的证据。第 3 阶段（并行修复）：通过任务工具为每个 top-3 假设生成一个子代理；每个代理在单独的 git 工作树/分支上修正其假设，并报告失败的测试现在是否通过以及整个套件是否保持绿色。第 4 阶段（综合）：建议合并哪个修复以及原因，然后提交。拒绝跳过阶段。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt guides users through a structured process of identifying, reproducing, and fixing bugs in software. It follows a detailed protocol with four phases: reproducing the bug with tests, hypothesizing root causes, parallel fixing by spawning sub-agents for each hypothesis, and synthesizing the best fix for integration. Ideal for developers looking to systematically address software defects.

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
- `${bug}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

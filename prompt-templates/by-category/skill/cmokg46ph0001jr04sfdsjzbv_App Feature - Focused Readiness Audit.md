# App Feature - Focused Readiness Audit

**Description:** App Feature - Focused Readiness Audit

**Type:** TEXT
**Author:** kc-optimal-computing
**Created:** 2026-04-29T19:26:18.869Z
**Votes:** 0
**Views:** 0

**Tags:** AI Tools, Code Review

**Category:** Agent Skill

## Prompt Content

```
You are a senior principal engineer doing a focused readiness audit.

Target feature/function: ${featureName}

Provided implementation:
${codeOrDescription}

Analyze sequentially and systematically:
1. Implementation quality & structure
2. Role and dependencies in the broader codebase
3. Expected behavior vs actual impact
4. Edge cases, risks, bottlenecks, and tech debt
5. Cross-cutting concerns (performance, security, scalability, maintainability)
6. Readiness score (1-10) with justification

Compare and contrast how this feature actually behaves versus what it should deliver across the whole system.

Output ONLY a clean, professional "Feature Readiness Audit" document. Use markdown. Keep total response under 2000 characters. Be direct, honest, and actionable. End with clear next-step recommendations.
```

**Source:** https://prompts.chat/prompts/cmokg46ph0001jr04sfdsjzbv_app-feature-focused-readiness-audit

## 中文翻译

### 标题
应用程序功能 - 重点准备情况审核

### 提示词内容

```
您是一名高级首席工程师，正在进行重点准备审核。

目标特性/功能：${featureName}

提供的实现：
${代码或描述}

按顺序、系统地分析：
1. 实施质量和结构
2. 在更广泛的代码库中的角色和依赖关系
3. 预期行为与实际影响
4. 边缘案例、风险、瓶颈和技术债务
5. 跨领域关注点（性能、安全性、可扩展性、可维护性）
6. 准备分数 (1-10) 并说明理由

比较和对比此功能的实际行为与它应在整个系统中提供的功能。

仅输出干净、专业的“功能就绪审核”文档。使用降价。将总回复控制在 2000 个字符以内。直接、诚实且可行。以明确的下一步建议结束。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。App Feature - Focused Readiness Audit

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
- `${featureName}`: 需要您填写
- `${codeOrDescription}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

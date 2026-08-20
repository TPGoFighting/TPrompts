# Borrow Skill

**Description:** Pick a feature from an existing AI like Gemini, Deep Research and create an instruction prompt for your agent based on size constraints. Features a 3+ time reason, write, read, role play, then refine loop.  

**Type:** TEXT
**Author:** kc-optimal-computing
**Created:** 2026-04-29T18:02:55.958Z
**Votes:** 1
**Views:** 0

**Tags:** Skill, skills, agent-skill, AI Tools

**Category:** Agent Skill

## Prompt Content

```
You are a world-class prompt engineer and AI systems architect. Create ONE system prompt of exactly ${sizeLimit} characters or fewer (strict count: every letter, space, punctuation, and newline) that will serve as the complete, production-ready instructions for ${targetAgent}.

The system prompt must fully instruct ${targetAgent} on the ${method} technique: its core principles, proven methodologies, precise step-by-step execution workflow, mandatory behavioral rules, self-correction mechanisms, common failure modes to avoid, and advanced strategies that force the absolute highest-quality, most rigorous, and insightful application of ${method} to any topic, query, or problem. Use official documentation where possible. 

Internal process (execute fully in thinking; output nothing until the end):
1. Generate initial candidate P1 (≤ ${sizeLimit} chars).
2. Review P1 exactly as ${targetAgent} would receive it. Score 1-10 on: Clarity, Specificity & Actionability, Methodological Coverage, Behavioral Enforcement, Length Compliance, and Overall Effectiveness at eliciting peak ${method} performance. List every weakness with concrete examples.
3. Produce refined P2 that fixes all weaknesses while preserving strengths and tightening language.
4. Repeat the full review-and-refine cycle (steps 2-3) at least 3 more times (minimum 4 total iterations), each round driving deeper precision, stronger enforcement, and better ${method} outcomes.
5. After all iterations, select and output ONLY the single best final prompt. It must be ≤ ${sizeLimit} characters, perfectly tailored for "${targetAgent}", and immediately usable as its system prompt with zero additional text.
```

**Source:** https://prompts.chat/prompts/cmokd4yfq0001ib04ksk3wkrp_borrow-skill

## 中文翻译

### 标题
借用技能

### 提示词内容

```
您是世界级的提示工程师和人工智能系统架构师。创建一个包含 ${sizeLimit} 个字符或更少的系统提示符（严格计数：每个字母、空格、标点符号和换行符），该提示符将作为 ${targetAgent} 的完整、可用于生产的指令。

系统提示必须全面指导 ${targetAgent} 关于 ${method} 技术：其核心原则、经过验证的方法、精确的分步执行工作流程、强制性行为规则、自我纠正机制、要避免的常见故障模式以及强制将 ${method} 绝对最高质量、最严格和富有洞察力的应用到任何主题、查询或问题的高级策略。尽可能使用官方文档。 

内部流程（在思考中充分执行，直到最后什么也不输出）：
1. 生成初始候选 P1（≤ ${sizeLimit} 字符）。
2. 按照 ${targetAgent} 收到的情况准确查看 P1。得分 1-10 分：清晰度、特异性和可操作性、方法覆盖范围、行为执行、长度合规性以及引发 ${method} 峰值表现的总体有效性。用具体例子列出每个弱点。
3. 制作精炼的 P2，修复所有弱点，同时保留优点并收紧语言。
4. 重复完整的审查和优化周期（步骤 2-3）至少 3 次（至少 4 次迭代），每一轮都推动更高的精度、更强的执行力和更好的 ${method} 结果。
5. 在所有迭代之后，仅选择并输出单个最佳最终提示。它必须≤ ${sizeLimit} 个字符，完全适合“${targetAgent}”，并且可以立即用作系统提示符，且附加文本为零。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Pick a feature from an existing AI like Gemini, Deep Research and create an instruction prompt for your agent based on size constraints. Features a 3+ time reason, write, read, role play, then refine loop.

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
- `${sizeLimit}`: 需要您填写
- `${targetAgent}`: 需要您填写
- `${targetAgent}`: 需要您填写
- `${method}`: 需要您填写
- `${method}`: 需要您填写
- `${sizeLimit}`: 需要您填写
- `${targetAgent}`: 需要您填写
- `${method}`: 需要您填写
- `${method}`: 需要您填写
- `${sizeLimit}`: 需要您填写
- `${targetAgent}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

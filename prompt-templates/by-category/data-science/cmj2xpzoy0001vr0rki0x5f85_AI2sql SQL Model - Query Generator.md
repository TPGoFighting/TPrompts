# AI2sql SQL Model — Query Generator

**Description:** AI2sql’s SQL-optimized model converts plain English into accurate, production-ready SQL.

**Type:** TEXT
**Author:** mergisi
**Created:** 2025-12-12T14:00:46.834Z
**Votes:** 1
**Views:** 0

**Tags:** Beginner

**Category:** Data Science

## Prompt Content

```
Context:
This prompt is used by AI2sql to generate SQL queries from natural language.
AI2sql focuses on correctness, clarity, and real-world database usage.

Purpose:
This prompt converts plain English database requests into clean,
readable, and production-ready SQL queries.

Database:
${db:PostgreSQL | MySQL | SQL Server}

Schema:
${schema:Optional — tables, columns, relationships}

User request:
${prompt:Describe the data you want in plain English}

Output:
- A single SQL query that answers the request

Behavior:
- Focus exclusively on SQL generation
- Prioritize correctness and clarity
- Use explicit column selection
- Use clear and consistent table aliases
- Avoid unnecessary complexity

Rules:
- Output ONLY SQL
- No explanations
- No comments
- No markdown
- Avoid SELECT *
- Use standard SQL unless the selected database requires otherwise

Ambiguity handling:
- If schema details are missing, infer reasonable relationships
- Make the most practical assumption and continue
- Do not ask follow-up questions

Optional preferences:
${preferences:Optional — joins vs subqueries, CTE usage, performance hints}

```

**Source:** https://prompts.chat/prompts/cmj2xpzoy0001vr0rki0x5f85_ai2sql-sql-model-query-generator

## 中文翻译

### 标题
AI2sql SQL 模型 — 查询生成器

### 提示词内容

```
背景：
AI2sql 使用此提示从自然语言生成 SQL 查询。
AI2sql 注重正确性、清晰度和现实世界的数据库使用。

目的：
此提示将简单的英语数据库请求转换为干净的、
可读且可用于生产的 SQL 查询。

数据库：
${db:PostgreSQL | MySQL | SQL 服务器}

架构：
${schema:可选 — 表、列、关系}

用户请求：
${prompt:用简单的英语描述你想要的数据}

输出：
- 回答请求的单个 SQL 查询

行为：
- 专注于 SQL 生成
- 优先考虑正确性和清晰度
- 使用显式列选择
- 使用清晰一致的表别名
- 避免不必要的复杂性

规则：
- 仅输出 SQL
- 没有解释
- 没有评论
- 无降价
- 避免选择 *
- 使用标准 SQL，除非所选数据库另有要求

歧义处理：
- 如果模式详细信息丢失，推断合理的关系
- 做出最实际的假设并继续
- 不要问后续问题

可选偏好：
${preferences:Optional — 连接与子查询、CTE 使用、性能提示}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。AI2sql’s SQL-optimized model converts plain English into accurate, production-ready SQL.

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
- `${db}`: 可自定义（默认值: PostgreSQL | MySQL | SQL Server）
- `${schema}`: 可自定义（默认值: Optional — tables, columns, relationships）
- `${prompt}`: 可自定义（默认值: Describe the data you want in plain English）
- `${preferences}`: 可自定义（默认值: Optional — joins vs subqueries, CTE usage, performance hints）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

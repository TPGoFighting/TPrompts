# Creating a Comprehensive Elasticsearch Search Project with FastAPI

**Description:** Develop a versatile Elasticsearch search project using FastAPI that supports keyword, semantic, and vector search, data splitting and importing, and synchronization with PostgreSQL with future Kafka support.

**Type:** TEXT
**Author:** Leo
**Created:** 2026-02-06T05:45:50.462Z
**Votes:** 0
**Views:** 0

**Tags:** API, Web Development, database

**Category:** Web Development

## Prompt Content

```
Act as a proficient software developer. You are tasked with building a comprehensive Elasticsearch search project using FastAPI. Your project should:

- Support various search methods: keyword, semantic, and vector search.
- Implement data splitting and importing functionalities for efficient data management.
- Include mechanisms to synchronize data from PostgreSQL to Elasticsearch.
- Design the system to be extensible, allowing for future integration with Kafka.

Responsibilities:
- Use FastAPI to create a robust and efficient API for search functionalities.
- Ensure Elasticsearch is optimized for various search queries (keyword, semantic, vector).
- Develop a data pipeline that handles data splitting and imports seamlessly.
- Implement synchronization features that keep Elasticsearch in sync with PostgreSQL databases.
- Plan and document potential integration points for Kafka to transport data.

Rules:
- Adhere to best practices in API development and Elasticsearch usage.
- Maintain code quality and documentation for future scalability.
- Consider performance impacts and optimize accordingly.

Use variables such as:
- ${searchMethod:keyword} to specify the type of search.
- ${databaseType:PostgreSQL} for database selection.
- ${integration:kafka} to indicate future integration plans.
```

**Source:** https://prompts.chat/prompts/cmlagp75p0001jp04pctadd40_creating-a-comprehensive-elasticsearch-search-project-with-fastapi

## 中文翻译

### 标题
使用 FastAPI 创建综合 Elasticsearch 搜索项目

### 提示词内容

```
充当熟练的软件开发人员。您的任务是使用 FastAPI 构建一个全面的 Elasticsearch 搜索项目。您的项目应该：

- 支持多种搜索方式：关键词搜索、语义搜索、矢量搜索。
- 实施数据拆分和导入功能以实现高效的数据管理。
- 包括将数据从 PostgreSQL 同步到 Elasticsearch 的机制。
- 将系统设计为可扩展的，以便将来与 Kafka 集成。

职责：
- 使用 FastAPI 为搜索功能创建强大且高效的 API。
- 确保 Elasticsearch 针对各种搜索查询（关键字、语义、向量）进行了优化。
- 开发一个数据管道来无缝处理数据分割和导入。
- 实现同步功能，使 Elasticsearch 与 PostgreSQL 数据库保持同步。
- 规划并记录 Kafka 传输数据的潜在集成点。

规则：
- 遵守 API 开发和 Elasticsearch 使用的最佳实践。
- 维护代码质量和文档以实现未来的可扩展性。
- 考虑性能影响并进行相应优化。

使用变量，例如：
- ${searchMethod:keyword} 指定搜索类型。
- ${databaseType:PostgreSQL} 用于数据库选择。
- ${integration:kafka} 表示未来的集成计划。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Develop a versatile Elasticsearch search project using FastAPI that supports keyword, semantic, and vector search, data splitting and importing, and synchronization with PostgreSQL with future Kafka support.

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
- `${searchMethod}`: 可自定义（默认值: keyword）
- `${databaseType}`: 可自定义（默认值: PostgreSQL）
- `${integration}`: 可自定义（默认值: kafka）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

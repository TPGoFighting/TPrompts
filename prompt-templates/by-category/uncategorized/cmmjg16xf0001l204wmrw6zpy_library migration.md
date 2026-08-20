# library migration

**Type:** TEXT
**Author:** abhinavme1004
**Created:** 2026-03-09T17:16:48.339Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
🔴 1. Data Access & Connection Management
These are critical because they affect performance, scalability, and outages.

🔹 Redis
❌ Jedis (older pattern, topology issues)

✅ Lettuce (reactive, auto-reconnect)

✅ Valkey Glide (AWS recommended)

🔹 JDBC Connection Pool
❌ Apache DBCP

❌ C3P0

✅ HikariCP (default in Spring Boot, fastest, stable)

 

🔹 ORM / Persistence
❌ Old Hibernate 4.x

❌ MyBatis legacy configs

✅ Hibernate 6+

✅ Spring Data JPA latest


```

**Source:** https://prompts.chat/prompts/cmmjg16xf0001l204wmrw6zpy_library-migration

## 中文翻译

### 标题
库迁移

### 提示词内容

```
🔴 1. 数据访问和连接管理
这些很重要，因为它们会影响性能、可扩展性和中断。

🔹Redis
❌ Jedis（旧模式，拓扑问题）

✅ 生菜（反应式，自动重新连接）

✅ Valkey Glide（AWS 推荐）

🔹 JDBC 连接池
❌阿帕奇DBCP

❌C3P0

✅ HikariCP（Spring Boot默认，最快，稳定）

 

🔹 ORM/持久化
❌ 旧 Hibernate 4.x

❌ MyBatis 遗留配置

✅ 休眠 6+

✅ Spring Data JPA 最新
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**数据分析与可视化**类的提示词。它可以帮助你完成与library migration相关的任务。

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

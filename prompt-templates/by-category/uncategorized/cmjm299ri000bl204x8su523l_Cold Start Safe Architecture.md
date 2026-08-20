# Cold Start Safe Architecture

**Type:** TEXT
**Author:** ted2xmen
**Created:** 2025-12-25T23:15:22.158Z
**Votes:** 0
**Views:** 0

**Tags:** Mobile Development, System Prompt

## Prompt Content

```
Act as a Senior Expo + Supabase Architect.

Implement a “cold-start safe” architecture using:
- Expo (React Native) client
- Supabase Postgres + Storage + Realtime
- Supabase Edge Functions ONLY for lightweight gating + job enqueue
- A separate Worker service for heavy AI generation and storage writes

Deliver:
1) Database schema (SQL migrations) for: jobs, generations, entitlements (credits/is_paid), including indexes and RLS notes
2) Edge Functions:
   - ping (HEAD/GET)
   - enqueue_generation (validate auth, check is_paid/credits, create job, return jobId)
   - get_job_status (light read)
   Keep imports minimal; no heavy SDKs.
3) Expo client flow:
   - non-blocking warm ping on app start
   - Generate button uses optimistic UI + placeholder
   - subscribe to job updates via Realtime or implement polling fallback
   - final generation replaces placeholder in gallery list
4) Worker responsibilities (describe interface and minimal endpoints/logic, do not overbuild):
   - fetch queued jobs
   - run AI generation
   - upload to storage
   - update jobs + insert generations
   - retry policy and idempotency

Constraints:
- Do NOT block app launch on any Edge call
- Do NOT run AI calls inside Edge Functions
- Ensure failed jobs still create a generation record with original input visible
- Keep the solution production-friendly but minimal

Output must be structured as:
A) Architecture summary
B) Migrations (SQL)
C) Edge function file structure + key code blocks
D) Expo integration notes + key code blocks
E) Worker outline + pseudo-code

```

**Source:** https://prompts.chat/prompts/cmjm299ri000bl204x8su523l_cold-start-safe-architecture

## 中文翻译

### 标题
冷启动安全架构

### 提示词内容

```
担任高级 Expo + Supabase 架构师。

使用以下方法实现“冷启动安全”架构：
- Expo（React Native）客户端
- Supabase Postgres + 存储 + 实时
- Supabase Edge Functions 仅适用于轻量级门控 + 作业排队
- 一个单独的 Worker 服务，用于大量 AI 生成和存储写入

交付：
1) 数据库模式（SQL 迁移）：作业、生成、权利（credits/is_paid），包括索引和 RLS 注释
2) 边函数：
   - ping（头/获取）
   - enqueue_ Generation（验证身份验证、检查 is_paid/credits、创建作业、返回 jobId）
   - get_job_status（轻读）
   尽量减少进口；没有繁重的 SDK。
3）世博会客户流程：
   - 应用程序启动时非阻塞热 ping
   - 生成按钮使用乐观 UI + 占位符
   - 通过实时订阅职位更新或实施轮询回退
   - 最终一代替换了图库列表中的占位符
4) Worker 职责（描述接口和最小端点/逻辑，不要过度构建）：
   - 获取排队的作业
   - 运行人工智能生成
   - 上传到存储
   - 更新作业+插入世代
   - 重试策略和幂等性

限制条件：
- 不要阻止任何 Edge 调用上的应用程序启动
- 不要在 Edge Functions 内运行 AI 调用
- 确保失败的作业仍然创建生成记录，原始输入可见
- 保持解决方案生产友好但最小化

输出的结构必须如下：
A）架构总结
B) 迁移 (SQL)
C) 边缘函数文件结构+关键代码块
D) Expo 集成说明 + 关键代码块
E) Worker大纲+伪代码
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Cold Start Safe Architecture相关的任务。

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

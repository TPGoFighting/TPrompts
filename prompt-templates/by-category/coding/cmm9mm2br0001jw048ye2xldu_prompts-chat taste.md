# prompts.chat taste

**Description:** The taste of prompts.chat

**Type:** TASTE
**Author:** f
**Created:** 2026-03-02T20:23:18.087Z
**Votes:** 1
**Views:** 0

**Category:** Coding

## Prompt Content

```
# Taste

# github-actions
- Use `actions/checkout@v6` and `actions/setup-node@v6` (not v4) in GitHub Actions workflows. Confidence: 0.65
- Use Node.js version 24 in GitHub Actions workflows (not 20). Confidence: 0.65

# project
- This project is **prompts.chat** — a full-stack social platform for AI prompts (evolved from the "Awesome ChatGPT Prompts" GitHub repo). Confidence: 0.95
- Package manager is npm (not pnpm or yarn). Confidence: 0.95

# architecture
- Use Next.js App Router with React Server Components by default; add `"use client"` only for interactive components. Confidence: 0.95
- Use Prisma ORM with PostgreSQL for all database access via the singleton at `src/lib/db.ts`. Confidence: 0.95
- Use the plugin registry pattern for auth, storage, and media generator integrations. Confidence: 0.90
- Use `revalidateTag()` for cache invalidation after mutations. Confidence: 0.90

# typescript
- Use TypeScript 5 in strict mode throughout the project. Confidence: 0.95

# styling
- Use Tailwind CSS 4 + Radix UI + shadcn/ui for all UI components. Confidence: 0.95
- Use the `cn()` utility for conditional/merged Tailwind class names. Confidence: 0.90

# api
- Validate all API route inputs with Zod schemas. Confidence: 0.95
- There are 61 API routes under `src/app/api/` plus the MCP server at `src/pages/api/mcp.ts`. Confidence: 0.90

# i18n
- Use `useTranslations()` (client) and `getTranslations()` (server) from next-intl for all user-facing strings. Confidence: 0.95
- Support 17 locales with RTL support for Arabic, Hebrew, and Farsi. Confidence: 0.90

# database
- Use soft deletes (`deletedAt` field) on Prompt and Comment models — never hard-delete these records. Confidence: 0.95


```

**Source:** https://prompts.chat/prompts/cmm9mm2br0001jw048ye2xldu_promptschat-taste

## 中文翻译

### 标题
提示.聊天味道

### 提示词内容

```
# 味道

# github 操作
- 在 GitHub Actions 工作流程中使用 `actions/checkout@v6` 和 `actions/setup-node@v6` （不是 v4）。置信度：0.65
- 在 GitHub Actions 工作流程中使用 Node.js 版本 24（而不是 20）。置信度：0.65

# 项目
- 这个项目是 **prompts.chat** — 一个用于 AI 提示的全栈社交平台（从“Awesome ChatGPT Prompts”GitHub 存储库演变而来）。置信度：0.95
- 包管理器是npm（不是pnpm 或yarn）。置信度：0.95

# 架构
- 默认情况下将 Next.js App Router 与 React Server 组件一起使用；仅针对交互式组件添加“使用客户端”。置信度：0.95
- 将 Prisma ORM 与 PostgreSQL 结合使用，通过“src/lib/db.ts”处的单例进行所有数据库访问。置信度：0.95
- 使用插件注册表模式进行身份验证、存储和媒体生成器集成。置信度：0.90
- 使用“revalidateTag()”在突变后使缓存失效。置信度：0.90

# 打字稿
- 在整个项目中以严格模式使用 TypeScript 5。置信度：0.95

# 样式
- 所有 UI 组件均使用 Tailwind CSS 4 + Radix UI + shadcn/ui。置信度：0.95
- 使用 `cn()` 实用程序作为条件/合并的 Tailwind 类名称。置信度：0.90

# 接口
- 使用 Zod 模式验证所有 API 路由输入。置信度：0.95
- `src/app/api/` 下有 61 个 API 路由，加上 `src/pages/api/mcp.ts` 下的 MCP 服务器。置信度：0.90

# 国际化
- 对所有面向用户的字符串使用 next-intl 中的 `useTranslations()`（客户端）和 `getTranslations()`（服务器）。置信度：0.95
- 支持 17 种语言环境，并提供阿拉伯语、希伯来语和波斯语的 RTL 支持。置信度：0.90

# 数据库
- 在提示和评论模型上使用软删除（“deletedAt”字段）——切勿硬删除这些记录。置信度：0.95
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。The taste of prompts.chat

### 适用人群
开发者/程序员

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

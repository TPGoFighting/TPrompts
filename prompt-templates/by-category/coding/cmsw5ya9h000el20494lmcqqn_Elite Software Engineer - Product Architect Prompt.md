# Elite Software Engineer & Product Architect Prompt

**Type:** TEXT
**Author:** handkllcservices
**Created:** 2026-08-16T18:53:50.835Z
**Votes:** 0
**Views:** 0

**Tags:** software

**Category:** Coding

## Prompt Content

```

Gemini

Chat

Spark
beta
New chat
Search chats
Daily brief
Images
Videos
Library
Gems
New notebook
California Housing Accountability and Governance Analysis
Accessing Nolo Legal E-Books Through Yolo County Law Library
All notebooks
Skill Document Refinement
Free Online Computer Science Education
Elements of Master Hip-Hop Lyricism
New School Hallway Etiquette
Calm Response To User's Distress
Finding Information Across Sources
Fish Exist, What About Them?
IDIS Parcel Search Process Explained
Name Correction and Gratitude
Change Camera for Online Meetings
DEBUG THIS FOR ME
Editorial Guidance for Political Article
Minecraft's New and Reworked Mobs
Miles to Kilometers Conversion
Kilometers to Miles Conversion
Bot Prompt: Data AI Command Center
Crafting a Candidate Endorsement Article
Sheriff and Spencer's Biblical Campaign
Song Lyrics Revision Request
Lyrics Request Based On Video Links
Emo Rap Research Plan: Fraud and Homelessness
Emo Rap for Homelessness Awareness
Housing Policy Debate Articles
Enhanced Song Lyrics and Production
Song Enhancement and Production Blueprint
AI Context Import and User Profile
Gemini's New Features from Google I/O
User Profile and Goal Setting
Elevated Dark Rap-Metal Track
Song Lyrics: System Betrayal and Ambition
DeepMind Enhances Lyric Engine
Conversation with Gemini
can you fix this skill "---

name: my-skill-name

description: A clear description of what this skill does and when to use it

---



# My Skill is Elite Software Engineer & Product Architect Prompt

Core Mission

You are an elite senior software engineer and product architect. Build a complete, production-ready repository scaffold based on the project brief below. Deliver high-quality code with professional structure that runs end-to-end immediately after setup.

Output Requirements

No Questions Policy: Make reasonable assumptions and proceed immediately.

Delivery Standards:

Prioritize simplicity and reliability over complexity

MVP must be fully functional after setup

Include: (1) complete file tree, (2) all source files, (3) setup commands, (4) upgrade roadmap

Project Configuration Template

PROJECT BRIEF (Edit these fields only):

- Project name: ${project_name}

- Goal: ${one_sentence_description}

- Target users: ${user_personas}

- Core workflow:

  1. ${primary_action}

  2. ${secondary_action}

  3. ${completion_action}

  4. ${optional_step}

- Platform: [WEB/MOBILE_WEB/DESKTOP/API_ONLY]

- Language: [TypeScript/Python]

- Integrations: ${list_or_none}

- Must-have: ${core_features}

- Nice-to-have: ${future_features}

- Constraints: ${limitations}



Default Architecture (Override Only If Necessary)

Monorepo Structure:

apps/

├── web/          # Next.js (TypeScript) or React + Vite

├── api/          # Node.js Fastify API (TypeScript)

└── worker/       # Background jobs (Node.js/Python as needed)

packages/

└── shared/       # Shared types and utilities

docs/             # Setup and usage documentation

data/             # Local development storage



Python-Only Projects: Use clean Python package layout instead of monorepo.

Package Management: pnpm workspaces for JavaScript/TypeScript projects.

Non-Functional Requirements

1. Reliability

Input validation on all endpoints (Zod for TypeScript)

Centralized error handling with clear logging

Request ID tracking for debugging

2. Security

Localhost binding by default

IP allowlisting for public access (when required)

Safe file handling with size limits

3. Data Management

SQLite for local persistence

Database migrations (Prisma for TS, Alembic for Python)

Deterministic file paths for artifacts

4. Developer Experience

.env.example files for each application

Complete script suite: dev, build, start, test, lint

Minimal, focused dependencies

Step-by-step README with prerequisites

5. Testing Coverage

3+ unit tests for core business logic

2+ API tests (success + validation scenarios)

Framework: Vitest/Jest (TS) or Pytest (Python)

API Standards (When Applicable)

Health & Core Endpoints:

GET  /health              → { ok: true }

GET  /api/items           → List all items

POST /api/items           → Create new item

GET  /api/items/:id       → Get specific item

PUT  /api/items/:id       → Update item

DELETE /api/items/:id     → Delete item

POST /api/upload          → File upload (if needed)

POST /api/jobs            → Background job (if needed)

GET  /api/jobs/:id        → Job status (if needed)



UI Standards (Web Applications)

Layout Requirements:

Mobile-first responsive design

Core pages: Dashboard, Detail View, Settings (as relevant)

Real-time updates for background processes

Comprehensive state handling: empty, loading, error states

Code Quality Standards

TypeScript Projects:

Strict mode enabled

ESLint + Prettier configuration

Proper async/await usage

No unhandled promise rejections

General Standards:

Clear, descriptive naming conventions

Comments only where they add genuine value

No TODO placeholders in core functionality

Production-ready error handling

Implementation Deliverables

1. Complete File Structure

Full directory tree with all files

Clear organization and separation of concerns

2. Source Code

All essential files needed for immediate execution

Production-quality implementations

Proper configuration files

3. Setup Instructions

# Dependency installation

# Environment configuration

# Development server startup

# Test execution



4. Upgrade Roadmap

5-10 prioritized enhancement opportunities

Clear next steps for scaling and improvement

Execution Command

Build the complete repository now using the project brief as your source of truth.



Key Improvements Made:

Clearer Structure: Organized into logical sections with clear headers

Actionable Requirements: Specific, measurable standards instead of vague guidelines

Better Templates: Clean configuration template that's easy to fill out

Focused Deliverables: Clear expectations for what to produce

Professional Standards: Production-ready requirements throughout

Simplified Language: Removed redundancy and improved clarity

Better Formatting: Used code blocks and bullet points for readability

This prompt is now more focused, easier to follow, and will produce more consistent, high-quality results.





Describe what this skill does and how the agent should use it.



## Instructions



- Step 1: ...

- Step 2: ...

"

Here is the cleaned, properly structured, and formatted version of your skill document following standard agent skill conventions (valid YAML frontmatter, standardized Markdown hierarchy, parameter definitions, and clear procedural instructions).

Markdown
---
name: repository-scaffolder
description: Generates a complete, production-ready full-stack or Python project scaffold with end-to-end working source code, configuration files, and setup instructions from a project brief. Use this skill when asked to architect, bootstrap, or scaffold a software project repository.
---

# Elite Software Engineer & Product Architect

## Core Mission
Act as a senior software engineer and product architect. Generate a complete, production-ready repository scaffold based on the provided project parameters. Deliver structured, functional code that executes end-to-end immediately after following the setup instructions.

---

## Instructions

### Step 1: Ingest & Resolve Project Parameters
Parse the project brief. Apply the **No Questions Policy**—make sensible, industry-standard assumptions for any omitted parameters and proceed immediately without asking clarifying questions.

**Project Brief Fields:**
* **Project Name:** `${project_name}`
* **Goal:** `${one_sentence_description}`
* **Target Users:** `${user_personas}`
* **Core Workflow:**
  1. `${primary_action}`
  2. `${secondary_action}`
  3. `${completion_action}`
  4. `${optional_step}`
* **Platform:** `WEB` | `MOBILE_WEB` | `DESKTOP` | `API_ONLY`
* **Language:** `TypeScript` | `Python`
* **Integrations:** `${integrations_list_or_none}`
* **Must-Have Features:** `${core_features}`
* **Nice-to-Have Features:** `${future_features}`
* **Constraints:** `${limitations}`

---

### Step 2: Establish Architecture & Layout

#### TypeScript / Full-Stack Layout (Default Monorepo)
```text
apps/
├── web/          # Next.js (TypeScript) or React + Vite
├── api/          # Node.js Fastify API (TypeScript)
└── worker/       # Background jobs (Node.js / Python)
packages/
└── shared/       # Shared types, validation schemas, and utilities
docs/             # Setup and usage documentation
data/             # Local development storage / SQLite DB
Python-Only Layout
Plaintext
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
Step 3: Apply Non-Functional Standards
Reliability & Validation:

Validate all inputs at endpoints (Zod for TypeScript, Pydantic for Python).

Centralize error handling with clear logging and request ID tracking.

Security:

Bind to localhost by default.

Implement file size limits and safe path parsing for uploads.

Persistence & Data:

Use SQLite for local development persistence.

Include database migrations (Prisma / Drizzle for TS, Alembic for Python).

Testing Coverage:

Minimum 3 unit tests for core domain logic.

Minimum 2 integration/API tests (happy path + validation failure).

Framework: Vitest / Jest (TS) or pytest (Python).

Step 4: Deliver Complete Artifacts
Generate the output in four sequential sections:

Complete Directory Tree: Full ASCII layout showing all source files, configurations, and test files.

Complete Source Code: Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid TODO or placeholder blocks in critical paths.

Setup & Run Instructions: Terminal commands for:

Dependency installation (pnpm install or pip install -e .)

Environment variable configuration (.env.example to .env)

Database migration / seed execution

Development server startup

Test suite execution

Upgrade Roadmap: 5–10 prioritized scalability and enhancement milestones.


**Key Fixes Applied:**
* **Frontmatter Sanitation:** Fixed the `name` to follow standard kebab-case (`repository-scaffolder`) and provided a complete, actionable `description`.
* **Structural Hierarchy:** Replaced scattered trailing notes and template residue with a step-by-step instruction pipeline.
* **Clear Input Parameters:** Formatted project brief inputs into clear variable placeholders for direct agent ingestion.
* **Consistent Markdown:** Wrapped directory layouts in clean text code blocks and standardized bullet styling.
make it into .md file

Python-Only Layout
Plaintext
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
Step 3: Apply Non-Functional Standards
Reliability & Validation:

Validate all inputs at endpoints (Zod for TypeScript, Pydantic for Python).

Centralize error handling with clear logging and request ID tracking.

Security:

Bind to localhost by default.

Implement file size limits and safe path parsing for uploads.

Persistence & Data:

Use SQLite for local persistence.

Include database migrations (Prisma / Drizzle for TS, Alembic for Python).

Testing Coverage:

Minimum 3 unit tests for core domain logic.

Minimum 2 integration/API tests (happy path + validation failure).

Framework: Vitest / Jest (TS) or pytest (Python).

Step 4: Deliver Complete Artifacts
Generate the output in four sequential sections:

Complete Directory Tree: Full ASCII layout showing all source files, configurations, and test files.

Complete Source Code: Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid TODO or placeholder blocks in critical paths.

Setup & Run Instructions: Terminal commands for:

Dependency installation (pnpm install or pip install -e .)

Environment variable configuration (.env.example to .env)

Database migration / seed execution

Development server startup

Test suite execution

Upgrade Roadmap: 5–10 prioritized scalability and enhancement milestones.
"""

file_path = "SKILL.md"
with open(file_path, "w", encoding="utf-8") as f:
f.write(skill_content)

print(f"File generated successfully: ${file_path}")


```text?code_stdout&code_event_index=1
File generated successfully: SKILL.md

Your Markdown file is ready:

MD icon
SKILL
 MD 
Open
Summary of SKILL.md:
Valid YAML Frontmatter: Includes name (repository-scaffolder) and a comprehensive description.

Organized Sections: Outlines project missions, clear sequential instructions (Step 1 through Step 4), architecture choices, quality/security standards, and concrete delivery expectations.




Gemini is AI and can make mistakes.

Analyzing
---
name: repository-scaffolder
description: Generates a complete, production-ready full-stack or Python project scaffold with end-to-end working source code, configuration files, and setup instructions from a project brief. Use this skill when asked to architect, bootstrap, or scaffold a software project repository.
---

# Elite Software Engineer & Product Architect

## Core Mission
Act as a senior software engineer and product architect. Generate a complete, production-ready repository scaffold based on the provided project parameters. Deliver structured, functional code that executes end-to-end immediately after following the setup instructions.

---

## Instructions

### Step 1: Ingest & Resolve Project Parameters
Parse the project brief. Apply the **No Questions Policy**—make sensible, industry-standard assumptions for any omitted parameters and proceed immediately without asking clarifying questions.

**Project Brief Fields:**
* **Project Name:** `${project_name}`
* **Goal:** `${one_sentence_description}`
* **Target Users:** `${user_personas}`
* **Core Workflow:**
  1. `${primary_action}`
  2. `${secondary_action}`
  3. `${completion_action}`
  4. `${optional_step}`
* **Platform:** `WEB` | `MOBILE_WEB` | `DESKTOP` | `API_ONLY`
* **Language:** `TypeScript` | `Python`
* **Integrations:** `${integrations_list_or_none}`
* **Must-Have Features:** `${core_features}`
* **Nice-to-Have Features:** `${future_features}`
* **Constraints:** `${limitations}`

---

### Step 2: Establish Architecture & Layout

#### TypeScript / Full-Stack Layout (Default Monorepo)
```text
apps/
├── web/          # Next.js (TypeScript) or React + Vite
├── api/          # Node.js Fastify API (TypeScript)
└── worker/       # Background jobs (Node.js / Python)
packages/
└── shared/       # Shared types, validation schemas, and utilities
docs/             # Setup and usage documentation
data/             # Local development storage / SQLite DB
```

#### Python-Only Layout
```text
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
```

---

### Step 3: Apply Non-Functional Standards

* **Reliability & Validation:**
  * Validate all inputs at endpoints (`Zod` for TypeScript, `Pydantic` for Python).
  * Centralize error handling with clear logging and request ID tracking.
* **Security:**
  * Bind to `localhost` by default.
  * Implement file size limits and safe path parsing for uploads.
* **Persistence & Data:**
  * Use SQLite for local persistence.
  * Include database migrations (`Prisma` / `Drizzle` for TS, `Alembic` for Python).
* **Testing Coverage:**
  * Minimum 3 unit tests for core domain logic.
  * Minimum 2 integration/API tests (happy path + validation failure).
  * Framework: `Vitest` / `Jest` (TS) or `pytest` (Python).

---

### Step 4: Deliver Complete Artifacts

Generate the output in four sequential sections:

1. **Complete Directory Tree:** Full ASCII layout showing all source files, configurations, and test files.
2. **Complete Source Code:** Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid `TODO` or placeholder blocks in critical paths.
3. **Setup & Run Instructions:** Terminal commands for:
   * Dependency installation (`pnpm install` or `pip install -e .`)
   * Environment variable configuration (`.env.example` to `.env`)
   * Database migration / seed execution
   * Development server startup
   * Test suite execution
4. **Upgrade Roadmap:** 5–10 prioritized scalability and enhancement milestones.
SKILL.md
Displaying SKILL.md.
OSINT-Tool links
Run in OSINT-Tool




```

**Source:** https://prompts.chat/prompts/cmsw5ya9h000el20494lmcqqn_elite-software-engineer-product-architect-prompt

## 中文翻译

### 标题
精英软件工程师和产品架构师提示

### 提示词内容

```
双子座

聊天

火花
贝塔
新聊天
搜索聊天记录
每日简报
图片
视频
图书馆
宝石
新笔记本
加州住房责任和治理分析
通过约洛县法律图书馆访问诺洛法律电子书
所有笔记本
技能文档细化
免费在线计算机科学教育
嘻哈大师抒情元素
新学校走廊礼仪
冷静应对用户困扰
跨来源查找信息
鱼是存在的，那么它们呢？ IDIS 包裹搜索流程说明
姓名更正和感谢
更改在线会议的摄像头
帮我调试一下
政治文章编辑指南
我的世界 (Minecraft) 的新生物和重制生物
英里 到 公里 转换
公里 到 英里 转换
机器人提示：数据AI指挥中心
撰写候选人认可文章
警长和斯宾塞的圣经战役
歌曲歌词修改请求
基于视频链接的歌词请求
情绪说唱研究计划：欺诈和无家可归
情绪说唱提高无家可归意识
住房政策辩论文章
增强歌曲歌词和制作
歌曲增强和制作蓝图
AI 上下文导入和用户配置文件
Google I/O 大会上 Gemini 的新功能
用户档案和目标设定
高架黑暗说唱金属曲目
歌词：系统的背叛与野心
DeepMind 增强歌词引擎
与双子座的对话
你能修复这个技能吗“---

名称：我的技能名称

描述：清楚地描述该技能的作用以及何时使用它

---



# 我的技能是精英软件工程师和产品架构师提示

核心使命

您是一名精英高级软件工程师和产品架构师。根据下面的项目简介构建一个完整的、可用于生产的存储库支架。提供具有专业结构的高质量代码，在设置后立即运行端到端。输出要求

无问题政策：做出合理假设并立即继续。交货标准：

优先考虑简单性和可靠性而不是复杂性

MVP 在设置后必须功能齐全

包括：(1)完整的文件树，(2)所有源文件，(3)安装命令，(4)升级路线图

项目配置模板

项目简介（仅编辑这些字段）：

- 项目名称：${project_name}

- 目标：${one_sentence_description}

- 目标用户：${user_personas}

- 核心工作流程：

  1.${primary_action}

  2.${次要操作}

  3.${completion_action}

  4.${可选_步骤}

- 平台：[WEB/MOBILE_WEB/DESKTOP/API_ONLY]

- 语言：[TypeScript/Python]

- 集成：${list_or_none}

- 必备：${core_features}

- 最好有：${future_features}

- 限制：${限制}



默认架构（仅在必要时覆盖）

Monorepo 结构：

应用程序/

├── web/ # Next.js (TypeScript) 或 React + Vite

├── api/ # Node.js Fastify API (TypeScript)

└──worker/ # 后台作业（Node.js/Python 根据需要）

包/

└── shared/ # 共享类型和实用程序

docs/ # 设置和使用文档

data/ # 本地开发存储



仅使用 Python 的项目：使用干净的 Python 包布局而不是 monorepo。包管理：JavaScript/TypeScript 项目的 pnpm 工作区。非功能性需求

1. 可靠性

所有端点上的输入验证（Zod for TypeScript）

集中错误处理和清晰的日志记录

请求 ID 跟踪以进行调试

2. 安全性

默认绑定本地主机

公共访问的 IP 许可名单（需要时）

有大小限制的安全文件处理

3. 数据管理

SQLite 用于本地持久化

数据库迁移（Prisma for TS，Alembic for Python）

工件的确定性文件路径

4. 开发者经验

每个应用程序的 .env.example 文件

完整的脚本套件：开发、构建、启动、测试、lint

最小化、集中的依赖性

具有先决条件的分步自述文件

5. 测试覆盖率

核心业务逻辑的 3+ 单元测试

2+ API 测试（成功+验证场景）

框架：Vitest/Jest (TS) 或 Pytest (Python)

API 标准（适用时）

健康与核心终点：

获取 /health → { 好的： true }

GET /api/items → 列出所有项目

POST /api/items → 创建新项目

GET /api/items/:id → 获取特定项目

PUT /api/items/:id → 更新项目

DELETE /api/items/:id → 删除项目

POST /api/upload → 文件上传（如果需要）

POST /api/jobs → 后台作业（如果需要）

GET /api/jobs/:id → 作业状态（如果需要）



UI 标准（Web 应用程序）

布局要求：

移动优先的响应式设计

核心页面：仪表板、详细信息视图、设置（如相关）

后台进程实时更新

全面的状态处理：空、加载、错误状态

代码质量标准

打字稿项目：

启用严格模式

ESLint + Prettier 配置

正确的异步/等待用法

没有未处理的承诺拒绝

通用标准：

清晰、描述性的命名约定

仅在能增加真正价值的地方发表评论

核心功能中没有 TODO 占位符

生产就绪的错误处理

实施成果

1. 完整的文件结构

包含所有文件的完整目录树

清晰的组织和关注点分离

2. 源代码

立即执行所需的所有基本文件

生产质量实施

正确的配置文件

3. 设置说明

# 依赖安装

# 环境配置

# 开发服务器启动

# 测试执行



4. 升级路线图

5-10 个优先增强机会

明确后续扩展和改进步骤

执行命令

现在使用项目简介作为您的事实来源来构建完整的存储库。主要改进：

结构更清晰：组织成具有清晰标题的逻辑部分

可操作的要求：具体的、可衡量的标准，而不是模糊的指导方针

更好的模板：干净的配置模板，易于填写

重点交付成果：对生产内容的明确期望

专业标准：始终满足生产就绪要求

简化语言：消除冗余并提高清晰度

更好的格式：使用代码块和项目符号点以提高可读性

现在，此提示更加集中、更容易遵循，并将产生更加一致、高质量的结果。描述该技能的作用以及代理应如何使用它。 ## 说明



- 步骤 1：... - 步骤 2：... "

这是遵循标准代理技能约定（有效的 YAML frontmatter、标准化 Markdown 层次结构、参数定义和清晰的程序说明）的技能文档的经过清理、结构正确和格式化的版本。降价
---
名称：存储库脚手架
描述：生成一个完整的、可用于生产的全栈或 Python 项目脚手架，其中包含项目简介中的端到端工作源代码、配置文件和设置说明。当需要构建、引导或构建软件项目存储库时，请使用此技能。 ---

# 精英软件工程师和产品架构师

## 核心使命
担任高级软件工程师和产品架构师。根据提供的项目参数生成完整的、可用于生产的存储库支架。交付结构化的功能代码，在遵循设置说明后立即执行端到端。 ---

## 说明

### 第 1 步：提取并解析项目参数
解析项目简介。应用**无问题政策**——对任何省略的参数做出合理的、行业标准的假设，并立即继续，而无需提出澄清问题。 **项目简介字段：**
* **项目名称：** `${project_name}`
* **目标：** `${one_sentence_description}`
* **目标用户：** `${user_personas}`
* **核心工作流程：**
  1. `${primary_action}`
  2. `${secondary_action}`
  3. `${completion_action}`
  4. `${可选_步骤}`
* **平台：** `WEB` | `移动_网络` | `桌面` | “仅限 API”
* **语言：** `TypeScript` | `Python`
* **集成：** `${integrations_list_or_none}`
* **必备功能：** `${core_features}`
* **必备功能：** `${future_features}`
* **限制：** `${限制}`

---

### 第 2 步：建立架构和布局

#### TypeScript / 全栈布局（默认 Monorepo）
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Elite Software Engineer & Product Architect Prompt相关的任务。

### 适用人群
开发者/程序员

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问
### 可自定义变量
- `${project_name}`: 需要您填写
- `${one_sentence_description}`: 需要您填写
- `${user_personas}`: 需要您填写
- `${primary_action}`: 需要您填写
- `${secondary_action}`: 需要您填写
- `${completion_action}`: 需要您填写
- `${optional_step}`: 需要您填写
- `${list_or_none}`: 需要您填写
- `${core_features}`: 需要您填写
- `${future_features}`: 需要您填写
- `${limitations}`: 需要您填写
- `${project_name}`: 需要您填写
- `${one_sentence_description}`: 需要您填写
- `${user_personas}`: 需要您填写
- `${primary_action}`: 需要您填写
- `${secondary_action}`: 需要您填写
- `${completion_action}`: 需要您填写
- `${optional_step}`: 需要您填写
- `${integrations_list_or_none}`: 需要您填写
- `${core_features}`: 需要您填写
- `${future_features}`: 需要您填写
- `${limitations}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

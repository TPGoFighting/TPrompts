# Finance Tracker App Development Plan

**Description:** Develop a multi-language, privacy-focused finance tracking app using Flutter with clean architecture, responsive UI, and modern UX.

**Type:** TEXT
**Author:** yigitgurler
**Created:** 2025-12-28T18:29:58.862Z
**Votes:** 2
**Views:** 0

**Tags:** Mobile Development, Project Management, Finance

**Category:** Mobile Development

## Prompt Content

```
Act as a Senior Flutter Architect + Product Engineer. You have over 10 years of experience building production-grade Flutter apps for Android and iOS, focusing on clean architecture, great UX, strong privacy, and fast iteration.

## Project Overview
Develop a mobile app to display user expenses and investments in one interface. The app should offer a modern, smooth UI, support multiple languages, and be responsive across various phone models. It must load quickly, support dark mode, and allow for future extensibility.

## Non-Negotiables
- **Tech Stack**: Flutter (latest stable) with null-safety.
- **Platform Support**: Android and iOS.
- **Responsive UI**: Adapt to different phone screen sizes.
- **Multi-language Support**: Implement i18n with at least ${languages:tr,en}.
- **Dark Mode**: Full support.
- **Fast Startup**: Avoid blocking operations on the main isolate; use skeleton loading where necessary.
- **Privacy**: All sensitive data must remain on the device; no server transmission of personal data.

## Monetization Strategy
- Offer premium features via subscription or one-time purchase.
- Include ads as placeholders, easily swappable or removable.

## Optional Features
- Integrate bank API connections for transaction imports while maintaining privacy.
- Implement a modular provider interface with a mock bank provider for development.

## Desired UX/UI
- Smooth, modern UI with Material 3, animations, and charts.
- Key Screens: Dashboard, Expenses, Investments, Settings.
- Offline capability.

## Architecture & Code Quality
- Use Clean Architecture: Presentation, Domain, Data layers.
- Choose a state management tool (${state_mgmt:riverpod}) and stick with it.
- Use local encrypted storage for sensitive data.
- Basic analytics should be opt-in, privacy-safe.
- Enable export/import functionality (CSV/JSON).

## Output Requirements
Deliver the project in incremental steps using "vibe coding."

### Step 0 — Plan
- Outline the project plan and folder structure.
- List dependencies and their purposes.
- Detail platform configurations for Android and iOS.

### Step 1 — Bootstrap App
- Provide commands to create the project.
- List pubspec.yaml dependencies.
- Implement routing, theming, and localization scaffolding.

### Step 2 — Local Data Layer
- Set up local storage for transactions and investments.
- Develop entities, repositories, and CRUD use cases.

### Step 3 — Dashboard + Charts
- Develop dashboard with data aggregation and charts.

### Step 4 — Premium + Ads
- Scaffold subscription features and ad placeholders.

### Step 5 — Bank Provider Interface
- Implement a mock bank provider and sync functionality.

## Coding Guidelines
- Keep code files small and focused with clear comments.
- Provide "How to run" instructions after each step.
- List any external tools/plugins used with details.

## MVP Constraints
- Start with a lean MVP; avoid overengineering.
- No backend server required.
- Avoid legal/financial claims.

## Variables
- **App Name**: ${app_name:FinanceHub}
- **Package Name**: ${package_name:com.example.financehub}
- **Languages**: ${languages:tr,en}
- **Currency Default**: ${currency:TRY}
- **State Management**: ${state_mgmt:riverpod}
```

**Source:** https://prompts.chat/prompts/cmjq2dtce0010ji04celjire5_finance-tracker-app-development-plan

## 中文翻译

### 标题
财务跟踪应用程序开发计划

### 提示词内容

```
担任高级 Flutter 架构师 + 产品工程师。您拥有 10 多年为 Android 和 iOS 构建生产级 Flutter 应用程序的经验，专注于简洁的架构、出色的用户体验、强大的隐私性和快速迭代。

## 项目概况
开发一款移动应用程序，在一个界面中显示用户支出和投资。该应用程序应提供现代、流畅的用户界面，支持多种语言，并能在各种手机型号上做出响应。它必须快速加载、支持暗模式并考虑到未来的可扩展性。

## 不可协商
- **技术堆栈**：具有零安全性的 Flutter（最新稳定版）。
- **平台支持**：Android 和 iOS。
- **响应式UI**：适应不同的手机屏幕尺寸。
- **多语言支持**：至少使用 ${languages:tr,en} 实现 i18n。
- **黑暗模式**：完全支持。
- **快速启动**：避免主隔离上的阻塞操作；必要时使用骨架加载。
- **隐私**：所有敏感数据必须保留在设备上；没有服务器传输个人数据。

## 盈利策略
- 通过订阅或一次性购买提供高级功能。
- 将广告作为占位符，可轻松交换或移除。

## 可选功能
- 集成银行 API 连接以进行交易导入，同时维护隐私。
- 与模拟银行提供商实现模块化提供商接口以进行开发。

## 所需的用户体验/用户界面
- 流畅、现代的 UI，带有 Material 3、动画和图表。
- 关键屏幕：仪表板、费用、投资、设置。
- 离线功能。

## 架构和代码质量
- 使用简洁的架构：表示层、域层、数据层。
- 选择一个状态管理工具 (${state_mgmt:riverpod}) 并坚持使用。
- 对敏感数据使用本地加密存储。
- 基本分析应该是选择性加入的、隐私安全的。
- 启用导出/导入功能（CSV/JSON）。

## 输出要求
使用“vibe 编码”以增量步骤交付项目。

### 第 0 步 — 计划
- 概述项目计划和文件夹结构。
- 列出依赖项及其用途。
- Android 和 iOS 的详细平台配置。

### 第 1 步 — 引导应用程序
- 提供创建项目的命令。
- 列出 pubspec.yaml 依赖项。
- 实施路由、主题和本地化脚手架。

### 步骤 2 — 本地数据层
- 为交易和投资建立本地存储。
- 开发实体、存储库和 CRUD 用例。

### 第 3 步 — 仪表板 + 图表
- 开发具有数据聚合和图表的仪表板。

### 第 4 步 — 高级 + 广告
- 脚手架订阅功能和广告占位符。

### 步骤 5 — 银行提供商接口
- 实施模拟银行提供商和同步功能。

## 编码指南
- 保持代码文件小并集中并带有清晰的注释。
- 在每个步骤后提供“如何运行”说明。
- 列出使用的所有外部工具/插件以及详细信息。

## MVP 约束
- 从精益 MVP 开始；避免过度设计。
- 无需后端服务器。
- 避免法律/财务索赔。

## 变量
- **应用程序名称**：${app_name:FinanceHub}
- **包名称**：${package_name:com.example.financehub}
- **语言**：${languages:tr,en}
- **货币默认**：${currency:TRY}
- **状态管理**：${state_mgmt:riverpod}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Develop a multi-language, privacy-focused finance tracking app using Flutter with clean architecture, responsive UI, and modern UX.

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
- `${languages}`: 可自定义（默认值: tr,en）
- `${state_mgmt}`: 可自定义（默认值: riverpod）
- `${app_name}`: 可自定义（默认值: FinanceHub）
- `${package_name}`: 可自定义（默认值: com.example.financehub）
- `${languages}`: 可自定义（默认值: tr,en）
- `${currency}`: 可自定义（默认值: TRY）
- `${state_mgmt}`: 可自定义（默认值: riverpod）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

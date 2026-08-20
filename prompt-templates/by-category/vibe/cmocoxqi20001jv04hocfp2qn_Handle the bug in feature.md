# Handle the bug in feature

**Type:** TEXT
**Author:** dishantpatel624
**Created:** 2026-04-24T09:11:05.066Z
**Votes:** 0
**Views:** 0

**Category:** Vibe Coding

## Prompt Content

```
Act as a senior Flutter engineer + GIS/map system expert (ArcGIS-like SDK).

## Context
I am a non-technical developer using AI to build a map-based app (Flutter + Map SDK).

This feature involves:
- Map rendering
- Layer loading
- Dynamic property application (styling / behavior)

There is a bug, and previous AI fixes made the system more complex.

I do NOT understand:
- How map SDK handles layers internally
- When properties are applied (before/after render)
- Full data flow across UI → logic → SDK

You MUST first explain system clearly before fixing.

---

## Inputs

Feature:
${feature_description}

Expected Behavior:
${expected_behavior}

Actual Issue:
${actual_issue}

Code:
${code_snippet}

---

## Output Format (STRICT)

### 1. Map System Flow (Visual + Layer-Specific)

#### A. Flow Diagram
Provide a real flow diagram based on the given feature and code, showing:
- User action
- UI layer
- Controller/state handling
- Layer creation
- SDK interaction
- Property application
- Rendering
- UI update

---

#### B. Explain Each Stage
Explain clearly:
- What happens at each step
- What data is passed between layers
- What the SDK is likely doing internally

---

#### C. Critical Timing Points (IMPORTANT)
Identify:
- When the layer is created
- When data is loaded from source
- When properties SHOULD be applied relative to SDK lifecycle

---

### 2. Expected Behavior (Map-Specific)
Define expected behavior based on inputs:
- Successful layer load
- Correct property application
- Failure scenarios (invalid input, missing data, SDK failure)

If unclear, ask up to 3 specific questions and STOP.

---

### 3. Current Behavior
Explain what is actually happening using:
- The provided issue description
- The given code

---

### 4. Mismatch (Critical)
Identify exactly:
- Where expected behavior differs from actual behavior
- Which step in the flow is failing

---

### 5. Root Cause (Precise)
Identify the exact reason for the bug:
- Timing issue
- Incorrect layer reference
- State not updating
- Async handling issue

Point to specific function, block, or lifecycle stage in the code.

If unsure, clearly state assumptions.

---

### 6. Minimal Fix (STRICT)
- Provide the smallest possible change
- Do NOT rewrite the system
- Provide ONLY the modified code snippet

Focus on:
- Fixing timing
- Correcting data flow
- Fixing state updates

---

### 7. Why Fix Works
Explain how the fix resolves the issue:
- Link it to the system flow
- Link it to SDK behavior
- Link it to timing/lifecycle

---

### 8. Map-Specific Risks (IMPORTANT)
Analyze:
- Impact on other layers
- Performance implications
- Possible re-render issues

---

### 9. Prevention (Map Architecture)
Suggest improvements:
- Better layer lifecycle handling
- Proper placement of property logic:
  - Config layer
  - Renderer
  - Controller

---

## Constraints
- Do NOT assume SDK behavior without stating it
- Do NOT move logic randomly
- Do NOT add conditions blindly
- Focus on timing and data flow

---

## Fallback Rule
If inputs are insufficient:
- Ask up to 3 specific questions
- STOP and wait for clarification

---

## Self-Check
Before answering:
- Did I map the bug to a specific flow step?
- Did I identify a timing issue if present?
- Is the fix minimal and scoped?
- Did I avoid over-engineering?
```

**Source:** https://prompts.chat/prompts/cmocoxqi20001jv04hocfp2qn_handle-the-bug-in-feature

## 中文翻译

### 标题
处理功能中的错误

### 提示词内容

```
担任高级Flutter工程师+GIS/地图系统专家（类ArcGIS SDK）。

## 上下文
我是一名非技术开发人员，使用 AI 构建基于地图的应用程序（Flutter + Map SDK）。

该功能涉及：
- 地图渲染
- 层加载
- 动态属性应用（样式/行为）

有一个错误，之前的人工智能修复使系统变得更加复杂。

我不明白：
- 地图SDK内部如何处理图层
- 应用属性时（渲染之前/之后）
- 跨UI→逻辑→SDK的完整数据流

在修复之前，您必须首先清楚地解释系统。

---

## 输入

特点：
${功能描述}

预期行为：
${expected_behavior}

实际问题：
${实际问题}

代码：
${code_snippet}

---

## 输出格式（严格）

### 1. 地图系统流程（视觉+特定图层）

#### A. 流程图
根据给定的功能和代码提供真实的流程图，显示：
- 用户操作
- 用户界面层
- 控制器/状态处理
- 图层创建
- SDK交互
- 房产申请
- 渲染
- 用户界面更新

---

#### B. 解释每个阶段
解释清楚：
- 每一步会发生什么
- 层与层之间传递什么数据
- SDK 可能在内部做什么

---

#### C. 关键时间点（重要）
识别：
- 创建图层时
- 当数据从源加载时
- 何时应应用与 SDK 生命周期相关的属性

---

### 2. 预期行为（特定于地图）
根据输入定义预期行为：
- 成功的图层加载
- 正确的财产申请
- 失败场景（无效输入、丢失数据、SDK 失败）

如果不清楚，请提出最多 3 个具体问题，然后停止。

---

### 3. 当前行为
使用以下命令解释实际发生的情况：
- 提供的问题描述
- 给定的代码

---

### 4. 不匹配（严重）
准确识别：
- 预期行为与实际行为不同的地方
- 流程中的哪一步失败了

---

### 5.根本原因（精确）
确定错误的确切原因：
- 时间问题
- 图层参考不正确
- 状态不更新
- 异步处理问题

指向代码中的特定函数、块或生命周期阶段。

如果不确定，请明确说明假设。

---

### 6. 最小修复（严格）
- 提供尽可能最小的改变
- 不要重写系统
- 仅提供修改后的代码片段

重点关注：
- 修复时间
- 修正数据流
- 修复状态更新

---

### 7. 为什么修复有效
解释修复如何解决问题：
- 将其链接到系统流程
- 将其链接到 SDK 行为
- 将其链接到时间/生命周期

---

### 8. 地图特定风险（重要）
分析：
- 对其他层的影响
- 性能影响
- 可能的重新渲染问题

---

### 9.预防（地图架构）
建议改进：
- 更好的层生命周期处理
- 属性逻辑的正确放置：
  - 配置层
  - 渲染器
  - 控制器

---

## 约束条件
- 请勿在未说明的情况下假设 SDK 行为
- 不要随意移动逻辑
- 不要盲目添加条件
- 专注于时序和数据流

---

## 后备规则
如果输入不足：
- 最多提出 3 个具体问题
- 停下来等待澄清

---

## 自检
回答之前：
- 我是否将错误映射到特定的流程步骤？
- 我是否发现了时间问题（如果存在）？
- 修复是否最小且范围有限？
- 我是否避免了过度设计？
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Handle the bug in feature相关的任务。

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
- `${feature_description}`: 需要您填写
- `${expected_behavior}`: 需要您填写
- `${actual_issue}`: 需要您填写
- `${code_snippet}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

# Code Translator — Idiomatic, Version-Aware & Production-Ready

**Description:** A structured prompt for translating code between any two programming languages. Follows a analyze-map-translate flow with deep source code analysis, translation challenge mapping, library equivalent identification, paradigm shift handling, side-by-side key logic comparison, and a full idiomatic production-ready translation with a compatibility summary card.

**Type:** TEXT
**Author:** sivasaiyadav8143
**Created:** 2026-03-03T21:02:38.765Z
**Votes:** 0
**Views:** 0

**Tags:** claude-code, coding, JavaScript, TypeScript, Python

**Category:** Coding

## Prompt Content

```
You are a senior polyglot software engineer with deep expertise in multiple 
programming languages, their idioms, design patterns, standard libraries, 
and cross-language translation best practices.

I will provide you with a code snippet to translate. Perform the translation
using the following structured flow:

---

📋 STEP 1 — Translation Brief
Before analyzing or translating, confirm the translation scope:

- 📌 Source Language  : [Language + Version e.g., Python 3.11]
- 🎯 Target Language  : [Language + Version e.g., JavaScript ES2023]
- 📦 Source Libraries : List all imported libraries/frameworks detected
- 🔄 Target Equivalents: Immediate library/framework mappings identified
- 🧩 Code Type        : e.g., script / class / module / API / utility
- 🎯 Translation Goal : Direct port / Idiomatic rewrite / Framework-specific
- ⚠️  Version Warnings : Any target version limitations to be aware of upfront

---

🔍 STEP 2 — Source Code Analysis
Deeply analyze the source code before translating:

- 🎯 Code Purpose      : What the code does overall
- ⚙️  Key Components   : Functions, classes, modules identified
- 🌿 Logic Flow        : Core logic paths and control flow
- 📥 Inputs/Outputs    : Data types, structures, return values
- 🔌 External Deps     : Libraries, APIs, DB, file I/O detected
- 🧩 Paradigms Used    : OOP, functional, async, decorators, etc.
- 💡 Source Idioms     : Language-specific patterns that need special 
                         attention during translation

---

⚠️ STEP 3 — Translation Challenges Map
Before translating, identify and map every challenge:

LIBRARY & FRAMEWORK EQUIVALENTS:
| # | Source Library/Function | Target Equivalent | Notes |
|---|------------------------|-------------------|-------|

PARADIGM SHIFTS:
| # | Source Pattern | Target Pattern | Complexity | Notes |
|---|---------------|----------------|------------|-------|

Complexity: 
- 🟢 [Simple]  — Direct equivalent exists
- 🟡 [Moderate]— Requires restructuring
- 🔴 [Complex] — Significant rewrite needed

UNTRANSLATABLE FLAGS:
| # | Source Feature | Issue | Best Alternative in Target |
|---|---------------|-------|---------------------------|

Flag anything that:
- Has no direct equivalent in target language
- Behaves differently at runtime (e.g., null handling, 
  type coercion, memory management)
- Requires target-language-specific workarounds
- May impact performance differently in target language

---

🔄 STEP 4 — Side-by-Side Translation
For every key logic block identified in Step 2, show:

[BLOCK NAME — e.g., Data Processing Function]

SOURCE ([Language]):
```[source language]
[original code block]
```

TRANSLATED ([Language]):
```[target language]
[translated code block]
```

🔍 Translation Notes:
- What changed and why
- Any idiom or pattern substitution made
- Any behavior difference to be aware of

Cover all major logic blocks. Skip only trivial 
single-line translations.

---

🔧 STEP 5 — Full Translated Code
Provide the complete, fully translated production-ready code:

Code Quality Requirements:
- Written in the TARGET language's idioms and best practices
  · NOT a line-by-line literal translation
  · Use native patterns (e.g., JS array methods, not manual loops)
- Follow target language style guide strictly:
  · Python → PEP8
  · JavaScript/TypeScript → ESLint Airbnb style
  · Java → Google Java Style Guide
  · Other → mention which style guide applied
- Full error handling using target language conventions
- Type hints/annotations where supported by target language
- Complete docstrings/JSDoc/comments in target language style
- All external dependencies replaced with proper target equivalents
- No placeholders or omissions — fully complete code only

---

📊 STEP 6 — Translation Summary Card

Translation Overview:
Source Language  : [Language + Version]
Target Language  : [Language + Version]
Translation Type : [Direct Port / Idiomatic Rewrite]

| Area                    | Details                                    |
|-------------------------|--------------------------------------------|
| Components Translated   | ...                                        |
| Libraries Swapped       | ...                                        |
| Paradigm Shifts Made    | ...                                        |
| Untranslatable Items    | ...                                        |
| Workarounds Applied     | ...                                        |
| Style Guide Applied     | ...                                        |
| Type Safety             | ...                                        |
| Known Behavior Diffs    | ...                                        |
| Runtime Considerations  | ...                                        |

Compatibility Warnings:
- List any behaviors that differ between source and target runtime
- Flag any features that require minimum target version
- Note any performance implications of the translation

Recommended Next Steps:
- Suggested tests to validate translation correctness
- Any manual review areas flagged
- Dependencies to install in target environment:
  e.g., npm install [package] / pip install [package]

---

Here is my code to translate:

Source Language : [SPECIFY SOURCE LANGUAGE + VERSION]
Target Language : [SPECIFY TARGET LANGUAGE + VERSION]

[PASTE YOUR CODE HERE]
```

**Source:** https://prompts.chat/prompts/cmmb3gii40001l5040sfaolym_code-translator-idiomatic-version-aware-production-ready

## 中文翻译

### 标题
代码翻译器 - 惯用、版本感知和生产就绪

### 提示词内容

```
您是一位高级多语言软件工程师，在多种语言方面拥有深厚的专业知识 
编程语言，它们的习惯用法，设计模式，标准库， 
和跨语言翻译最佳实践。

我将为您提供一个要翻译的代码片段。执行翻译
使用以下结构化流程：

---

📋 步骤 1 — 翻译简介
在分析或翻译之前，先确认翻译范围：

- 📌 源语言：[语言 + 版本，例如 Python 3.11]
- 🎯 目标语言：[语言 + 版本，例如 JavaScript ES2023]
- 📦 源库：列出检测到的所有导入库/框架
- 🔄 目标等效项：确定的直接库/框架映射
- 🧩 代码类型：例如脚本/类/模块/API/实用程序
- 🎯 翻译目标：直接移植/惯用重写/特定于框架
- ⚠️版本警告：需要预先了解的任何目标版本限制

---

🔍 第 2 步 — 源代码分析
翻译前深入分析源码：

- 🎯 代码目的：代码的总体用途
- ⚙️ 关键组件：确定的函数、类、模块
- 🌿 逻辑流程：核心逻辑路径和控制流程
- 📥 输入/输出：数据类型、结构、返回值
- 🔌 外部部门：检测到库、API、数据库、文件 I/O
- 🧩 使用的范式：OOP、函数式、异步、装饰器等。
- 💡 源习语：需要特殊的语言特定模式 
                         翻译时注意

---

⚠️ 第 3 步 — 翻译挑战地图
在翻译之前，确定并绘制每个挑战：

库和框架等效项：
| ＃|源库/函数 |目标当量|笔记|
|---|------------------------|--------------------|--------|

范式转变：
| ＃|源模式|目标模式|复杂性 |笔记|
|---|---------------|----------------|------------|--------|

复杂性： 
- 🟢 [简单] — 存在直接等价物
- 🟡 [中等]— 需要重组
- 🔴 [复杂] — 需要大量重写

不可翻译的标志：
| ＃|来源特征 |问题 | Target 的最佳替代方案 |
|---|---------------|-------|----------------------------|

标记任何符合以下条件的内容：
- 在目标语言中没有直接对应的内容
- 运行时的行为不同（例如，空处理， 
  类型强制、内存管理）
- 需要特定于目标语言的解决方法
- 可能会对目标语言的性能产生不同的影响

---

🔄 第 4 步 — 并排翻译
对于步骤 2 中确定的每个关键逻辑块，显示：

[块名称 - 例如，数据处理函数]

来源（[语言]）：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A structured prompt for translating code between any two programming languages. Follows a analyze-map-translate flow with deep source code analysis, translation challenge mapping, library equivalent identification, paradigm shift handling, side-by-side key logic comparison, and a full idiomatic production-ready translation with a compatibility summary card.

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

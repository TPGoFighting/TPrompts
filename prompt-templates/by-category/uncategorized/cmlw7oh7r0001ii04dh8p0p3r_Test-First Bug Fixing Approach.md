# Test-First Bug Fixing Approach

**Description:** Guide to fixing bugs using a test-first approach, ensuring code reliability through systematic testing and implementation.

**Type:** TEXT
**Author:** ilker
**Created:** 2026-02-21T11:04:16.167Z
**Votes:** 1
**Views:** 0

**Tags:** development

## Prompt Content

```
I have a bug: ${bug}. Take a test-first approach: 1) Read the relevant source files and existing tests. 2) Write a failing test that reproduces the exact bug. 3) Run the test suite to confirm it fails. 4) Implement the minimal fix. 5) Re-run the full test suite. 6) If any test fails, analyze the failure, adjust the code, and re-run—repeat until ALL tests pass. 7) Then grep the codebase for related code paths that might have the same issue and add tests for those too. 8) Summarize every change made and why. Do not ask me questions—make reasonable assumptions and document them.
```

**Source:** https://prompts.chat/prompts/cmlw7oh7r0001ii04dh8p0p3r_test-first-bug-fixing-approach

## 中文翻译

### 标题
测试优先的错误修复方法

### 提示词内容

```
我有一个错误：${bug}。采取测试优先的方法：1）阅读相关源文件和现有测试。 2) 编写一个失败的测试来重现确切的错误。 3) 运行测试套件以确认其失败。 4) 实施最小修复。 5) 重新运行完整的测试套件。 6) 如果任何测试失败，请分析失败，调整代码，然后重新运行 - 重复直到所有测试通过。 7) 然后 grep 代码库以查找可能存在相同问题的相关代码路径，并为这些路径添加测试。 8) 总结所做的每项更改及其原因。不要问我问题——做出合理的假设并记录下来。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Guide to fixing bugs using a test-first approach, ensuring code reliability through systematic testing and implementation.

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
- `${bug}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

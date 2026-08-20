# Angular Directive Generator

**Description:** Generates fully working Angular structural or attribute directives from a plain English description, including selector, logic, inputs, host bindings, and usage example.

**Type:** TEXT
**Author:** SatishB15
**Created:** 2026-03-07T08:32:24.868Z
**Votes:** 0
**Views:** 0

**Category:** Web Development

## Prompt Content

```
You are an expert Angular developer. Generate a complete Angular directive based on the following description:

Directive Description: ${description}
Directive Type: [structural | attribute]
Selector Name: [e.g. appHighlight, *appIf]
Inputs needed: [list any @Input() properties]
Target element behavior: ${what_should_happen_to_the_host_element}

Generate:
1. The full directive TypeScript class with proper decorators
2. Any required imports
3. Host bindings or listeners if needed
4. A usage example in a template
5. A brief explanation of how it works

Use Angular 17+ standalone directive syntax. Follow Angular style guide conventions.
```

**Source:** https://prompts.chat/prompts/cmmg2f4840007ky046diw5elk_angular-directive-generator

## 中文翻译

### 标题
角度指令生成器

### 提示词内容

```
您是一位专业的 Angular 开发人员。根据以下描述生成完整的 Angular 指令：

指令说明：${description}
指令类型：[结构|属性]
选择器名称：[例如appHighlight, *appIf]
所需的输入：[列出所有 @Input() 属性]
目标元素行为：${what_should_happen_to_the_host_element}

生成：
1. 具有适当装饰器的完整指令 TypeScript 类
2. 任何需要的进口
3. 主机绑定或侦听器（如果需要）
4. 模板中的使用示例
5. 简要说明其工作原理

使用 Angular 17+ 独立指令语法。遵循 Angular 风格指南约定。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Generates fully working Angular structural or attribute directives from a plain English description, including selector, logic, inputs, host bindings, and usage example.

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
- `${description}`: 需要您填写
- `${what_should_happen_to_the_host_element}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

# 21st.dev component prompt

**Type:** TEXT
**Author:** fariasandreluiz
**Created:** 2026-06-08T13:24:30.537Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
You are given a task to integrate an existing React component in the codebase.

The codebase should support:
- shadcn project structure  
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles. 
If default path for components is not /components/ui, provide instructions on why it's important to create this folder
Copy-paste this component to /components/ui folder:

${21st.dev_component}

Implementation Guidelines
 1. Analyze the component structure and identify all required dependencies
 2. Review the component's argumens and state
 3. Identify any required context providers or hooks and install them
 4. Questions to Ask
 - What data/props will be passed to this component?
 - Are there any specific state management requirements?
 - Are there any required assets (images, icons, etc.)?
 - What is the expected responsive behavior?
 - What is the best place to use this component in the app?

Steps to integrate
 0. Copy paste all the code above in the correct directories
 1. Install external dependencies
 2. Fill image assets with Unsplash stock images you know exist
 3. Use lucide-react icons for svgs or logos if component requires them

```

**Source:** https://prompts.chat/prompts/cmq58sz480004i9046hdc9zkr_21stdev-component-prompt

## 中文翻译

### 标题
21st.dev 组件提示

### 提示词内容

```
您需要将现有的 React 组件集成到代码库中。

代码库应该支持：
- shadcn项目结构  
- 顺风CSS
- 打字稿

如果没有，请提供有关如何通过 shadcn CLI 设置项目、安装 Tailwind 或 Typescript 的说明。

确定组件和样式的默认路径。 
如果组件的默认路径不是 /components/ui，请提供有关创建此文件夹的重要性的说明
将此组件复制粘贴到 /components/ui 文件夹：

${21st.dev_component}

实施指南
 1. 分析组件结构并确定所有所需的依赖关系
 2. 检查组件的参数和状态
 3. 确定任何所需的上下文提供程序或挂钩并安装它们
 4. 要问的问题
 - 哪些数据/道具将传递给该组件？
 - 是否有任何具体的状态管理要求？
 - 是否有任何必需的资源（图像、图标等）？
 - 预期的响应行为是什么？
 - 在应用程序中使用此组件的最佳位置是什么？

整合步骤
 0. 将上面的所有代码复制粘贴到正确的目录中
 1.安装外部依赖
 2. 使用您知道存在的 Unsplash 库存图像填充图像资源
 3. 如果组件需要，请使用 lucide-react 图标作为 svgs 或徽标
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与21st.dev component prompt相关的任务。

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

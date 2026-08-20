# Next.js

**Description:** Next.js Taste

**Type:** TASTE
**Author:** arre-ankit
**Created:** 2026-03-03T18:23:38.781Z
**Votes:** 0
**Views:** 0

**Tags:** Frontend

**Category:** Coding

## Prompt Content

```
# Next.js
- Use minimal hook set for components: useState for state, useEffect for side effects, useCallback for memoized handlers, and useMemo for computed values. Confidence: 0.85
- Never make page.tsx a client component. All client-side logic lives in components under /components, and page.tsx stays a server component. Confidence: 0.85
- When persisting client-side state, use lazy initialization with localStorage. Confidence: 0.85
- Always use useRef for stable, non-reactive state, especially for DOM access, input focus, measuring elements, storing mutable values, and managing browser APIs without triggering re-renders. Confidence: 0.85
- Use sr-only classes for accessibility labels. Confidence: 0.85
- Always use shadcn/ui as the component system for Next.js projects. Confidence: 0.85
- When setting up shadcn/ui, ensure globals.css is properly configured with all required Tailwind directives and shadcn theme variables. Confidence: 0.70
- When a component grows beyond a single responsibility, break it into smaller subcomponents to keep each file focused and improve readability. Confidence: 0.85
- State itself should trigger persistence to keep side-effects predictable, centralized, and always in sync with the UI. Confidence: 0.85
- Derive new state from previous state using functional updates to avoid stale closures and ensure the most accurate version of state. Confidence: 0.85
```

**Source:** https://prompts.chat/prompts/cmmaxs1el0001l104sg8u4fdx_nextjs

## 中文翻译

### 标题
Next.js

### 提示词内容

```
# Next.js
- 对组件使用最小的钩子集：useState 用于状态，useEffect 用于副作用，useCallback 用于记忆处理程序，useMemo 用于计算值。置信度：0.85
- 切勿将 page.tsx 设为客户端组件。所有客户端逻辑都位于 /components 下的组件中，而 page.tsx 仍然是服务器组件。置信度：0.85
- 保留客户端状态时，使用 localStorage 的延迟初始化。置信度：0.85
- 始终使用 useRef 来实现稳定、非反应性状态，特别是对于 DOM 访问、输入焦点、测量元素、存储可变值以及管理浏览器 API 而不触发重新渲染。置信度：0.85
- 使用 sr-only 类作为辅助功能标签。置信度：0.85
- 始终使用 shadcn/ui 作为 Next.js 项目的组件系统。置信度：0.85
- 设置 shadcn/ui 时，确保使用所有必需的 Tailwind 指令和 shadcn 主题变量正确配置 globals.css。置信度：0.70
- 当组件超出单一职责时，将其分解为更小的子组件，以保持每个文件的重点并提高可读性。置信度：0.85
- 状态本身应该触发持久性，以保持副作用可预测、集中并始终与 UI 同步。置信度：0.85
- 使用功能更新从先前状态派生新状态，以避免过时的关闭并确保最准确的状态版本。置信度：0.85
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Next.js Taste

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

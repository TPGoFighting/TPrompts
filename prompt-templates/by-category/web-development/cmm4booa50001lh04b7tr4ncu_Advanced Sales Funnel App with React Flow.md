# Advanced Sales Funnel App with React Flow

**Description:** Develop a comprehensive sales funnel application using React Flow, focusing on production-ready features, mobile-first design, and coding best practices.

**Type:** TEXT
**Author:** amvicioushecs
**Created:** 2026-02-27T03:18:33.198Z
**Votes:** 0
**Views:** 0

**Tags:** React, Web Development, JavaScript, Frontend, Sales, Best Practices, Testing

**Category:** Web Development

## Prompt Content

```
Act as a Full-Stack Developer specialized in sales funnels. Your task is to build a production-ready sales funnel application using React Flow. Your application will:

- Initialize using Vite with a React template and integrate @xyflow/react for creating interactive, node-based visualizations.
- Develop production-ready features including lead capture, conversion tracking, and analytics integration.
- Ensure mobile-first design principles are applied to enhance user experience on all devices using responsive CSS and media queries.
- Implement best coding practices such as modular architecture, reusable components, and state management for scalability and maintainability.
- Conduct thorough testing using tools like Jest and React Testing Library to ensure code quality and functionality without relying on mock data.

Enhance user experience by:
- Designing a simple and intuitive user interface that maintains high-quality user interactions.
- Incorporating clean and organized UI utilizing elements such as dropdown menus and slide-in/out sidebars to improve navigation and accessibility.

Use the following setup to begin your project:

```javascript
pnpm create vite my-react-flow-app --template react
pnpm add @xyflow/react

import { useState, useCallback } from 'react';
import { ReactFlow, applyNodeChanges, applyEdgeChanges, addEdge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
 
const initialNodes = [
  { id: 'n1', position: { x: 0, y: 0 }, data: { label: 'Node 1' } },
  { id: 'n2', position: { x: 0, y: 100 }, data: { label: 'Node 2' } },
];
const initialEdges = [{ id: 'n1-n2', source: 'n1', target: 'n2' }];
 
export default function App() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);
 
  const onNodesChange = useCallback(
    (changes) => setNodes((nodesSnapshot) => applyNodeChanges(changes, nodesSnapshot)),
    [],
  );
  const onEdgesChange = useCallback(
    (changes) => setEdges((edgesSnapshot) => applyEdgeChanges(changes, edgesSnapshot)),
    [],
  );
  const onConnect = useCallback(
    (params) => setEdges((edgesSnapshot) => addEdge(params, edgesSnapshot)),
    [],
  );
 
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
      />
    </div>
  );
}
```
```

**Source:** https://prompts.chat/prompts/cmm4booa50001lh04b7tr4ncu_advanced-sales-funnel-app-with-react-flow

## 中文翻译

### 标题
具有 React Flow 的高级销售漏斗应用程序

### 提示词内容

```
担任专门研究销售渠道的全栈开发人员。您的任务是使用 React Flow 构建一个可投入生产的销售漏斗应用程序。您的申请将：

- 使用 Vite 和 React 模板进行初始化，并集成 @xyflow/react 以创建交互式、基于节点的可视化。
- 开发生产就绪的功能，包括潜在客户捕获、转化跟踪和分析集成。
- 确保应用移动优先设计原则，以使用响应式 CSS 和媒体查询增强所有设备上的用户体验。
- 实施最佳编码实践，例如模块化架构、可重用组件和状态管理，以实现可扩展性和可维护性。
- 使用 Jest 和 React 测试库等工具进行彻底的测试，以确保代码质量和功能，而不依赖于模拟数据。

通过以下方式增强用户体验：
- 设计简单直观的用户界面，保持高质量的用户交互。
- 利用下拉菜单和滑入/滑出侧边栏等元素，整合干净、有组织的用户界面，以改善导航和可​​访问性。

使用以下设置开始您的项目：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Develop a comprehensive sales funnel application using React Flow, focusing on production-ready features, mobile-first design, and coding best practices.

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

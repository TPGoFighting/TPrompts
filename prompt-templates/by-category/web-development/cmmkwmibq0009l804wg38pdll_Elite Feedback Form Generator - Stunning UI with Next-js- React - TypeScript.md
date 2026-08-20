# Elite Feedback Form Generator — Stunning UI with Next.js, React & TypeScript

**Description:** Transform your forms into visual masterpieces. This prompt turns AI into a senior developer to create forms in Next.js, React, and TypeScript. It includes micro-interactions, Framer Motion, glassmorphism, real-time validation, WCAG 2.1 accessibility, and mobile-first design. Fully customizable with 11 variables. Get pixel-perfect, production-ready components without spending hours designing. Ideal for developers seeking high visual standards and performance.

**Type:** TEXT
**Author:** easycoregamesnoctis
**Created:** 2026-03-10T17:49:02.918Z
**Votes:** 0
**Views:** 0

**Tags:** React, TypeScript, Frontend, coding, next.js, Accessibility, CSS, design

**Category:** Web Development

## Prompt Content

```
<role>
You are an elite senior frontend developer with exceptional artistic expertise and modern aesthetic sensibility. You deeply master Next.js, React, TypeScript, and other modern frontend technologies, combining technical excellence with sophisticated visual design.
</role>

<instructions>
You will create a feedback form that is a true visual masterpiece.

Follow these guidelines in order of priority:

1. VISUAL IDENTITY ANALYSIS
Examine the existing project carefully to extract:
- Primary and secondary color palette
- Typography and visual hierarchy
- Spacing patterns and grid system
- Animation and transition styles
- Characteristic visual elements
- Logo and its application

Reference material: `${path_or_description_of_existing_project}`

Reason: Maintaining consistency with the established visual identity is essential for creating a cohesive and professional brand experience.

2. COMPONENT ARCHITECTURE
Structure the form using modular, reusable React/Next.js components:
- Create atomic components for inputs, buttons, and cards
- Implement TypeScript with strong and complete typing
- Organize the folder structure professionally
- Ensure full responsiveness (mobile-first)

Target directory: `${target_folder_path}`

Reason: A well-structured architecture facilitates maintenance, testing, and scalability.

3. EXCEPTIONAL VISUAL DESIGN
Elevate the visual standard with:
- Smooth and meaningful micro-interactions on every element
- Fluid animations using Framer Motion or similar libraries
- Transitions between states (hover, focus, active, disabled)
- Immediate visual feedback for each user action
- Depth effects with subtle shadows and gradients
- Glassmorphism or other modern effects where appropriate

Design inspiration/references: `${design_references_or_urls}`

Reason: Well-executed interactive elements and animations create a memorable experience and demonstrate attention to detail.

4. INTERACTIVE AND REACTIVE ELEMENTS
Implement features that increase engagement:
- Real-time validation with elegant messages
- Visual progress indicators
- Animated and contextual loading states
- Success/error messages with smooth animations
- Informative tooltips where relevant
- Entry animations when the form appears on screen

Reason: Constant visual feedback keeps the user informed and confident during interaction.

5. LOGO INTEGRATION
Use the existing logo creatively:
- Logo location: `${logo_file_path}`
- Brand colors: `${primary_color}`, `${secondary_color}`
- Position it strategically in the layout
- Consider subtle logo animations (pulse, glow, etc.)
- Maintain brand visual integrity

Reason: The logo is a central element of the visual identity and should be highlighted with elegance.

6. OPTIMIZATION AND PERFORMANCE
Ensure visual richness does not compromise performance:
- Optimize animations for 60fps
- Lazy load resources where appropriate
- Code splitting for larger components
- Optimized images in modern formats

Reason: A visually impressive form that loads slowly damages the user experience.
</instructions>

<thinking>
Before starting to code, think step by step:

1. Analyze the existing project at `${path_or_description_of_existing_project}` and list specifically:
   - What colors are being used?
   - What is the typography style?
   - What types of animations already exist?
   - What is the general feel/mood of the design?

2. Plan the form structure:
   - Required fields: `${form_fields}` _(e.g. name, email, rating, message)_
   - How to organize them in a visually appealing way?
   - What flow makes the most sense for the user?

3. Choose libraries and tools:
   - Which animation library to use? (Framer Motion, React Spring, etc.)
   - Is a form library needed? (React Hook Form, Formik, etc.)
   - Which styling approach? `${styling_approach}` _(e.g. Tailwind, Styled Components, CSS Modules)_

4. Define states and interactions:
   - What visual states will each element have?
   - What visual feedback will each action generate?
   - How do animations connect with each other?

5. Verify that your solution:
   - Maintains consistency with the established visual identity
   - Is completely functional and responsive
   - Is well-typed in TypeScript
   - Follows React/Next.js best practices
</thinking>

<task>
Create a complete and functional feedback form that is a visual masterpiece, using Next.js, React, and TypeScript. The form must:

- Capture user feedback in an elegant and intuitive way
- Incorporate the project's visual identity (colors, typography, logo)
- Include animations and micro-interactions on all interactive elements
- Be fully responsive and accessible
- Demonstrate technical and artistic excellence in every detail
- Submit data to: `${api_endpoint_or_action}` _(e.g. /api/feedback or a server action)_

Provide complete, organized code ready to be integrated into the system.
</task>

<constraints>
- Maintain absolute fidelity to the established visual identity
- Ensure accessibility (WCAG 2.1 AA minimum)
- Code must be production-ready, not a prototype
- All animations must be smooth (60fps)
- The form must work perfectly on mobile, tablet, and desktop
- Package manager: `${package_manager}` _(e.g. npm, pnpm, yarn)_
- Node version: `${node_version}` _(optional)_
</constraints>

<output_format>
Structure your response as follows:

1. VISUAL ANALYSIS
Briefly describe the visual elements identified in the existing project that you will use as reference.

2. FILE STRUCTURE
List the folder and file structure you will create.
</output_format>

```

**Source:** https://prompts.chat/prompts/cmmkwmibq0009l804wg38pdll_elite-feedback-form-generator-stunning-ui-with-nextjs-react-typescript

## 中文翻译

### 标题
Elite Feedback Form Generator — 使用 Next.js、React 和 TypeScript 打造令人惊叹的 UI

### 提示词内容

```
<角色>
您是一位精英高级前端开发人员，具有卓越的艺术专业知识和现代审美敏感性。您将深入掌握 Next.js、React、TypeScript 和其他现代前端技术，将卓越的技术与复杂的视觉设计相结合。 </角色>

<说明>
您将创建一个真正的视觉杰作的反馈表。按优先顺序遵循以下准则：

1.视觉识别分析
仔细检查现有项目以提取：
- 主要和次要调色板
- 版式和视觉层次结构
- 间距图案和网格系统
- 动画和过渡风格
- 特色视觉元素
- 标志及其应用

参考资料：`${path_or_description_of_existing_project}`

原因：保持与既定视觉识别的一致性对于创造有凝聚力和专业的品牌体验至关重要。 2. 组件架构
使用模块化、可重用的 React/Next.js 组件构建表单：
- 为输入、按钮和卡片创建原子组件
- 实现具有强大且完整的打字功能的 TypeScript
- 专业地组织文件夹结构
- 确保充分响应（移动优先）

目标目录：`${target_folder_path}`

原因：结构良好的架构有利于维护、测试和可扩展性。 3. 出色的视觉设计
通过以下方式提升视觉标准：
- 每个元素上的流畅且有意义的微交互
- 使用 Framer Motion 或类似库的流畅动画
- 状态之间的转换（悬停、焦点、活动、禁用）
- 每个用户操作的即时视觉反馈
- 具有微妙阴影和渐变的深度效果
- 玻璃形态或其他适当的现代效果

设计灵感/参考：`${design_references_or_urls}`

理由：执行良好的互动元素和动画创造了令人难忘的体验并表现出对细节的关注。 4. 交互和反应元素
实施可提高参与度的功能：
- 带有优雅消息的实时验证
- 视觉进度指示器
- 动画和上下文加载状态
- 带有流畅动画的成功/错误消息
- 相关的信息工具提示
- 表单出现在屏幕上时的输入动画

原因：持续的视觉反馈让用户在交互过程中了解情况并充满信心。 5. 标志整合
创造性地使用现有徽标：
- 徽标位置：`${logo_file_path}`
- 品牌颜色：`${primary_color}`、`${secondary_color}`
- 在布局中战略性地定位
- 考虑微妙的标志动画（脉冲、发光等）
- 保持品牌视觉完整性

原因：标志是视觉识别的核心元素，应该突出优雅。 6. 优化和性能
确保视觉丰富度不会影响性能：
- 优化 60fps 的动画
- 在适当的情况下延迟加载资源
- 较大组件的代码分割
- 现代格式的优化图像

原因：加载缓慢的视觉效果令人印象深刻的表单会损害用户体验。 </说明>

<思考>
在开始编码之前，请逐步思考：

1. 分析`${path_or_description_of_existing_project}`处的现有项目，具体列出：
   - 使用什么颜色？ - 排版风格是什么？ - 已有哪些类型的动画？ - 设计的总体感觉/情绪是什么？ 2.规划表单结构：
   - 必填字段：`${form_fields}`_（例如姓名、电子邮件、评级、消息）_
   - 如何以视觉上吸引人的方式组织它们？ - 什么流程对用户最有意义？ 3. 选择库和工具：
   - 使用哪个动画库？ （Framer Motion、React Spring 等）
   - 需要表单库吗？ （React Hook Form、Formik 等）
   - 哪种造型方法？ `${styling_approach}` _（例如 Tailwind、样式化组件、CSS 模块）_

4. 定义状态和交互：
   - 每个元素将具有什么视觉状态？ - 每个动作会产生什么视觉反馈？ - 动画如何相互关联？ 5. 验证您的解决方案：
   - 与既定的视觉识别保持一致
   - 功能齐全且反应灵敏
   - 在 TypeScript 中输入良好
   - 遵循 React/Next.js 最佳实践
</思考>

<任务>
使用 Next.js、React 和 TypeScript 创建一个完整且实用的反馈表单，这是一个视觉杰作。 该表格必须：

- 以优雅直观的方式捕获用户反馈
- 纳入项目的视觉识别（颜色、版式、徽标）
- 在所有交互元素上包括动画和微交互
- 充分响应并易于访问
- 在每一个细节上展现卓越的技术和艺术
- 将数据提交到：`${api_endpoint_or_action}`_（例如/api/feedback或服务器操作）_

提供完整、有组织的代码，以便集成到系统中。 </任务>

<约束>
- 保持对既定视觉识别的绝对忠诚
- 确保可访问性（最低 WCAG 2.1 AA）
- 代码必须是生产就绪的，而不是原型
- 所有动画必须流畅（60fps）
- 该表格必须在移动设备、平板电脑和台式机上完美运行
- 包管理器：`${package_manager}` _（例如 npm、pnpm、yarn）_
- 节点版本：`${node_version}`_（可选）_
</约束>

<输出格式>
您的回复结构如下：

1. 目视分析
简要描述现有项目中确定的视觉元素，您将用作参考。 2. 文件结构
列出您将创建的文件夹和文件结构。 </输出格式>
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Transform your forms into visual masterpieces. This prompt turns AI into a senior developer to create forms in Next.js, React, and TypeScript. It includes micro-interactions, Framer Motion, glassmorphism, real-time validation, WCAG 2.1 accessibility, and mobile-first design. Fully customizable with 11 variables. Get pixel-perfect, production-ready components without spending hours designing. Ideal for developers seeking high visual standards and performance.

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
- `${path_or_description_of_existing_project}`: 需要您填写
- `${target_folder_path}`: 需要您填写
- `${design_references_or_urls}`: 需要您填写
- `${logo_file_path}`: 需要您填写
- `${primary_color}`: 需要您填写
- `${secondary_color}`: 需要您填写
- `${path_or_description_of_existing_project}`: 需要您填写
- `${form_fields}`: 需要您填写
- `${styling_approach}`: 需要您填写
- `${api_endpoint_or_action}`: 需要您填写
- `${package_manager}`: 需要您填写
- `${node_version}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

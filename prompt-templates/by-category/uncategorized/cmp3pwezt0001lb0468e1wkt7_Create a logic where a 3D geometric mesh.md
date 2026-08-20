# Create a logic where a 3D geometric mesh

**Description:** Create a logic where a 3D geometric mesh (e.g., a torus or a custom GLTF model) dissolves into a cloud of thousands of interactive particles and reassembles into a different shape.

**Type:** TEXT
**Author:** loshu2000
**Created:** 2026-05-13T07:07:49.866Z
**Votes:** 0
**Views:** 0

**Tags:** OpenAI

## Prompt Content

```
I want you to act as a 3D Particle Effects Engineer specializing in kinetic typography and mesh-to-particle morphing. Your goal is to design a sophisticated WebGL-based transition system.

Core Task: Create a logic where a 3D geometric mesh (e.g., a torus or a custom GLTF model) dissolves into a cloud of thousands of interactive particles and reassembles into a different shape.

Technical Requirements:

Implement an FBO (Frame Buffer Object) to store and update particle positions on the GPU for high performance.

Use GPGPU techniques to calculate attraction and repulsion forces between particles and their target "anchor points" in the destination mesh.

Add a "Noise Turbulence" field using 3D Perlin or Simplex noise to create organic movement during the transition phase.

Ensure particles have dynamic color gradients based on their velocity or distance from the center.

Provide a clear explanation of how to map vertex data from a 3D model into a particle attribute buffer.

Please output the conceptual Shader logic and the core JavaScript implementation using Three.js.
```

**Source:** https://prompts.chat/prompts/cmp3pwezt0001lb0468e1wkt7_create-a-logic-where-a-3d-geometric-mesh

## 中文翻译

### 标题
创建 3D 几何网格的逻辑

### 提示词内容

```
我希望您担任 3D 粒子效果工程师，专门从事动态排版和网格到粒子变形。您的目标是设计一个复杂的基于 WebGL 的转换系统。

核心任务：创建一个逻辑，其中 3D 几何网格（例如，环面或自定义 GLTF 模型）溶解成数千个交互式粒子的云，并重新组装成不同的形状。

技术要求：

实现 FBO（帧缓冲区对象）来存储和更新 GPU 上的粒子位置，以实现高性能。

使用 GPGPU 技术计算粒子与其目标网格中的目标“锚点”之间的吸引力和排斥力。

使用 3D Perlin 或 Simplex 噪声添加“噪声湍流”字段，以在过渡阶段创建有机运动。

确保粒子根据其速度或距中心的距离具有动态颜色渐变。

清晰解释如何将 3D 模型中的顶点数据映射到粒子属性缓冲区中。

请使用 Three.js 输出概念 Shader 逻辑和核心 JavaScript 实现。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Create a logic where a 3D geometric mesh (e.g., a torus or a custom GLTF model) dissolves into a cloud of thousands of interactive particles and reassembles into a different shape.

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

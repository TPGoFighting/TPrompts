# Cyber-Pulse: 3D Neon Particle Swarm

**Description:** A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.

**Type:** TEXT
**Author:** loshu2000
**Created:** 2026-04-23T22:46:32.290Z
**Votes:** 0
**Views:** 0

**Tags:** OpenAI

**Category:** Coding

## Prompt Content

```
Game Concept: A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.
Technical Prompt:
Create a Three.js scene featuring a Points system with 15,000 particles. Use a custom ShaderMaterial for a glow effect. Implement a repulsion logic where particles fly away from the mouse cursor.

JavaScript
// Core repulsion math
let dist = particlePos.distanceTo(mousePos);
if (dist < 5) {
  direction.subVectors(particlePos, mousePos).normalize();
  particlePos.addScaledVector(direction, 0.2);
}
Include a BloomPass for post-processing and ensure 60FPS performance via
```

**Source:** https://prompts.chat/prompts/cmoc2mkbm0001jr04k3z0vxrc_cyber-pulse-3d-neon-particle-swarm

## 中文翻译

### 标题
Cyber​​-Pulse：3D 霓虹粒子群

### 提示词内容

```
游戏概念：以数字空间为背景的快节奏街机“躲避游戏”。玩家控制核心能量火花，穿过由 10,000 多个蓝色和紫色粒子组成的流体状星云，这些粒子会对玩家的存在做出反应。
技术提示：
创建一个具有包含 15,000 个粒子的点系统的 Three.js 场景。使用自定义 ShaderMaterial 实现发光效果。实现粒子飞离鼠标光标的斥力逻辑。

JavaScript
// 核心斥力数学
让 dist = molecularPos.distanceTo(mousePos);
如果（距离 < 5）{
  Direction.subVectors(articlePos, mousePos).normalize();
  粒子Pos.addScaledVector（方向，0.2）；
}
包括用于后处理的 BloomPass 并通过以下方式确保 60FPS 性能
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.

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

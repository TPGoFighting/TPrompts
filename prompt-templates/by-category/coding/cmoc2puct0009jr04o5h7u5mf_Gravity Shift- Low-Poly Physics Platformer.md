# Gravity Shift: Low-Poly Physics Platformer

**Description:** A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth. The environment is minimalist, using pastel gradients and sharp geometric shapes.

**Type:** TEXT
**Author:** loshu2000
**Created:** 2026-04-23T22:49:05.262Z
**Votes:** 0
**Views:** 0

**Tags:** Games

**Category:** Coding

## Prompt Content

```
Game Concept: A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth. The environment is minimalist, using pastel gradients and sharp geometric shapes.
Technical Prompt:
Build a 3D platformer using Three.js and Cannon.js. The world is a cube-shaped maze. When the user presses 'R', rotate the world.gravity vector by 90 degrees.

JavaScript
// Gravity rotation logic
world.gravity.set(0, -9.82, 0); // Default
function rotateGravity() {
  let newG = new CANNON.Vec3(-world.gravity.y, world.gravity.x, 0);
  world.gravity.copy(newG);
}
Include smooth camera interpolation using Lerp to follow the player's rigid body during shifts.
```

**Source:** https://prompts.chat/prompts/cmoc2puct0009jr04o5h7u5mf_gravity-shift-low-poly-physics-platformer

## 中文翻译

### 标题
重力转移：低多边形物理平台游戏

### 提示词内容

```
游戏概念：一款名为“Gravity Shift”的解谜平台游戏，玩家可以旋转整个世界来探索 3D 低多边形迷宫。环境简约，采用柔和的渐变和锐利的几何形状。
技术提示：
使用 Three.js 和 Cannon.js 构建 3D 平台游戏。世界是一个立方体形状的迷宫。当用户按下“R”时，将 world.gravity 向量旋转 90 度。

JavaScript
// 重力旋转逻辑
world.gravity.set(0, -9.82, 0); // 默认
函数旋转重力（）{
  let newG = new CANNON.Vec3(-world.gravity.y, world.gravity.x, 0);
  world.gravity.copy(newG);
}
包括使用 Lerp 进行平滑摄像机插值，以在轮班期间跟随玩家的刚体。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth. The environment is minimalist, using pastel gradients and sharp geometric shapes.

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

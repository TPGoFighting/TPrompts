# 3D to 2D Floor Plan Converter

**Description:** Convert a furnished 3D interior render into a detailed and precise 2D architectural floor plan. Ideal for real estate listings or construction documents, this tool offers a clean vector-style blueprint with clearly defined rooms and spaces.

**Type:** IMAGE
**Author:** gunebak4n
**Created:** 2025-12-30T21:56:29.041Z
**Votes:** 0
**Views:** 0

**Tags:** Interior Design, Computer Vision

**Category:** Image Generation

## Prompt Content

```
{
  "task": "image_to_image",
  "description": "Convert a furnished 3D interior render into a clean 2D architectural floor plan drawing",
  "input_image": "3d_render_of_apartment_interior.png",
  "prompt": "top-down 2D architectural floor plan, black and white technical drawing, clean vector-style lines, precise wall thickness, clearly defined rooms, labeled spaces with room names and square meter areas, doors with swing arcs, windows shown as breaks in walls, minimal shading, no perspective, orthographic projection, architectural blueprint style, professional residential floor plan, similar to CAD drawing",
  "negative_prompt": "3d perspective, isometric view, realistic lighting, shadows, textures, furniture rendering, people, depth, photorealism, colors, gradients, soft edges, artistic sketch, hand drawn style",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 30,
    "cfg_scale": 7,
    "denoising_strength": 0.65,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "flat 2D floor plan similar to architectural plan drawings, suitable for real estate listings or construction documents"
}

```

**Source:** https://prompts.chat/prompts/cmjt4n3000001ky04k1pv255w_3d-to-2d-floor-plan-converter

## 中文翻译

### 标题
3D 到 2D 平面图转换器

### 提示词内容

```
{
  “任务”：“图像到图像”，
  "description": "将带家具的 3D 室内渲染转换为干净的 2D 建筑平面图",
  "input_image": "3d_render_of_apartment_interior.png",
  "prompt": "自上而下的 2D 建筑平面图，黑白技术图，干净的矢量风格线条，精确的墙厚，明确定义的房间，带有房间名称和平方米面积的标记空间，带有摆动弧线的门，显示为墙壁断裂的窗户，最小阴影，无透视，正投影，建筑蓝图风格，专业住宅平面图，类似于 CAD 绘图",
  "negative_prompt": "3d 透视、等轴测视图、真实照明、阴影、纹理、家具渲染、人物、深度、照片写实、颜色、渐变、软边、艺术素描、手绘风格",
  “设置”：{
    “型号”：“sdxl”，
    “采样器”：“DPM++ 2M Karras”，
    “步骤”：30，
    “cfg_scale”：7，
    “去噪强度”：0.65，
    “分辨率”：{
      “宽度”：1024，
      “高度”：1024
    }
  },
  "output_expectation": "类似于建筑平面图的平面二维平面图，适用于房地产清单或施工文件"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Convert a furnished 3D interior render into a detailed and precise 2D architectural floor plan. Ideal for real estate listings or construction documents, this tool offers a clean vector-style blueprint with clearly defined rooms and spaces.

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

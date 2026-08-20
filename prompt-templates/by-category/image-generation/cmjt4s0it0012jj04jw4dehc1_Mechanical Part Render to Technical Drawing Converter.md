# Mechanical Part Render to Technical Drawing Converter

**Description:** Convert a 3D mechanical part render into a precise and fully dimensioned technical drawing suitable for manufacturing documentation, adhering to ISO mechanical drafting standards.

**Type:** IMAGE
**Author:** gunebak4n
**Created:** 2025-12-30T22:00:19.109Z
**Votes:** 0
**Views:** 0

**Tags:** AI Tools, Data Science, Machine Learning, Computer Vision

**Category:** Image Generation

## Prompt Content

```
{
  "task": "image_to_image",
  "description": "Convert a 3D mechanical part render into a fully dimensioned manufacturing drawing",
  "input_image": "3d_render_of_pipe_or_mechanical_part.png",
  "prompt": "mechanical engineering drawing, multi-view orthographic projection, front view, top view, side view and section view, fully dimensioned technical drawing, precise numeric measurements in millimeters, diameter symbols, radius annotations, hole count notation, center lines, section hatching, consistent line weights, ISO mechanical drafting standard, black ink on white background, manufacturing-ready documentation",
  "negative_prompt": "artistic style, perspective view, soft shading, textures, realistic lighting, colors, decorative rendering, sketch, hand-drawn look, incomplete dimensions",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 40,
    "cfg_scale": 6,
    "denoising_strength": 0.5,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "ISO-style mechanical drawing with clear dimensions suitable for CNC, casting, or fabrication reference"
}

```

**Source:** https://prompts.chat/prompts/cmjt4s0it0012jj04jw4dehc1_mechanical-part-render-to-technical-drawing-converter

## 中文翻译

### 标题
机械零件渲染到技术绘图转换器

### 提示词内容

```
{
  “任务”：“图像到图像”，
  "description": "将 3D 机械零件渲染转换为完整尺寸的制造图纸",
  "input_image": "3d_render_of_pipe_or_mechanical_part.png",
  "prompt": "机械工程图、多视图正投影、前视图、俯视图、侧视图和剖面图、全尺寸技术图纸、以毫米为单位的精确数字测量、直径符号、半径注释、孔计数符号、中心线、剖面剖面线、一致的线宽、ISO 机械绘图标准、白底黑墨、制造就绪文档",
  "negative_prompt": "艺术风格、透视图、柔和的阴影、纹理、逼真的灯光、颜色、装饰渲染、草图、手绘外观、不完整的尺寸",
  “设置”：{
    “型号”：“sdxl”，
    “采样器”：“DPM++ 2M Karras”，
    “步骤”：40，
    “cfg_scale”：6，
    “去噪强度”：0.5，
    “分辨率”：{
      “宽度”：1024，
      “高度”：1024
    }
  },
  "output_expectation": "ISO 风格的机械绘图，具有清晰的尺寸，适合 CNC、铸造或制造参考"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Convert a 3D mechanical part render into a precise and fully dimensioned technical drawing suitable for manufacturing documentation, adhering to ISO mechanical drafting standards.

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

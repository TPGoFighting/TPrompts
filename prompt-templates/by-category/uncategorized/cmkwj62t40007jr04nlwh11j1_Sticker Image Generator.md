# Sticker Image Generator

**Description:** Generate a colorful sticker image with a transparent background, customizable text and icon, similar to Stickermule style.

**Type:** IMAGE
**Author:** f
**Created:** 2026-01-27T11:46:10.745Z
**Votes:** 3
**Views:** 0

**Tags:** creative, design

## Prompt Content

```
{
  "role": "Image Designer",
  "task": "Create a detailed sticker image with a transparent background.",
  "style": "Colorful, vibrant, similar to Stickermule",
  "variables": {
    "text": "Custom text for the sticker",
    "icon": "Icon to be included in the sticker",
    "colorPalette": "Color palette to be used for the sticker"
  },
  "constraints": [
    "Must have a transparent background",
    "Should be colorful and vibrant",
    "Text should be readable regardless of the background",
    "Icon should complement the text style"
  ],
  "output_format": "PNG",
  "examples": [
    {
      "text": "${text:Hello World}",
      "icon": "${icon:smiley_face}",
      "colorPalette": "${colorPalette:vibrant}",
      "result": "A colorful sticker with '${text:Hello World}' text and a ${icon:smiley_face} icon using a ${colorPalette:vibrant} color palette. It's an image of ${details}"
    }
  ],
  "details": {
    "resolution": "300 DPI",
    "dimensions": "1024x1024 pixels",
    "layers": "Text and icon should be on separate layers for easy editing"
  }
}
```

**Source:** https://prompts.chat/prompts/cmkwj62t40007jr04nlwh11j1_sticker-image-generator

## 中文翻译

### 标题
贴纸图像生成器

### 提示词内容

```
{
  "role": "形象设计师",
  "task": "创建具有透明背景的详细贴纸图像。",
  "style": "色彩缤纷，充满活力，类似于 Stickermule",
  “变量”：{
    "text": "贴纸的自定义文本",
    "icon": "要包含在贴纸中的图标",
    "colorPalette": "贴纸使用的调色板"
  },
  “约束”：[
    “必须有透明背景”，
    “应该是色彩缤纷、充满活力的”，
    “无论背景如何，文本都应该可读”，
    “图标应该与文字风格相辅相成”
  ],
  “输出格式”：“PNG”，
  “例子”：[
    {
      "text": "${text:Hello World}",
      "图标": "${icon:smiley_face}",
      "colorPalette": "${colorPalette:vibrant}",
      "result": "带有 '${text:Hello World}' 文本和 ${icon:smiley_face} 图标的彩色贴纸，使用 ${colorPalette:vibrant} 调色板。这是 ${details} 的图像"
    }
  ],
  “详细信息”：{
    “分辨率”：“300 DPI”，
    “尺寸”：“1024x1024 像素”，
    "layers": "文本和图标应位于单独的图层上，以便于编辑"
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Generate a colorful sticker image with a transparent background, customizable text and icon, similar to Stickermule style.

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
- `${text}`: 可自定义（默认值: Hello World）
- `${icon}`: 可自定义（默认值: smiley_face）
- `${colorPalette}`: 可自定义（默认值: vibrant）
- `${text}`: 可自定义（默认值: Hello World）
- `${icon}`: 可自定义（默认值: smiley_face）
- `${colorPalette}`: 可自定义（默认值: vibrant）
- `${details}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

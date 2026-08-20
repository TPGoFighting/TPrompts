# 3D Medical Anatomy Model Render Prompt

**Description:** Create a photorealistic 3D medical anatomy model render with customizable features including gender, view angle, target muscle group, and highlight color. The prompt ensures a wide-angle, full-body shot with a clean, seamless background and a focus on scientific accuracy and detailed textures.

**Type:** IMAGE
**Author:** cem
**Created:** 2026-01-01T19:25:59.333Z
**Votes:** 3
**Views:** 0

**Tags:** Art, Computer Vision, Fitness, Health, Science

**Category:** Image Generation

## Prompt Content

```
{
  "fixed_prompt_components": {
    "composition": "Wide angle full body shot, the entire figure is visible from head to toe, far shot, vertical portrait framing, centered and symmetrical stance",
    "background": "Isolated on a seamless pure white background, studio backdrop, clean white environment",
    "art_style": "Photorealistic 3D medical render, ZBrush digital sculpture style, scientific anatomy model aesthetics",
    "texture_and_material": "Monochromatic silver-grey skin with brushed metal texture, micro-surface details, highly detailed muscle striation, matte finish",
    "lighting_and_tech": "Cinematic rim lighting, global illumination, raytracing, ambient occlusion, 8k resolution, UHD, sharp focus, hyper-detailed"
  },
  "variables": {
    "gender": "${gender:male}",
    "view_angle": "${view_angle:Front view}",
    "target_muscle_group": "${target_muscle_group:Pectoralis Major (Chest)}",
    "highlight_color": "${highlight_color:glowing cyan blue}"
  },
  "negative_prompt": "text, infographic, chart, diagram, labels, arrows, UI, cropped image, close-up, macro shot, headshot, cut off feet, cut off head, partial body, grey background, gradient background, shadows on floor, blurry, low resolution, distortion, watermark"
}
```

**Source:** https://prompts.chat/prompts/cmjvu58yt0007l4048mf50kst_3d-medical-anatomy-model-render-prompt

## 中文翻译

### 标题
3D 医学解剖模型渲染提示

### 提示词内容

```
{
  “固定提示组件”：{
    "构图": "广角全身拍，整个人物从头到脚清晰可见，远景，垂直人像取景，站姿居中对称",
    "background": "隔离在无缝的纯白色背景、工作室背景、干净的白色环境上",
    "art_style": "真实感3D医学渲染，ZBrush数字雕塑风格，科学解剖模型美学",
    "texture_and_material": "单色银灰色皮肤，拉丝金属质感，微表面细节，高度细致的肌肉条纹，哑光效果",
    "lighting_and_tech": "电影边缘照明、全局照明、光线追踪、环境光遮挡、8k 分辨率、超高清、锐焦、超细节"
  },
  “变量”：{
    "性别": "${性别:男}",
    "view_angle": "${view_angle:前视图}",
    "target_muscle_group": "${target_muscle_group:胸大肌（胸部）}",
    "highlight_color": "${highlight_color:发光青蓝色}"
  },
  "negative_prompt": "文本、信息图、图表、图表、标签、箭头、UI、裁剪图像、特写、微距拍摄、爆头、截脚、截头、部分身体、灰色背景、渐变背景、地板阴影、模糊、低分辨率、失真、水印"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Create a photorealistic 3D medical anatomy model render with customizable features including gender, view angle, target muscle group, and highlight color. The prompt ensures a wide-angle, full-body shot with a clean, seamless background and a focus on scientific accuracy and detailed textures.

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
- `${gender}`: 可自定义（默认值: male）
- `${view_angle}`: 可自定义（默认值: Front view）
- `${target_muscle_group}`: 可自定义（默认值: Pectoralis Major (Chest)）
- `${highlight_color}`: 可自定义（默认值: glowing cyan blue）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

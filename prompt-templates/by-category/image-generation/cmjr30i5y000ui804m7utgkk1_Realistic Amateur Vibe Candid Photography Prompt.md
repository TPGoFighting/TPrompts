# Realistic Amateur Vibe Candid Photography Prompt

**Description:** This prompt generates a realistic amateur vibe candid photograph with specific technical attributes such as natural skin texture, handheld micro-blur, and casual postures using iPhone 11 settings. It aims to create an authentic, everyday snapshot feel with minimal retouching and natural imperfections.

**Type:** TEXT
**Author:** beatstobytes
**Created:** 2025-12-29T11:35:23.638Z
**Votes:** 0
**Views:** 0

**Category:** Image Generation

## Prompt Content

```
{
  "prompt": "instagirl, candid phone snapshot, realistic amateur vibe, natural skin texture, light makeup at most, handheld micro-blur, iPhone 11 wide 26mm EXIF look, f/1.8, 1/60s, ISO 200, slight lens distortion, casual posture, everyday outfit, mild flyaway hair, imperfect framing, background clutter present, no retouching, realistic shadows, faithful anatomy, same person identity, same body proportions",
  "negative_prompt": "beauty filter, skin smoothing, studio glam, hdr glow, cinematic grading, fashion editorial, airbrush, liquify, body morph, face changed, de-aged, uncanny valley, extra fingers, warped limbs, NSFW, lingerie, bikini, watermark, text, logo, border",
  "image": "<REFERENCE_IMAGE_URL>",
  "strength": 0.35,
  "guidance": 5.0,
  "control_nets": [
    {
      "type": "openpose",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.7,
      "guess_mode": false
    },
    {
      "type": "depth",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.45
    }
  ],
  "face_lock": {
    "type": "ip_adapter_faceid",
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    "weight": 0.75
  }
}
```

**Source:** https://prompts.chat/prompts/cmjr30i5y000ui804m7utgkk1_realistic-amateur-vibe-candid-photography-prompt

## 中文翻译

### 标题
逼真的业余氛围坦率摄影提示

### 提示词内容

```
{
  "prompt": "instagirl、偷拍手机快照、真实业余氛围、自然肤质、淡妆至多、手持微模糊、iPhone 11 宽幅 26mm EXIF 外观、f/1.8、1/60s、ISO 200、轻微镜头畸变、休闲姿势、日常服装、轻微飞扬的头发、不完美的取景、背景杂乱、无修饰、逼真的阴影、忠实的解剖结构、同一个人身份、同一身体比例”，
  "negative_prompt": "美容滤镜、皮肤平滑、工作室魅力、hdr 发光、电影分级、时尚社论、喷枪、液化、身体变形、变脸、去衰老、恐怖谷、额外的手指、扭曲的四肢、NSFW、内衣、比基尼、水印、文本、徽标、边框",
  “图像”：“<REFERENCE_IMAGE_URL>”，
  “强度”：0.35，
  “指导”：5.0，
  “控制网”：[
    {
      “类型”：“开放姿势”，
      “图像”：“<REFERENCE_IMAGE_URL>”，
      “重量”：0.7，
      “猜测模式”：假
    },
    {
      “类型”：“深度”，
      “图像”：“<REFERENCE_IMAGE_URL>”，
      “重量”：0.45
    }
  ],
  “面部锁定”：{
    “类型”：“ip_adapter_faceid”，
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    “重量”：0.75
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。This prompt generates a realistic amateur vibe candid photograph with specific technical attributes such as natural skin texture, handheld micro-blur, and casual postures using iPhone 11 settings. It aims to create an authentic, everyday snapshot feel with minimal retouching and natural imperfections.

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

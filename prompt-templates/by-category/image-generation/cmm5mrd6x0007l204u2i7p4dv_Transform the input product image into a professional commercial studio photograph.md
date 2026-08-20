# Transform the input product image into a professional commercial studio photograph

**Description:** Transform the input product image into a professional commercial studio photograph while preserving the exact product identity, geometry, proportions, stitching, texture, and material properties.


**Type:** IMAGE
**Author:** ayoubelouardi3710
**Created:** 2026-02-28T01:16:20.745Z
**Votes:** 2
**Views:** 0

**Tags:** Nano Banana, image-prompt, image-generation

**Category:** Image Generation

## Prompt Content

```
{
  "model": "nano-banana",
  "task": "image_to_image_product_enhancement",
  "objective": "Transform the input product image into a professional commercial studio photograph while preserving the exact product identity, geometry, proportions, stitching, texture, and material properties.",
  "input": {
    "type": "image",
    "preserve_identity": true,
    "preserve_geometry": true,
    "preserve_texture": true,
    "preserve_color": true,
    "preserve_material": true
  },
  "scene": {
    "background": {
      "type": "solid",
      "color": "#FFFFFF",
      "pure_white": true,
      "uniform": true,
      "no_gradient": true,
      "no_texture": true
    },
    "environment": "professional commercial photography studio",
    "surface": "invisible or pure white seamless sweep"
  },
  "lighting": {
    "style": "soft studio lighting",
    "setup": "three_point_lighting",
    "key_light": {
      "type": "softbox",
      "position": "front-left",
      "intensity": "medium",
      "softness": "high"
    },
    "fill_light": {
      "type": "softbox",
      "position": "front-right",
      "intensity": "low",
      "softness": "high"
    },
    "rim_light": {
      "type": "softbox",
      "position": "rear",
      "intensity": "low",
      "purpose": "edge separation and clean outline"
    },
    "shadow": {
      "type": "contact_shadow",
      "softness": "soft",
      "opacity": "low",
      "blur": "subtle",
      "direction": "natural",
      "realistic": true
    },
    "reflections": {
      "allowed": false
    }
  },
  "camera": {
    "angle": "front-facing or natural product angle",
    "alignment": "perfectly centered",
    "lens": "85mm equivalent",
    "distortion": "none",
    "focus": "tack sharp across entire product",
    "depth_of_field": "moderate",
    "aperture": "f/8",
    "perspective": "natural and undistorted"
  },
  "composition": {
    "framing": "centered",
    "product_scale": "occupies 75-90% of frame",
    "orientation": "straight, upright, natural",
    "symmetry": "maintained if applicable",
    "clean_edges": true,
    "no_crop_of_product": true
  },
  "quality": {
    "resolution": "4096x4096",
    "definition": "ultra high definition",
    "sharpness": "maximum",
    "noise": "none",
    "grain": "none",
    "compression_artifacts": "none",
    "photorealism": "maximum",
    "commercial_quality": true,
    "catalog_ready": true,
    "ecommerce_ready": true
  },
  "color": {
    "profile": "sRGB",
    "accuracy": "true_to_original",
    "white_balance": "neutral studio",
    "exposure": "balanced",
    "contrast": "natural",
    "saturation": "accurate",
    "no_color_shift": true
  },
  "material_rendering": {
    "fabric_detail": "fully preserved",
    "texture_clarity": "high",
    "stitching_visibility": "clear",
    "edges": "clean and precise",
    "wrinkles": "natural and realistic",
    "no_fake_modifications": true
  },
  "constraints": {
    "do_not_modify_product_design": true,
    "do_not_change_shape": true,
    "do_not_add_or_remove_parts": true,
    "do_not_hallucinate_details": true,
    "do_not_stylize": true,
    "keep_product_exact": true
  },
  "negative_prompt": [
    "colored background",
    "gray background",
    "gradient background",
    "dirty background",
    "text",
    "logo",
    "watermark",
    "reflection floor",
    "extra objects",
    "props",
    "person",
    "hands",
    "model",
    "distortion",
    "warping",
    "blurry",
    "low resolution",
    "noise",
    "grain",
    "overexposed",
    "underexposed",
    "harsh shadows",
    "hard shadows",
    "inconsistent lighting",
    "fake texture",
    "hallucinated details"
  ],
  "output": {
    "format": "PNG",
    "background": "pure_white",
    "transparent_background": false,
    "ready_for": [
      "ecommerce",
      "catalog",
      "website",
      "advertising",
      "print"
    ]
  }
}
```

**Source:** https://prompts.chat/prompts/cmm5mrd6x0007l204u2i7p4dv_transform-the-input-product-image-into-a-professional-commercial-studio-photograph

## 中文翻译

### 标题
将输入的产品图片转换为专业的商业影楼照片

### 提示词内容

```
{
  “模型”：“纳米香蕉”，
  “任务”：“图像到图像产品增强”，
  "objective": "将输入的产品图像转换为专业的商业工作室照片，同时保留准确的产品身份、几何形状、比例、缝合、纹理和材料属性。",
  “输入”：{
    “类型”：“图像”，
    “保留身份”：正确，
    “保留几何”：正确，
    “preserve_texture”：正确，
    “保留颜色”：正确，
    “保留材料”：正确
  },
  “场景”：{
    “背景”：{
      “类型”：“固体”，
      “颜色”：“#FFFFFF”，
      “pure_white”：正确，
      “统一”：真实，
      “无梯度”：正确，
      “无纹理”：正确
    },
    “环境”：“专业商业摄影工作室”，
    “surface”：“隐形或纯白色无缝扫描”
  },
  “照明”：{
    "style": "柔和的演播室灯光",
    “设置”：“三点照明”，
    “键灯”：{
      “类型”：“柔光箱”，
      "position": "左前",
      “强度”：“中”，
      “柔软度”：“高”
    },
    “填充光”：{
      “类型”：“柔光箱”，
      "position": "右前",
      “强度”：“低”，
      “柔软度”：“高”
    },
    “边缘灯”：{
      “类型”：“柔光箱”，
      “位置”：“后”，
      “强度”：“低”，
      “目的”：“边缘分离和清晰的轮廓”
    },
    “阴影”：{
      “类型”：“contact_shadow”，
      “柔软度”：“柔软”，
      “不透明度”：“低”，
      “模糊”：“微妙”，
      “方向”：“自然”，
      “现实”：真实
    },
    “反思”：{
      “允许”：假
    }
  },
  “相机”：{
    "angle": "正面或自然产品角度",
    "alignment": "完全居中",
    "lens": "85mm 等效值",
    “扭曲”：“无”，
    “焦点”：“在整个产品中保持锐利”，
    "depth_of_field": "中等",
    “光圈”：“f/8”，
    “视角”：“自然且不扭曲”
  },
  “组成”：{
    “框架”：“居中”，
    "product_scale": "占据框架的 75-90%",
    "orientation": "笔直、正直、自然",
    "symmetry": "如果适用则保持",
    “clean_edges”：正确，
    “no_crop_of_product”：true
  },
  “质量”：{
    “分辨率”：“4096x4096”，
    "definition": "超高清",
    “清晰度”：“最大”，
    “噪音”：“无”，
    “谷物”：“无”，
    "compression_artifacts": "无",
    “照片写实主义”：“最大”，
    “商业质量”：正确，
    “catalog_ready”：正确，
    “ecommerce_ready”：正确
  },
  “颜色”：{
    “配置文件”：“sRGB”，
    “准确度”：“真实到原始”，
    "white_balance": "中性工作室",
    “曝光”：“平衡”，
    “对比度”：“自然”，
    “饱和度”：“准确”，
    “no_color_shift”：正确
  },
  “材质渲染”：{
    "fabric_detail": "完全保留",
    "texture_clarity": "高",
    "stitching_visibility": "清晰",
    “edges”：“干净、精确”，
    “皱纹”：“自然真实”，
    “no_fake_modifications”：正确
  },
  “约束”：{
    “do_not_modify_product_design”：正确，
    “do_not_change_shape”：正确，
    “do_not_add_or_remove_parts”：true，
    “do_not_hallucinate_details”：正确，
    “do_not_stylize”：正确，
    “keep_product_exact”：true
  },
  “否定提示”：[
    “彩色背景”，
    “灰色背景”，
    “渐变背景”，
    “肮脏的背景”，
    “文本”，
    “标志”，
    “水印”，
    “反射地板”，
    “额外的对象”，
    “道具”，
    “人”，
    “手”，
    “模型”，
    “扭曲”，
    “扭曲”，
    “模糊”，
    “低分辨率”，
    “噪音”，
    “谷物”，
    “曝光过度”，
    “曝光不足”，
    “严酷的阴影”，
    “硬阴影”，
    “照明不一致”，
    “假纹理”，
    “幻觉细节”
  ],
  “输出”：{
    “格式”：“PNG”，
    “背景”：“纯白色”，
    “透明背景”：假，
    “准备好”：[
      “电子商务”，
      “目录”，
      “网站”，
      “广告”，
      “打印”
    ]
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Transform the input product image into a professional commercial studio photograph while preserving the exact product identity, geometry, proportions, stitching, texture, and material properties.

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

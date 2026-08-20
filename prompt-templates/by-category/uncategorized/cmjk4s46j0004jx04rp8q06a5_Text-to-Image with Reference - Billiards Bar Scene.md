# Text-to-Image with Reference - Billiards Bar Scene

**Description:** Generate a photorealistic image of a young woman in a billiards bar using a reference photo to ensure identity preservation.

**Type:** TEXT
**Author:** cipeberre
**Created:** 2025-12-24T14:50:28.267Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
{
  "meta_data": {
    "task_type": "text_to_image_with_reference",
    "version": "v1.0",
    "priority": "high"
  },
  "technical_constraints": {
    "identity_preservation": {
      "enabled": true,
      "reference_mode": "strict",
      "parameters": {
        "use_reference_face_only": true,
        "identity_lock": true,
        "preserve_facial_features": true,
        "preserve_skin_texture": true,
        "avoid_face_morphing": true,
        "preservation_strength": 1.0
      }
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "resolution_target": "ultra_high_res",
      "render_engine_style": "photorealistic"
    }
  },
  "creative_prompt": {
    "scene": {
      "location": "dim billiards bar",
      "background": "dark ceiling, red-and-white wall stripe, a few tables/chairs in the back, low-light ambience with subtle film grain",
      "key_props": [
        "green-felt pool table (foreground)",
        "vintage red billiard lamps overhead (warm red glow)",
        "scattered billiard balls on the table",
        "pool cue (held by the subject)"
      ]
    },
    "subject": {
      "type": "young adult woman",
      "identity_instruction": "The subject must be 100% identical to the uploaded reference photo (same face, proportions, age, and identity). No identity drift.",
      "pose": "leaning against the pool table edge; one hand braced on the table; the other hand holding the cue stick vertically; hip slightly popped; head slightly tilted; gaze up and to the side",
      "expression": "cool, confident, subtly flirtatious",
      "wardrobe": {
        "top": "leopard-print corset/bustier top with straps",
        "bottom": "black mini skirt",
        "accessories": "minimal jewelry (small hoops or studs)"
      },
      "details": {
        "nails": "red nail polish",
        "hair": "long, voluminous, wavy hair",
        "makeup": "night-out glam: defined eyeliner/lashes, warm blush, nude-brown lips"
      }
    },
    "camera_and_lighting": {
      "shot_style": "realistic nightlife flash photo + ambient bar lighting",
      "camera": "full-frame DSLR",
      "lens": "35mm or 50mm",
      "aperture": "f/1.8",
      "shutter_speed": "1/80s",
      "iso": "800",
      "lighting": {
        "primary": "on-camera flash (crisp subject, natural falloff, realistic shadows)",
        "secondary": "overhead red lamps glow + dim ambient fill",
        "look": "high contrast, controlled specular highlights, no blown whites"
      },
      "color_grading": "warm reds with natural skin tones, subtle film grain",
      "focus": "tack-sharp eyes and face, shallow depth of field, soft background bokeh"
    }
  },
  "negative_prompt": [
    "different person",
    "identity change",
    "face morphing",
    "extra people",
    "extra limbs",
    "extra fingers",
    "bad hands",
    "deformed anatomy",
    "warped cue stick",
    "warped pool table",
    "text",
    "logo",
    "watermark",
    "cartoon",
    "anime",
    "illustration",
    "over-smoothed skin",
    "plastic skin",
    "low resolution",
    "blurred face",
    "overexposed flash highlights"
  ]
}
```

**Source:** https://prompts.chat/prompts/cmjk4s46j0004jx04rp8q06a5_text-to-image-with-reference-billiards-bar-scene

## 中文翻译

### 标题
文本到图像参考 - 台球酒吧场景

### 提示词内容

```
{
  “元数据”：{
    "task_type": "text_to_image_with_reference",
    “版本”：“v1.0”，
    “优先级”：“高”
  },
  “技术约束”：{
    “身份保存”：{
      “启用”：正确，
      "reference_mode": "严格",
      “参数”：{
        “use_reference_face_only”：true，
        “身份锁”：真，
        “preserve_facial_features”：正确，
        “preserve_skin_texture”：正确，
        “avoid_face_morphing”：正确，
        “保存强度”：1.0
      }
    },
    “输出设置”：{
      “纵横比”：“9:16”，
      "resolution_target": "ultra_high_res",
      "render_engine_style": "照片级真实感"
    }
  },
  “创意提示”：{
    “场景”：{
      "location": "昏暗的台球酒吧",
      “背景”：“深色天花板，红白色墙壁条纹，后面有几张桌子/椅子，低光氛围与微妙的胶片颗粒”，
      “key_props”：[
        “绿色毡台球桌（前景）”，
        “头顶上的老式红色台球灯（温暖的红色光芒）”，
        “桌子上散落着台球”，
        “台球杆（对象持有）”
      ]
    },
    “主题”：{
      “type”：“年轻成年女性”，
      "identity_instruction": "拍摄对象必须与上传的参考照片100%相同（相同的面孔、比例、年龄和身份）。无身份漂移。",
      "pose": "靠在台球桌边缘；一只手支撑在桌子上；另一只手垂直握住球杆；臀部稍微弹出；头部稍微倾斜；向上看向侧面",
      “表情”：“冷静、自信、微妙的调情”，
      “衣柜”：{
        "top": "豹纹紧身胸衣/带肩带紧身胸衣",
        "bottom": "黑色迷你裙",
        “配件”：“最小的珠宝（小圈或饰钉）”
      },
      “详细信息”：{
        "nails": "红色指甲油",
        “头发”：“长而浓密的卷发”，
        "makeup": "夜间魅力：轮廓分明的眼线/睫毛、温暖的腮红、裸棕色的嘴唇"
      }
    },
    “相机和照明”：{
      "shot_style": "逼真的夜生活闪光灯照片+酒吧环境灯光",
      "camera": "全画幅单反相机",
      “镜头”：“35毫米或50毫米”，
      “光圈”：“f/1.8”，
      "shutter_speed": "1/80s",
      “iso”：“800”，
      “照明”：{
        "primary": "机上闪光灯（清晰的主题、自然的衰减、逼真的阴影）",
        "secondary": "头顶红灯发光 + 昏暗的环境填充",
        “look”：“高对比度，受控镜面高光，无吹白”
      },
      "color_grading": "温暖的红色，自然的肤色，微妙的胶片颗粒",
      “焦点”：“锐利的眼睛和脸部，浅景深，柔和的背景散景”
    }
  },
  “否定提示”：[
    “不同的人”，
    “身份改变”，
    “变脸”，
    “额外的人”，
    “额外的肢体”，
    “额外的手指”，
    “坏手”，
    “变形的解剖结构”，
    “扭曲的球杆”，
    “变形的台球桌”，
    “文本”，
    “标志”，
    “水印”，
    “卡通”，
    “动漫”，
    “插图”，
    “皮肤过于光滑”，
    “塑料皮肤”，
    “低分辨率”，
    “模糊的脸”，
    “闪光高光曝光过度”
  ]
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。Generate a photorealistic image of a young woman in a billiards bar using a reference photo to ensure identity preservation.

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

# Realistic İmage JSON Prompt

**Description:** A JSON-based prompt for generating realistic images. This prompt allows users to specify various parameters and constraints to create detailed and lifelike images using AI technologies. It is ideal for artists, designers, and developers looking to enhance their projects with high-quality visuals.

**Type:** IMAGE
**Author:** narrivo
**Created:** 2026-04-22T10:35:08.927Z
**Votes:** 1
**Views:** 0

**Tags:** image-generation, image-prompt

**Category:** Image Generation

## Prompt Content

```
{
  "meta_instruction": {
    "image_category": "cinematic_scene",
    "core_prompt": "A cinematic shot taken from inside a dimly lit blacksmith shop looking outwards towards a partially open rolling shutter. A middle-aged master and his young apprentice are having a traditional Turkish breakfast on a scrap wood table covered with newspaper. The morning sunlight streams through the 80% open shutter, creating a beautiful lens flare and illuminating the dust particles in the air. The master is speaking while the apprentice listens with polite curiosity.",
    "negative_prompt": "clean pristine clothes, spotless environment, modern furniture, soft unworked hands, messy food, overexposed, fully open shutter, artificial studio lighting, cartoonish, 3d render"
  },
  "narrative_and_purpose": {
    "story_or_concept": "A moment of mentorship and tradition. An apprentice respectfully listening to his master during a peaceful early morning breakfast before a hard day's work in an industrial site.",
    "mood_and_vibe": "Authentic, warm, respectful, raw, industrious, serene morning."
  },
  "subjects": [
    {
      "presence": "primary",
      "type": "human",
      "description": "Middle-aged blacksmith master.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Middle-aged male, stubble beard, wearing reading glasses resting on his chest with a neck strap.",
          "emotion_and_expression": "Experienced, calm, speaking with authority and warmth.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean from dirt but look deeply worn, calloused, and weathered. Sitting and eating breakfast."
        }
      }
    },
    {
      "presence": "primary",
      "type": "human",
      "description": "Young blacksmith apprentice.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Young male, humble appearance.",
          "emotion_and_expression": "Curious, polite, respectful, actively listening.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean but show signs of manual labor. Sitting at the table, leaning in slightly to listen attentively."
        }
      }
    }
  ],
  "environment_and_worldbuilding": {
    "setting_type": "indoor",
    "location_details": "Inside a gritty mechanic and blacksmith shop in an industrial zone. A metal rolling shutter door is 80% open, revealing the bright morning outside.",
    "time_of_day_and_weather": "Early morning, sunrise, clear weather outside.",
    "props_and_supporting_elements": [
      "Low coffee table made from scrap wood",
      "Newspaper spread as a tablecloth",
      "Chrome plates containing tomatoes, black olives, white feta cheese, and cucumbers",
      "A metal pan of 'menemen' (Turkish scrambled eggs with tomatoes) in the center",
      "A custom trivet under the pan made from welded scrap iron pieces",
      "Metal shavings scattered organically on the shop floor"
    ]
  },
  "camera_and_lens": {
    "shot_scale": "medium_shot",
    "camera_angle": "eye_level",
    "lens_focal_length": "35mm",
    "depth_of_field": "Shallow depth of field, sharp focus on the subjects and the breakfast table, background and outside lightly blurred."
  },
  "lighting_and_atmosphere": {
    "lighting_source": "natural",
    "lighting_quality": "high_contrast",
    "atmospheric_effects": "Morning sun rays streaming into the dark shop, illuminated airborne dust particles, gentle lens flare from the sun."
  },
  "composition_and_layout": {
    "framing_rule": "rule_of_thirds",
    "functional_space": "none"
  },
  "post_processing_and_medium": {
    "medium": "digital_photography",
    "color_grading": "Cinematic color grading, warm earthy tones inside contrasting with the bright morning light outside, subtle teal and orange hues.",
    "texture_and_grain": "Subtle film grain, highly detailed textures on hands, wood, and metal."
  }
}
```

**Source:** https://prompts.chat/prompts/cmo9x251b000ajm04u1vmh02i_realistic-image-json-prompt

## 中文翻译

### 标题
逼真的图像 JSON 提示

### 提示词内容

```
{
  "meta_instruction": {
    "image_category": "cinematic_scene",
    "core_prompt": "A cinematic shot taken from inside a dimly lit blacksmith shop looking outwards towards a partially open rolling shutter. A middle-aged master and his young apprentice are having a traditional Turkish breakfast on a scrap wood table covered with newspaper. The morning sunlight streams through the 80% open shutter, creating a beautiful lens flare and illuminating the dust particles in the air. The master is speaking while the apprentice listens with polite curiosity.",
    "negative_prompt": "clean pristine clothes, spotless environment, modern furniture, soft unworked hands, messy food, overexposed, fully open shutter, artificial studio lighting, cartoonish, 3d render"
  },
  "narrative_and_purpose": {
    "story_or_concept": "A moment of mentorship and tradition. An apprentice respectfully listening to his master during a peaceful early morning breakfast before a hard day's work in an industrial site.",
    "mood_and_vibe": "Authentic, warm, respectful, raw, industrious, serene morning."
  },
  "subjects": [
    {
      "presence": "primary",
      "type": "human",
      "description": "Middle-aged blacksmith master.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Middle-aged male, stubble beard, wearing reading glasses resting on his chest with a neck strap.",
          "emotion_and_expression": "Experienced, calm, speaking with authority and warmth.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean from dirt but look deeply worn, calloused, and weathered. Sitting and eating breakfast."
        }
      }
    },
    {
      "presence": "primary",
      "type": "human",
      "description": "Young blacksmith apprentice.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Young male, humble appearance.",
          "emotion_and_expression": "Curious, polite, respectful, actively listening.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean but show signs of manual labor. Sitting at the table, leaning in slightly to listen attentively."
        }
      }
    }
  ],
  "environment_and_worldbuilding": {
    "setting_type": "indoor",
    "location_details": "Inside a gritty mechanic and blacksmith shop in an industrial zone. A metal rolling shutter door is 80% open, revealing the bright morning outside.",
    "time_of_day_and_weather": "Early morning, sunrise, clear weather outside.",
    "props_and_supporting_elements": [
      "Low coffee table made from scrap wood",
      "Newspaper spread as a tablecloth",
      "Chrome plates containing tomatoes, black olives, white feta cheese, and cucumbers",
      "A metal pan of 'menemen' (Turkish scrambled eggs with tomatoes) in the center",
      "A custom trivet under the pan made from welded scrap iron pieces",
      "Metal shavings scattered organically on the shop floor"
    ]
  },
  "camera_and_lens": {
    "shot_scale": "medium_shot",
    "camera_angle": "eye_level",
    "lens_focal_length": "35mm",
    "depth_of_field": "Shallow depth of field, sharp focus on the subjects and the breakfast table, background and outside lightly blurred."
  },
  "lighting_and_atmosphere": {
    "lighting_source": "natural",
    "lighting_quality": "high_contrast",
    "atmospheric_effects": "Morning sun rays streaming into the dark shop, illuminated airborne dust particles, gentle lens flare from the sun."
  },
  "composition_and_layout": {
    "framing_rule": "rule_of_thirds",
    "functional_space": "none"
  },
  "post_processing_and_medium": {
    "medium": "digital_photography",
    "color_grading": "Cinematic color grading, warm earthy tones inside contrasting with the bright morning light outside, subtle teal and orange hues.",
    "texture_and_grain": "Subtle film grain, highly detailed textures on hands, wood, and metal."
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A JSON-based prompt for generating realistic images. This prompt allows users to specify various parameters and constraints to create detailed and lifelike images using AI technologies. It is ideal for artists, designers, and developers looking to enhance their projects with high-quality visuals.

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

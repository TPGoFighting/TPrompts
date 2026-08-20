# Isometric City Diorama

**Description:** Structured prompt for generating an isometric city diorama in a miniature 3D style, with weather and environment adaptive to the specified city.

**Type:** TEXT
**Author:** f
**Created:** 2025-12-11T22:45:52.483Z
**Votes:** 2
**Views:** 0

**Tags:** Midjourney, Vision

**Category:** Image Generation

## Prompt Content

```
{
  "meta": {
    "description": "Structured prompt for generating an isometric city diorama in a miniature 3D style, with weather and environment adaptive to the specified city.",
    "variable": "${City:San Francisco}"
  },
  "prompt_structure": {
    "perspective_and_format": {
      "view": "Isometric camera view",
      "format": "Miniature 3D diorama resting on a floating square base serving as the ground plinth.",
      "ratio": "16:9 (vertical phone)"
    },
    "art_style": {
      "medium": "High-detail 3D render",
      "texture_quality": "Realistic textures appropriate for the region's architecture (e.g., stone/brick, stucco/adobe, glass/steel).",
      "vibe": "Toy-like but highly sophisticated architectural model with tactile material qualities."
    },
    "environment_and_atmosphere": {
      "weather": "Typical climate and weather conditions associated with the specified city (e.g., overcast/rainy for London, bright/sunny/arid for Cairo, snowy for Moscow). Lighting matches the weather.",
      "ground": "Ground surface material typical for the city (e.g., asphalt, cobblestones, sand, dirt). Surface conditions reflect the weather (e.g., wet with reflections if rainy, dry and dusty if arid, snow-covered if winter).",
      "background": "Sky gradient and atmosphere matching the chosen weather, filling the upper frame."
    },
    "architectural_elements": {
      "housing": "Dense cluster of residential or commercial buildings reflecting the city's vernacular architecture style.",
      "landmarks": "Isometric miniature representations of iconic landmarks defining the city."
    },
    "props_and_details": {
      "street_level": "Miniature elements specific to the city's vibe (e.g., iconic vehicles like yellow cabs or red buses, specific vegetation like palm trees or deciduous trees, streetlights, signage).",
      "life": "Tiny, stylized figures dressed in clothing appropriate for the climate and culture."
    },
    "text_overlay": {
      "content": "${City:San Francisco}",
      "font_style": "White, sans-serif, bold, uppercase letters",
      "placement": "Centered floating at the very top of the frame."
    }
  }
}
```

**Source:** https://prompts.chat/prompts/cmj211exv0005wa0stbf15gvm_isometric-city-diorama

## 中文翻译

### 标题
等距城市立体模型

### 提示词内容

```
{
  “元”：{
    "description": "生成微型 3D 风格的等距城市立体模型的结构化提示，天气和环境适应指定城市。",
    "variable": "${城市:旧金山}"
  },
  “提示结构”：{
    “透视和格式”：{
      "view": "等距相机视图",
      "format": "微型 3D 立体模型放置在作为地面底座的浮动方形底座上。",
      "ratio": "16:9（竖屏手机）"
    },
    “艺术风格”：{
      "medium": "高细节 3D 渲染",
      "texture_quality": "适合该地区建筑的真实纹理（例如石头/砖、灰泥/土坯、玻璃/钢）。",
      “vibe”：“类似玩具但高度复杂的建筑模型，具有触觉材料品质。”
    },
    “环境和大气”：{
      "weather": "与指定城市相关的典型气候和天气条件（例如，伦敦阴/雨，开罗晴/晴/干旱，莫斯科下雪）。照明与天气相匹配。",
      "ground": "城市典型的地面材料（例如，沥青、鹅卵石、沙子、泥土）。地表条件反映了天气（例如，下雨时潮湿并有反射，干旱时干燥且多尘，冬季时积雪覆盖）。",
      "background": "与所选天气相匹配的天空渐变和大气，填充上框。"
    },
    “建筑元素”：{
      "housing": "密集的住宅或商业建筑群，体现了城市的乡土建筑风格。",
      “landmarks”：“定义城市的标志性地标的等距微型表示。”
    },
    “道具和详细信息”：{
      "street_level": "特定于城市氛围的微型元素（例如，黄色出租车或红色巴士等标志性车辆、棕榈树或落叶树等特定植被、路灯、标牌）。",
      《life》：“微小的、程式化的人物穿着适合气候和文化的衣服。”
    },
    “文本覆盖”：{
      "content": "${城市:旧金山}",
      "font_style": "白色、无衬线、粗体、大写字母",
      "placement": "居中浮动在框架的最顶部。"
    }
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Structured prompt for generating an isometric city diorama in a miniature 3D style, with weather and environment adaptive to the specified city.

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
- `${City}`: 可自定义（默认值: San Francisco）
- `${City}`: 可自定义（默认值: San Francisco）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

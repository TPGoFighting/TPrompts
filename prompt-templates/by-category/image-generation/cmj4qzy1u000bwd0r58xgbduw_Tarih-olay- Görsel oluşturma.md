# Tarih-olay- Görsel oluşturma

**Description:** Prompt Konum (location)ve tarih (date) kısmını siz gireceksiniz

O tarihte o konumda olmuş önemli bir olayı (var ise) nano banana araştırıyor ve ona uygun bir görsel oluşturuyor


**Type:** TEXT
**Author:** stiva1979
**Created:** 2025-12-13T20:28:06.306Z
**Votes:** 2
**Views:** 0

**Category:** Image Generation

## Prompt Content

```
{
  "meta": {
    "model": "nano-banana-pro",
    "mode": "thinking",
    "use_search_grounding": true,
    "language": "tr"
  },
  "input": {
    "location": "${Location: Location}",
    "date": "${Date: YYYY-MM-DD}",
    "aspectRatio": "${Aspect Ratio: 16:9 | 4:3 | 1:1 | 9:16}",
    "timeOfDay": "${Time of the Day}",
    "mood": "${Mood: epic | solemn | celebratory | tense | melancholic}"
  },
  "prompt": {
    "positive": "Konum: ${Location: Location}\nTarih: ${Date: YYYY-MM-DD}\n\nÖnce güvenilir kaynaklarla arama yap ve bu tarihte bu konumda gerçekleşen en önemli tarihsel olayı belirle. Sonra bu olayı temsil eden tek bir foto-gerçekçi, ultra detaylı, sinematik kare üret.\n\nDönem doğruluğu zorunlu: mimari, kıyafet, silah/araç ve şehir dokusu tarihle tutarlı olsun. Modern hiçbir obje, bina, araç veya tabela görünmesin. Tek sahne, tek an, gerçek kamera fiziği, doğal insan oranları, yüksek mikro detay.",
    "negative": "modern buildings, cars, asphalt, neon, smartphones, wrong era clothing/armor, fantasy, anime, cartoon, text overlay, blurry, low-res, extra limbs"
  },
  "render": {
    "quality": "ultra",
    "resolution": "4k"
  },
  "name": "My Workflow",
  "steps": []
}
```

**Source:** https://prompts.chat/prompts/cmj4qzy1u000bwd0r58xgbduw_date-event-image-creation

## 中文翻译

### 标题
Tarih-olay- Görsel oluşturma

### 提示词内容

```
{
  “元”：{
    “型号”：“纳米香蕉专业”，
    “模式”：“思考”，
    “use_search_grounding”：正确，
    “语言”：“tr”
  },
  “输入”：{
    "location": "${位置: 位置}",
    "date": "${日期: YYYY-MM-DD}",
    "aspectRatio": "${宽高比: 16:9 | 4:3 | 1:1 | 9:16}",
    "timeOfDay": "${一天中的时间}",
    "mood": "${心情：史诗|庄严|庆祝|紧张|忧郁}"
  },
  “提示”：{
    "positive": "Konum: ${Location: Location}\nTarih: ${Date: YYYY-MM-DD}\n\nÖnce güvenilir kaynaklarla arama yap ve bu tarihte bu konumda gerçekleşen en önemli tarihsel olayı belirle。Sonra bu olayı temsil eden tek bir摄影、超详细、清晰。\n\nDönem doğruluğu zorunlu：mimari、kıyafet、silah/araç ve şehir dokusu tarihle tutarlı olsun。 sahne、tek an、gerçek kamera fiziği、doğal insan oranları、yüksek mikro detay。",
    “负面”：“现代建筑、汽车、沥青、霓虹灯、智能手机、错误时代的服装/盔甲、幻想、动漫、卡通、文本叠加、模糊、低分辨率、额外的肢体”
  },
  “渲染”：{
    “质量”：“超”，
    “分辨率”：“4k”
  },
  "name": "我的工作流程",
  “步骤”：[]
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Prompt Konum (location)ve tarih (date) kısmını siz gireceksiniz

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
- `${Location}`: 可自定义（默认值:  Location）
- `${Date}`: 可自定义（默认值:  YYYY-MM-DD）
- `${Mood}`: 可自定义（默认值:  epic | solemn | celebratory | tense | melancholic）
- `${Location}`: 可自定义（默认值:  Location）
- `${Date}`: 可自定义（默认值:  YYYY-MM-DD）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

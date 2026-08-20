# Neon Silence

**Type:** IMAGE
**Author:** kyllimir
**Created:** 2025-12-31T18:45:36.789Z
**Votes:** 1
**Views:** 0

**Category:** Image Generation

## Prompt Content

```
{
  "task": "style_transfer_portrait_poster",
  "input": {
    "reference_image": "${reference_image_url_or_path}",
    "use_reference_as": "content_and_pose",
    "preserve": [
      "yüz ifadesi ve bakış yönü",
      "saç/siluet ve kıyafet formu",
      "kadraj (üst gövde portre)",
      "ışık yönü ve gölge dağılımı"
    ]
  },
  "prompt": {
    "language": "tr",
    "style_goal": "Referans görseldeki kişiyi/konuyu, aynı kompozisyonu koruyarak yüksek kontrastlı neon-ink poster illüstrasyonu stiline dönüştür.",
    "main": "Dikey (9:16) sinematik portre illüstrasyonu: referans görseldeki ana konu (kişi/figür) aynı poz ve kadrajda kalsın. Stil: koyu lacivert/siyah mürekkep dokuları ve kalın konturlar; yüz ve kıyafet üzerinde oyma/gravür benzeri ince çizgisel gölgelendirme (etched shading), cel-shading ile birleşen poster estetiği. Arka plan: düz, çok doygun sıcak neon pembe/kırmızı zemin; etrafında sıvı mürekkep/duman girdapları, akışkan alevimsi kıvrımlar ve parçacık sıçramaları. Vurgu rengi olarak neon pembe/kırmızı lekeler: yüzde çizik/iz gibi küçük vurgular, giyside ve duman dokusunda serpiştirilmiş parlak damlacıklar. Yüksek kontrast, sert kenarlar, dramatik karanlık tonlar, minimal ama güçlü renk paleti (koyu soğuk tonlar + neon sıcak arka plan). Hafif baskı grain’i ve poster dokusu; ultra net, yüksek çözünürlüklü kapak/poster görünümü.",
    "content_rules": [
      "Marka, model, logo, rozet, imza, watermark veya okunabilir metin EKLEME.",
      "Referans görselde yazı/logolar varsa okunabilirliğini kaldır: bulanıklaştır, soyut şekle çevir veya sil.",
      "Yeni kişi/obje ekleme; sadece referanstaki içeriği stilize et.",
      "Yüz anatomi oranlarını bozma; doğal ama stilize kalsın."
    ]
  },
  "negative_prompt": [
    "photorealistic",
    "lowres",
    "blurry",
    "muddy shading",
    "extra people",
    "extra limbs",
    "deformed face",
    "uncanny",
    "new text",
    "brand names",
    "logos",
    "watermark",
    "signature",
    "busy background details",
    "washed out neon",
    "color banding",
    "jpeg artifacts"
  ],
  "generation": {
    "mode": "image_to_image",
    "strength": 0.6,
    "style_transfer_weight": 0.85,
    "composition_lock": 0.8,
    "detail_level": "high",
    "resolution": {
      "width": 1080,
      "height": 1920
    },
    "guidance": {
      "cfg_scale": 7.0
    },
    "sampler": "auto",
    "seed": "auto"
  },
  "postprocess": {
    "sharpen": "medium_low",
    "grain": "subtle",
    "contrast": "high",
    "saturation": "high"
  }
}
```

**Source:** https://prompts.chat/prompts/cmjud9h1w0001ld042c6l5mcx_neon-silence

## 中文翻译

### 标题
霓虹灯沉默

### 提示词内容

```
{
  "任务": "style_transfer_portrait_poster",
  “输入”：{
    "reference_image": "${reference_image_url_or_path}",
    "use_reference_as": "内容和姿势",
    “保留”：[
      “yüz ifadesi ve bakış yönü”，
      “saç/siluet ve kıyafet formu”，
      “kadraj（üst gövde portre）”，
      “Işık yönü ve golge dağılımı”
    ]
  },
  “提示”：{
    “语言”：“tr”，
    "style_goal": "参考 görseldeki kişiyi/konuyu，aynı kompozisyonu koruyarak yüksek kontrastlı 霓虹灯海报 illüstrasyonu stiline dönüştür。",
    "main": "Dikey (9:16) sinematik portre illüstrasyonu:referans görseldeki ana konu (kişi/figür) aynı poz ve kadrajda kalsın. Stil: koyu lacivert/siyah mürekkep dokuları ve kalın konturlar; yüz ve kıyafet üzerinde oyma/gravür benzeri ince çizgisel gölgelendirme（蚀刻阴影），cel-shading ile birleşen海报Arka计划：düz，çok doygun sıcak neon pembe/kırmızı zemin；etrafında sıvı mürekkep/duman girdapları，可能会出现霓虹灯闪烁/闪烁的情况： yüzde çizik/iz gibi küçük vurgular，giyside ve duman dokusunda serpiştirilmiş parlak damlacıklar。 kontrast、sert kenarlar、dramatik karanlık tonlar、minimal ama güçlü renk Palati（koyu soğuk tonlar + neon sıcak arka plan）。
    “内容规则”：[
      “Marka、模型、徽标、rozet、imza、水印 veya okunabilir metin EKLEME。”,
      "参考 görselde yazı/logolar varsa okunabilirliğini kaldır: bulanıklaştır, soyut şekle çevir veya sil。",
      “Yeni kişi/obje ekleme；sadecereferanstaki içeriği stilize et.”，
      “Yüz anatomi oranlarını bozma；doğal ama stilize kalsın。”
    ]
  },
  “否定提示”：[
    “照片级写实”，
    “低”，
    “模糊”，
    “泥泞的阴影”，
    “额外的人”，
    “额外的肢体”，
    “变形脸”，
    “不可思议”，
    “新文本”，
    “品牌名称”，
    “标志”，
    “水印”，
    “签名”，
    “繁忙的背景详细信息”，
    “洗掉霓虹灯”，
    “色带”，
    “jpeg 工件”
  ],
  “一代”：{
    “模式”：“图像到图像”，
    “强度”：0.6，
    “风格转移权重”：0.85，
    “组合锁”：0.8，
    "detail_level": "高",
    “分辨率”：{
      “宽度”：1080，
      “身高”：1920
    },
    “指导”：{
      “cfg_scale”：7.0
    },
    “采样器”：“自动”，
    “种子”：“自动”
  },
  “后处理”：{
    “锐化”：“中低”，
    “颗粒”：“微妙”，
    “对比度”：“高”，
    “饱和度”：“高”
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。它可以帮助你完成与Neon Silence相关的任务。

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
- `${reference_image_url_or_path}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

# 🤖 SafeKids Video Analyzer

**Description:** SafeKids Video Analyzer is an AI prompt that evaluates whether a YouTube video is appropriate for children using a video URL, transcript, or summary. It generates a structured Turkish report with age recommendations, risk scores, content warnings, educational value, parental guidance, and an approximate international age rating. The analysis is evidence-based, objective, and avoids speculation.


**Type:** TEXT
**Author:** gunebak4n
**Created:** 2026-07-06T11:04:09.553Z
**Votes:** 0
**Views:** 0

**Tags:** YouTube Analysis, Parenting

**Category:** Kids & Early Learning

## Prompt Content

```
Objective

Analyze the YouTube video URL, transcript, or summary provided by the user and determine whether the content is appropriate for children. Produce a factual, structured, easy-to-read report in Turkish for parents.

Context

Parents want to quickly understand whether a video is suitable for children, what potential risks it contains, and which age group it is appropriate for.

Inputs

The user may provide one of the following:
- YouTube video URL
- Video transcript
- Video summary

If only a URL is provided and the video cannot be accessed or analyzed, clearly explain that a reliable assessment cannot be made without sufficient information. Never invent details.

Instructions

Base the evaluation only on observable content.

Do NOT speculate about scenes, dialogue, intentions, or events that are not supported by the available information.

When evidence is insufficient, explicitly state this.

Evaluate both positive and negative aspects of the content.

Assess the following categories:

- Language and profanity
- Violence, fear, horror, jumpscares
- Sexual or suggestive content
- Alcohol, smoking, drugs
- Dangerous behaviors or harmful challenges
- Bullying, discrimination, hate speech
- Educational value
- Positive messages (friendship, empathy, cooperation, creativity, learning)
- Emotional intensity for young children

Assign a risk score (0–5) for each category:

0 = None
1 = Very Low
2 = Low
3 = Moderate
4 = High
5 = Very High

Scores must be based only on observable evidence.

Decision Priority

When determining the final verdict, evaluate the content using the following priority order:

1. Child safety risks
2. Psychological and emotional impact
3. Explicit or age-inappropriate content
4. Frequency, duration, and intensity of risky content
5. Educational, creative, and positive value

Educational value must never outweigh serious safety or psychological concerns.

A single severe issue (for example, graphic violence or dangerous imitation) may justify a "Dikkat Edilmeli" or "Uygun Değil" verdict even if the rest of the content is appropriate.

Age Recommendation Rule

Recommend the youngest age group that is appropriate for the majority of children.

If suitability depends on a child's maturity, clearly state this.

When uncertain between two age groups, recommend the more conservative (older) age group.

Evidence Rule

Differentiate clearly between:

- Directly observed facts
- Reasonable inferences based on observable evidence
- Unknown or unavailable information

Never present assumptions as facts.

Confidence Level

After the final recommendation, indicate your confidence level:

🟢 High Confidence
- Based on a complete transcript or a detailed summary.

🟡 Medium Confidence
- Based on partial information.

🔴 Low Confidence
- Based on very limited information (for example, only a title or incomplete summary).

Explain briefly why this confidence level was assigned.

Special Cases

If the content includes satire, fantasy, animation, roleplay, fictional violence, or parody, clearly distinguish fictional content from realistic behavior.

Evaluate fictional content according to its likely impact on children rather than treating it as real-world events.

Context Matters

Consider:

- Whether risky behaviors are encouraged or discouraged.
- Whether consequences are shown.
- Whether inappropriate actions are rewarded, normalized, criticized, or corrected.
- Whether adult supervision is present within the video.
- Whether the creator explicitly provides safety warnings.
- Whether dangerous actions are repeated or isolated.

A brief appearance of risky content should generally be evaluated differently from repeated or glorified exposure.

Output Specification

Generate the entire response in Turkish using the following structure.

# 🎯 GENEL DEĞERLENDİRME

**Video:** [Title if available]

**Karar:**
- ✅ Uygun
- ⚠️ Dikkat Edilmeli
- ❌ Uygun Değil

**Genel Risk Seviyesi:**
- 🟢 Düşük
- 🟡 Orta
- 🔴 Yüksek

**Önerilen Yaş:**
- 3+
- 6+
- 9+
- 13+
- 16+
- 18+

Provide a short overall explanation (2–3 sentences).

---

# 📝 İÇERİK ÖZETİ

Summarize the video in one or two short paragraphs.

---

# 🔍 RİSK ANALİZİ

## 🗣️ Dil ve Argo
- Değerlendirme
- Risk Puanı: X/5

## 🥊 Şiddet ve Korku
- Değerlendirme
- Risk Puanı: X/5

## ❤️ Cinsel İçerik / Müstehcenlik
- Değerlendirme
- Risk Puanı: X/5

## 🚬 Alkol / Sigara / Madde Kullanımı
- Değerlendirme
- Risk Puanı: X/5

## 🧠 Olumsuz Davranışlar
- Tehlikeli hareketler
- Zararlı meydan okumalar
- Kötü rol model davranışları
- Risk Puanı: X/5

## 🚫 Zorbalık / Ayrımcılık / Nefret Söylemi
- Değerlendirme
- Risk Puanı: X/5

## ❤️ Olumlu Mesajlar
- Eğitim değeri
- Empati
- Yardımlaşma
- Problem çözme
- Yaratıcılık
- Öğrenmeye katkı

---

# ⚠️ İÇERİK UYARILARI

List only the warnings that actually apply.

Possible examples:
- 😱 Ani korku sahneleri
- 🩸 Kan veya yaralanma görüntüleri
- 🔊 Yüksek ses efektleri
- 😢 Yoğun duygusal sahneler
- 💀 Ölüm teması
- 👻 Korku unsurları
- 🤬 Küfür
- 🚬 Sigara
- 🍺 Alkol
- 💉 Uyuşturucu
- 💋 Romantik / cinsel içerik
- ⚔️ Dövüş sahneleri
- 🚗 Tehlikeli araç kullanımı
- 🔥 Riskli hareketlerin taklit edilmesi

If none apply, explicitly state:
"Belirgin bir içerik uyarısı bulunmamaktadır."

---

# 👨‍👩‍👧 EBEVEYN GÖZETİMİ

Clearly state one of the following:

- ✅ Tek başına izleyebilir.
- 👨‍👩‍👧 Ebeveyn eşliğinde izlenmesi önerilir.
- ⛔ Küçük çocuklar için önerilmez.

Explain why in one or two sentences.

---

# 🌍 ULUSLARARASI YAŞ DERECELENDİRMESİ (Yaklaşık)

If possible, provide the closest equivalent rating.

Examples:

- Everyone (ESRB)
- Everyone 10+
- Teen (ESRB)
- Mature 17+
- PEGI 3
- PEGI 7
- PEGI 12
- PEGI 16
- PEGI 18

If an exact match cannot be determined, clearly state that this is only an approximate comparison.

---

# 🧠 KARAR GÜVENİ

- 🟢 High Confidence
- 🟡 Medium Confidence
- 🔴 Low Confidence

Brief explanation of why this confidence level was assigned.

---

# ✨ SONUÇ VE TAVSİYE

Provide practical advice for parents.

Mention:

- Why the content is or is not appropriate.
- Whether adult supervision is recommended.
- Which age group is most suitable.
- Whether sensitive children may be negatively affected.
- Whether the educational value outweighs any potential risks.

Constraints

- The entire output MUST be in Turkish.
- Use Markdown headings.
- Use emojis consistently (🎯 📝 🔍 🗣️ 🥊 ❤️ 🚬 🧠 🚫 ⚠️ 👨‍👩‍👧 🌍 ✨).
- Keep paragraphs short.
- Avoid large walls of text.
- Never fabricate details.
- Base every conclusion only on observable evidence.
- Clearly distinguish facts from uncertainty.
- If insufficient information is available, state this explicitly instead of guessing.

Acceptance Criteria

The response must:

- Include every required section.
- Clearly state the final verdict.
- Clearly state the overall risk level.
- Clearly state the recommended age group.
- Include individual risk scores (0–5).
- Include applicable content warnings.
- Include a parent supervision recommendation.
- Include an approximate international age rating when possible.
- Include a confidence level.
- Remain objective, evidence-based, and factual.
- Never invent details that are not supported by the provided material.
```

**Source:** https://prompts.chat/prompts/cmr944c410001lg04scs57c1c_safekids-video-analyzer

## 中文翻译

### 标题
🤖 SafeKids 视频分析仪

### 提示词内容

```
目的

分析用户提供的 YouTube 视频 URL、文字记录或摘要，并确定内容是否适合儿童。用土耳其语为家长制作一份真实、结构化、易于阅读的报告。背景

家长希望快速了解某个视频是否适合儿童、包含哪些潜在风险以及适合哪个年龄段。输入

用户可以提供以下其中一项：
- YouTube 视频网址
- 视频文字记录
- 视频摘要

如果仅提供 URL 而无法访问或分析视频，请明确说明在没有足够信息的情况下无法做出可靠的评估。永远不要发明细节。使用说明

仅根据可观察的内容进行评估。不要推测现有信息不支持的场景、对话、意图或事件。当证据不足时，明确说明这一点。评估内容的积极和消极方面。评估以下类别：

- 语言和脏话
- 暴力、恐惧、恐怖、跳跃惊吓
- 色情或暗示性内容
- 酗酒、吸烟、吸毒
- 危险行为或有害挑战
- 欺凌、歧视、仇恨言论
- 教育价值
- 积极的信息（友谊、同理心、合作、创造力、学习）
- 幼儿的情绪强度

为每个类别分配风险评分 (0–5)：

0 = 无
1 = 非常低
2 = 低
3 = 中等
4 = 高
5 = 非常高

分数必须仅基于可观察到的证据。决策优先级

在确定最终判决时，请按照以下优先顺序评估内容：

1、儿童安全风险
2.心理和情绪影响
3. 露骨或不适合年龄的内容
4. 风险内容的频率、持续时间和强度
5. 教育性、创造性和积极价值

教育价值绝不能超过严重的安全或心理问题。即使其余内容是适当的，单个严重问题（例如，图形暴力或危险模仿）也可能证明“Dikkat Edilmeli”或“Uygun Değil”判决是合理的。年龄推荐规则

推荐适合大多数儿童的最小年龄组。如果适合性取决于孩子的成熟度，请明确说明。当两个年龄组之间不确定时，建议使用更保守（年龄较大）的年龄组。证据规则

明确区分：

- 直接观察到的事实
- 基于可观察证据的合理推论
- 未知或不可用的信息

切勿将假设呈现为事实。置信度

在最终建议后，请表明您的信心水平：

🟢 高信心
- 基于完整的成绩单或详细的摘要。 🟡中等信心
- 基于部分信息。 🔴信心不足
- 基于非常有限的信息（例如，只有标题或不完整的摘要）。简要解释为什么指定此置信水平。特殊情况

如果内容包括讽刺、幻想、动画、角色扮演、虚构暴力或戏仿，请明确区分虚构内容和现实行为。根据虚构内容可能对儿童的影响来评估虚构内容，而不是将其视为现实世界的事件。背景很重要

考虑：

- 是否鼓励或劝阻危险行为。 - 是否显示后果。 - 不当行为是否受到奖励、规范化、批评或纠正。 - 视频中是否存在成人监督。 - 创建者是否明确提供安全警告。 - 危险行为是否重复或孤立。风险内容的短暂出现通常应与重复或美化的暴露进行不同的评估。输出规格

使用以下结构生成土耳其语的完整响应。 # 🎯 GENEL DEĞERLENDIRME

**视频：** [标题（如果有）]

**卡拉：**
- ✅ 乌伊贡
- ⚠️ Dikkat Edilmeli
- ❌ 乌伊贡·德吉尔

**通用风险塞维耶西：**
- 🟢 杜苏克
- 🟡奥尔塔
- 🔴尤克塞克

**奥纳里伦·亚什：**
- 3+
- 6+
- 9+
- 13+
- 16+
- 18+

提供简短的总体解释（2-3 句话）。 ---

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📞

用一两个短段落总结视频。 ---

# 🔍 风险分析

## 🗣️ 迪尔维阿尔戈
- 德格伦迪尔梅
- 风险损失：X/5

## 🥊 Şiddet ve Korku
- 德格伦迪尔梅
- 风险损失：X/5

## ❤️ Cinsel Içerik / Müstehcenlik
- 德格伦迪尔梅
- 风险损失：X/5

## 🚬 阿尔科尔 / 西加拉 / 马德·库拉尼米
- 德格伦迪尔梅
- 风险损失：X/5

## 🧠 奥卢姆苏兹·达夫拉尼什拉尔
- 泰里克利·哈雷克特勒
- Zararlı meydan okumalar
- Kötü rol 模型 davranışları
- 风险损失：X/5

## 🚫 佐巴勒克 / 艾瑞姆西勒克 / Nefret Söylemi
- 德格伦迪尔梅
- 风险损失：X/5

## ❤️ 奥伦鲁·梅萨吉拉尔
- 埃蒂姆·德埃里
- 恩帕蒂
- 亚迪姆拉什玛
- 问题 çözme
- 亚拉蒂西里克
- Öğrenmeye katkı

---

# ⚠️ 伊塞里克·乌亚里拉里

仅列出实际适用的警告。可能的例子：
- 😱 Ani korku sahneleri
- 🩸 Kan veya yaralanma görüntüleri
- 🔊 Yüksek ses efektleri
- 😢 约根·杜伊古萨尔·萨内勒
- 💀 Ölüm teması
- 👻 科尔库unsurları
- 🤬 库福尔
- 🚬 西加拉
- 🍺 醇
- 💉 乌尤斯图鲁库
- 💋 Romantik / cinsel içerik
- ⚔️ Dövüş sahneleri
- 🚗 Tehlikeli araç kullanımı
- 🔥 Riskli hareketlerin taklit edilmesi

如果都不适用，请明确说明：
“Belirgin bir içerik uyarısı bulunmamaktadır。”

---

# 👨‍👩‍👧 埃贝文·戈泽特伊米

明确说明以下其中一项：

- ✅ Tek başına izleyebilir。 - 👨‍👩‍👧 Ebeveyn eşliğinde izlenmesi önerilir。 - ⛔Küçük çocuklar için önerilmez。用一两句话解释原因。 ---

# 🌍 ULUSLARARASI YAŞ DERECELENDıRMESі (Yaklaşık)

如果可能，请提供最接近的等效评级。示例：

- 每个人（ESRB）
- 10 岁以上的所有人
- 青少年 (ESRB)
- 成熟 17+
- 聚乙二醇3
- 聚乙二醇7
- 佩吉12
- 佩吉16
- 佩吉18

如果无法确定精确匹配，请明确说明这只是近似比较。 ---

#🧠卡拉·古文伊

- 🟢 高信心
- 🟡 中等信心
- 🔴信心不足

简要解释为什么分配此置信水平。 ---

# ✨ 索尼韦塔维斯耶

为家长提供切实可行的建议。提及：

- 为什么内容合适或不合适。 - 是否建议成人监督。 - 哪个年龄段最适合。 - 敏感儿童是否会受到负面影响。 - 教育价值是否超过任何潜在风险。约束条件

- 整个输出必须是土耳其语。 - 使用 Markdown 标题。 - 持续使用表情符号（🎯 📝 🔍 🗣️ 🥊 ❤️ 🚬 🧠 🚫 ⚠️ 👨‍👩‍👧 🌍 ✨）。 - 保持段落简短。 - 避免大面积的文字墙。 - 切勿捏造细节。 - 每个结论仅基于可观察到的证据。 - 清楚地区分事实与不确定性。 - 如果可用信息不足，请明确说明而不是猜测。验收标准

响应必须：

- 包括每个必需的部分。 - 明确陈述最终判决。 - 明确说明总体风险水平。 - 明确说明推荐的年龄组。 - 包括个人风险评分 (0–5)。 - 包括适用的内容警告。 - 包括家长监督建议。 - 如果可能的话，包括大致的国际年龄评级。 - 包括置信度。 - 保持客观、基于证据和事实。 - 切勿发明所提供材料不支持的细节。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。SafeKids Video Analyzer is an AI prompt that evaluates whether a YouTube video is appropriate for children using a video URL, transcript, or summary. It generates a structured Turkish report with age recommendations, risk scores, content warnings, educational value, parental guidance, and an approximate international age rating. The analysis is evidence-based, objective, and avoids speculation.

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

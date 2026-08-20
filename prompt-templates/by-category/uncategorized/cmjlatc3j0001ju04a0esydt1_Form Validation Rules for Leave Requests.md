# Form Validation Rules for Leave Requests

**Description:** This prompt defines validation rules for different types of leave requests in a form. It ensures compliance with specific leave conditions based on the type of leave and prevents duplicate requests for overlapping dates.

**Type:** TEXT
**Author:** muhtesemozgur9
**Created:** 2025-12-25T10:27:09.056Z
**Votes:** 0
**Views:** 0

**Tags:** HR, Workflow, Automation

## Prompt Content

```
{
  "rules": [
    {
      "leaveType": "Evlilik İzni",
      "validity": "Personelin evlenmesi halinde 3 iş günü şeklinde kullandırılır.",
      "maxDays": 3
    },
    {
      "leaveType": "Doğum İzni (Eş)",
      "validity": "Personelin eşinin doğum yapması halinde 5 iş günü",
      "maxDays": 5
    },
    {
      "leaveType": "I.Derece Yakın Ölümü İçin İzin",
      "validity": "Personelin ana, baba, kardeş, eş ve çocuklarının ölümü halinde 3 iş günü",
      "maxDays": 3
    },
    {
      "leaveType": "Doğal Afet",
      "validity": "Doğal afet olması halinde 10 iş gününe kadar kullanılan izindir.",
      "maxDays": 10
    },
    {
      "leaveType": "Ücretli Doğum İzni",
      "validity": "Gebelik ve analık halinde Kanunu’na göre islem yapılır. Kadın personelin dogumdan önce 8 hafta ve dogumdan sonra 8 hafta olmak üzere çalıstırılmamaları esastır. Çogul gebelik halinde dogumdan önce çalıstırılmayacak 8 haftalık süreye iki hafta süre eklenir.",
      "preBirthWeeks": 8,
      "postBirthWeeks": 8,
      "extraWeeksForMultiplePregnancy": 2,
      "workUntilPreWeeks": 3
    },
    {
      "leaveType": "Ücretsiz Doğum İzni",
      "validity": "Ücretli doğum izninin bitmesi durumunda çalışanın talebi üzerine 6 aya kadar verilen izindir. Parçalar halinde kullanılamaz.",
      "maxMonths": 6
    },
    {
      "leaveType": "Hamile Çalışan Sağlık Kontrol İzni",
      "validity": "Hamile çalışanın hamileliğini belgelemesi durumunda aylık kontrollerinde kullanılabilen ve gün kısıtı bulunmayan izin türüdür.",
      "documentationRequired": true
    },
    {
      "leaveType": "Sosyal Mazeret İzni",
      "validity": "Çalışanın bir yılda kullanabilecegi mazeret izni toplam 3 iş günüdür. 3 günü aşan izinler yıllık izinden düşürülür.",
      "maxDaysPerYear": 3
    },
    {
      "leaveType": "Ücretsiz İzin",
      "validity": "Çalışanın yazılı talebi üzerine işverenin uygun görmesi durumunda kısıtı bulunmayan izin türüdür.",
      "documentationRequired": true
    }
  ],
  "generalRules": {
    "duplicateCheck": "Daha önce aynı tarihler içinde bir izin talebi varsa kullanıcının tekrar izin talep etmemeli.",
    "applicableFormId": 1
  }
}
```

**Source:** https://prompts.chat/prompts/cmjlatc3j0001ju04a0esydt1_form-validation-rules-for-leave-requests

## 中文翻译

### 标题
休假申请的表单验证规则

### 提示词内容

```
{
  “规则”：[
    {
      "leaveType": "埃夫利利克·伊兹尼",
      "validity": "Personelin evlenmesi halinde 3 iş günü şeklinde kullandırılır.",
      “最大天数”：3
    },
    {
      "leaveType": "Doğum ızni (Eş)",
      "validity": "Personelin eşinin doğum yapması halinde 5 iş günü",
      “最大天数”：5
    },
    {
      "leaveType": "I.Derece Yakın Ölümü ïçin ïzin",
      "validity": "Personelin ana, baba, kardeş, eş ve çocuklarının ölümü halinde 3 iş günü",
      “最大天数”：3
    },
    {
      "leaveType": "Doğal Afet",
      "validity": "Doğal afet olması halinde 10 iş gününe kadar kullanılan izindir.",
      “最大天数”：10
    },
    {
      "leaveType": "Ücretli Doğum ızni",
      "validity": "Gebelik ve analık halinde Kanunu’na göre islem yapılır. Kadın personelin Dogumdan önce 8 hafta ve Dogumdan sonra 8 hafta olmak üzere çalıstırılmamaları esastır. Çogul gebelik halinde Dogumdan önce çalıstırılmayacak 8 haftalık süreye iki hafta sure eklenir。",
      “出生前周”：8，
      “出生后周”：8，
      “多胎妊娠额外周数”：2，
      “工作直到周前”：3
    },
    {
      "leaveType": "Ücretsiz Doğum ızni",
      "validity": "Ücretli doğum izninin bitmesi durumunda çalışanın talebi üzerine 6 aya kadar verilen izindir。Parçalar halinde kullanılamaz。",
      “最大月份”：6
    },
    {
      "leaveType": "Hamile Çalışan Sağlık Kontrol Ázni",
      "validity": "Hamile çalışanın hamileliğini belgelemesi durumunda aylık kontrollerinde kullanılabilen ve gün kısıtı bulunmayan izin türüdür。",
      “文档必需”：true
    },
    {
      "leaveType": "索西尔·马泽雷·伊兹尼",
      "validity": "Çalışanın bir yılda kullanabilecegi mazeret izni toplam 3 iş günüdür。3 günü aşan izinler yıllık izinden düşürülür。",
      “每年最多天数”：3
    },
    {
      "leaveType": "Ücretsiz ïzin",
      "validity": "Çalışanın yazılı talebi üzerine işverenin uygun görmesi durumunda kısıtı bulunmayan izin türüdür。",
      “文档必需”：true
    }
  ],
  “一般规则”：{
    "duplicateCheck": "Daha önce aynı tarihler içinde bir izin talebi varsa kullanıcının tekrar izin talep etmemeli。",
    “适用表格ID”：1
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。This prompt defines validation rules for different types of leave requests in a form. It ensures compliance with specific leave conditions based on the type of leave and prevents duplicate requests for overlapping dates.

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

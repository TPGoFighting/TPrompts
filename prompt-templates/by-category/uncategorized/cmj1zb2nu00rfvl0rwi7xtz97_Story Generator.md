# Story Generator

**Description:** Generate a story.

**Type:** TEXT
**Author:** f
**Created:** 2025-12-11T21:57:23.898Z
**Votes:** 1
**Views:** 0

**Tags:** Story

## Prompt Content

```
{
  "role": "Story Generator",
  "parameters": {
    "genre": "${Genre:fantasy, sci-fi, mystery, romance, horror}",
    "length": "${Length:short, medium, long}",
    "tone": "${Tone:dark, humorous, inspirational}",
    "protagonist": "string (optional description)",
    "setting": "string (optional setting description)"
  },
  "output_format": {
    "title": "string",
    "story": "string",
    "characters": [
      "string"
    ],
    "themes": [
      "string"
    ]
  },
  "instructions": "Generate a creative story based on the provided parameters. Include a compelling title, well-developed characters, and thematic elements."
}
```

**Source:** https://prompts.chat/prompts/cmj1zb2nu00rfvl0rwi7xtz97_story-generator

## 中文翻译

### 标题
故事生成器

### 提示词内容

```
{
  "role": "故事生成器",
  “参数”：{
    "genre": "${类型:奇幻、科幻、神秘、浪漫、恐怖}",
    "length": "${长度:短、中、长}",
    "tone": "${Tone:黑暗、幽默、励志}",
    "主角": "字符串（可选描述）",
    "setting": "字符串（可选设置描述）"
  },
  “输出格式”：{
    “标题”：“字符串”，
    “故事”：“字符串”，
    “字符”：[
      “串”
    ],
    “主题”：[
      “串”
    ]
  },
  "instructions": "根据提供的参数生成一个创意故事。包括引人注目的标题、发展良好的角色和主题元素。"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。Generate a story.

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
- `${Genre}`: 可自定义（默认值: fantasy, sci-fi, mystery, romance, horror）
- `${Length}`: 可自定义（默认值: short, medium, long）
- `${Tone}`: 可自定义（默认值: dark, humorous, inspirational）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

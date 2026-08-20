# Interactive Love Message HTML Page

**Description:** Create a simple and beautiful HTML page where a click reveals a love message.

**Type:** TEXT
**Author:** icymost
**Created:** 2026-08-16T14:29:58.317Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
Act as a Web Developer. You are tasked with creating a simple and visually appealing HTML page for a partner. Your task is to create an interactive page that displays a beautiful message when clicked.

You will:
- Use HTML to structure the page.
- Apply CSS for styling to make it attractive but not heavy.
- Use JavaScript to handle the click event and reveal a message saying 'دوستت دارم'.

Example:
```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love Message</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f8ff;
            font-family: Arial, sans-serif;
        }
        #message {
            display: none;
            font-size: 2em;
            color: #ff1493;
        }
    </style>
</head>
<body>
    <div id="message">دوستت دارم</div>
    <script>
        document.body.addEventListener('click', function() {
            var message = document.getElementById('message');
            message.style.display = 'block';
        });
    </script>
</body>
</html>
```
```

**Source:** https://prompts.chat/prompts/cmsvwixt90001k004rlsjuna0_interactive-love-message-html-page


## 中文翻译

### 标题
Interactive Love 消息 HTML 页面

### 提示词内容

```
【中文翻译说明】以下为英文提示词原文，请参考下方使用说明了解其用途和用法。

Act as a Web Developer. You are tasked with creating a simple and visually appealing HTML page for a partner. Your task is to create an interactive page that displays a beautiful message when clicked.

You will:
- Use HTML to structure the page.
- Apply CSS for styling to make it attractive but not heavy.
- Use JavaScript to handle the click event and reveal a message saying 'دوستت دارم'.

Example:
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。Create a simple and beautiful HTML page where a click reveals a love message.

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

# Automated Text Typing Every 5 Minutes with Python

**Description:** Create a Python script that automatically types a specified text every 5 minutes. The timer is customizable, and the script functions without manual keyboard input, allowing text to be typed on any writable interface.

**Type:** TEXT
**Author:** icymost
**Created:** 2026-06-26T15:12:07.508Z
**Votes:** 0
**Views:** 0

**Tags:** Automation, Productivity, Python

**Category:** Coding

## Prompt Content

```
Act as a Python Automation Engineer. You are skilled in creating scripts that automate repetitive tasks. Your task is to develop a Python script that types a specified text automatically every ${interval:5} minutes on any writable interface. The timer should be customizable.

You will:
- Use the `pyautogui` library to simulate keyboard input
- Implement a customizable timer using the `time` library
- Ensure the script runs continuously and types the text on any writable interface

Example Script:
```python
import pyautogui
import time

def auto_typing(text, interval):
    while True:
        pyautogui.typewrite(text)
        time.sleep(interval)

if __name__ == "__main__":
    # Customize your text and interval here
    text_to_type = "Your text here"
    time_interval = 300  # every 5 minutes
    auto_typing(text_to_type, time_interval)
```

To convert the Python script to an executable (.exe) file, follow these steps:
1. **Install PyInstaller**: Open your terminal or command prompt and run:
   ```
   pip install pyinstaller
   ```
2. **Create Executable**: Navigate to the directory containing your Python script and execute:
   ```
   pyinstaller --onefile your_script_name.py
   ```
3. **Find the .exe File**: After running PyInstaller, the executable will be located in the `dist` folder.

Rules:
- The script must run without manual keyboard interaction
- Ensure the interval and text are easy to update
- The script should be efficient and lightweight
```

**Source:** https://prompts.chat/prompts/cmqv2kpck0001jr044rji3nxj_automated-text-typing-every-5-minutes-with-python

## 中文翻译

### 标题
使用 Python 每 5 分钟自动输入一次文本

### 提示词内容

```
担任 Python 自动化工程师。您擅长创建自动执行重复任务的脚本。您的任务是开发一个 Python 脚本，该脚本每隔 ${interval:5} 分钟在任何可写界面上自动键入指定的文本。计时器应该是可定制的。

您将：
- 使用`pyautogui`库模拟键盘输入
- 使用“time”库实现可定制的计时器
- 确保脚本连续运行并在任何可写界面上键入文本

脚本示例：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Create a Python script that automatically types a specified text every 5 minutes. The timer is customizable, and the script functions without manual keyboard input, allowing text to be typed on any writable interface.

### 适用人群
开发者/程序员

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问
### 可自定义变量
- `${interval}`: 可自定义（默认值: 5）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

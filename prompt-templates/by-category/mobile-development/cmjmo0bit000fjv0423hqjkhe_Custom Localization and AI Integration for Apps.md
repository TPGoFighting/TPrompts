# Custom Localization and AI Integration for Apps

**Description:** Implement a user-preference-based localization system in your app with AI integration.

**Type:** TEXT
**Author:** ahmettzorlutuna
**Created:** 2025-12-26T09:24:16.086Z
**Votes:** 1
**Views:** 0

**Tags:** Mobile Development

**Category:** Mobile Development

## Prompt Content

```
Act as an App Localization Expert. You are tasked with setting up a user-preference-based localization architecture in an application independent of the phone's system language.

Your task includes:
1. **LanguageManager Class**: Create a `LanguageManager` class using the `ObservableObject` protocol. Store the user's selected language in `UserDefaults`, with the default language set to 'en' (English). Display a selection screen on the first launch.
2. **Global Locale Override**: Wrap the entire `ContentView` structure in your SwiftUI app with `.environment(\.locale, .init(identifier: languageManager.selectedLanguage))` to trigger translations based on the selected language in `LanguageManager`.
3. **Onboarding Language Selection**: If no language has been selected previously, show a stylish 'Language Selection' screen with English and Turkish options on app launch. Save the selection immediately and transition to the main screen.
4. **AI (LLM) Integration**: Add the user's selected language as a parameter in AI requests (API calls). Update the system prompt to: 'User's preferred language: ${selected_language}. Respond in this language.'
5. **String Catalogs**: Integrate `.stringxcatalog` into your project and add all existing hardcoded strings in English (base) and Turkish.
6. **Dynamic Update**: Ensure that changing the language in settings updates the UI without restarting the app.
7. **User Language Change**: Allow users to change the app's language dynamically at any time.

Rules:
- Ensure seamless user experience during language selection and updates.
- Test functionality for both English and Turkish languages.
```

**Source:** https://prompts.chat/prompts/cmjmo0bit000fjv0423hqjkhe_custom-localization-and-ai-integration-for-apps

## 中文翻译

### 标题
应用程序的自定义本地化和人工智能集成

### 提示词内容

```
担任应用程序本地化专家。您的任务是在独立于手机系统语言的应用程序中设置基于用户偏好的本地化架构。

你的任务包括：
1. **LanguageManager类**：使用`ObservableObject`协议创建一个`LanguageManager`类。将用户选择的语言存储在“UserDefaults”中，默认语言设置为“en”（英语）。首次启动时显示选择屏幕。
2. **全局区域设置覆盖**：使用 .environment(\.locale, .init(identifier: languageManager.selectedLanguage))` 包装 SwiftUI 应用程序中的整个 `ContentView` 结构，以根据 `LanguageManager` 中所选的语言触发翻译。
3. **入门语言选择**：如果之前未选择任何语言，则在应用程序启动时显示带有英语和土耳其语选项的时尚“语言选择”屏幕。立即保存选择并转换到主屏幕。
4. **AI (LLM) 集成**：将用户选择的语言添加为 AI 请求（API 调用）中的参数。将系统提示更新为：“用户的首选语言：${selected_language}”。用这种语言回应。
5. **字符串目录**：将 `.stringxcatalog` 集成到您的项目中，并添加英语（基本）和土耳其语的所有现有硬编码字符串。
6. **动态更新**：确保更改设置中的语言可以更新 UI，而无需重新启动应用程序。
7. **用户语言更改**：允许用户随时动态更改应用程序的语言。

规则：
- 确保语言选择和更新期间的无缝用户体验。
- 测试英语和土耳其语的功能。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Implement a user-preference-based localization system in your app with AI integration.

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
- `${selected_language}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

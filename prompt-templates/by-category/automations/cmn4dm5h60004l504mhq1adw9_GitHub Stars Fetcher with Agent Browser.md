# GitHub Stars Fetcher with Agent Browser

**Description:** Use the Agent Browser skill to automate logging into GitHub and retrieving starred projects of the currently logged-in user, sorted by star count. Contains complete execution steps, key notes, and troubleshooting.

**Type:** TEXT
**Author:** xiaostore
**Created:** 2026-03-24T08:52:17.082Z
**Votes:** 1
**Views:** 0

**Category:** Automations

## Prompt Content

```
# Using Agent Browser to Fetch GitHub Starred Projects

## Objective
Use the Agent Browser skill to log into GitHub and retrieve the starred projects of the currently logged-in user, sorted by the number of stars.

## Execution Steps (Follow in Order)

1. **Launch Browser and Open GitHub Homepage**
   ```bash
   agent-browser --headed --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github" open https://github.com && agent-browser wait --load networkidle
   ```

2. **Get Current Logged-in User Information**
   ```bash
   agent-browser snapshot -i
   # Find the user avatar or username link in the top-right corner to confirm login status
   # Extract the username of the currently logged-in user from the page
   ```

3. **Navigate to Current User's Stars Tab**
   ```bash
   # Construct URL: https://github.com/{username}?tab=stars
   agent-browser open https://github.com/{username}?tab=stars && agent-browser wait --load networkidle
   ```

4. **Sort by Stars Count (Most Stars First)**
   ```bash
   agent-browser snapshot -i  # First get the latest snapshot to find the sort button
   agent-browser click @e_sort_button  # Click the sort button
   agent-browser wait --load networkidle
   # Select "Most stars" from the dropdown options
   ```

5. **Retrieve and Record Project Information**
   ```bash
   agent-browser snapshot -i
   # Extract project name, description, stars, and forks information
   ```

## Critical Notes

### 1. Daemon Process Issues
- If you see "daemon already running", the browser is already running
- **Important:** When the daemon is already running, `--headed` and `--profile` parameters are ignored, and the browser continues in its current running mode
- You can proceed with subsequent commands without reopening
- To restart in headed mode, you must first execute: `agent-browser close`, then use the `--headed` parameter to reopen

### 2. Dynamic Nature of References
- Element references (@e1, @e2, etc.) change after each page modification
- You must execute `snapshot -i` before each interaction to get the latest references
- Never assume references are fixed

### 3. Command Execution Pattern
- Use `&&` to chain multiple commands, avoiding repeated process launches
- Wait for page load after each command: `wait --load networkidle`

### 4. Login Status
- Use the `--profile` parameter to specify a profile directory, maintaining login state
- If login expires, manually log in once to save the state

### 5. Windows Environment Variable Expansion
- **Important:** On Windows, environment variables like `%HOMEPATH%` must be expanded to actual paths before use
- **Incorrect:** `agent-browser --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github"`
- **Correct:** First execute `echo $HOME` to get the actual path, then use the expanded path
  ```bash
  # Get HOME path (e.g., /c/Users/xxx)
  echo $HOME
  # Use the expanded absolute path
  agent-browser --profile "/c/Users/xxx/.agent-browser/chrome-win64/chrome-profiles/github" --headed open https://github.com
  ```
- Without expanding environment variables, you'll encounter connection errors (e.g., `os error 10060`)

### 6. Sorting Configuration
- Click the "Sort by: Recently starred" button (typically reference e44)
- Select the "Most stars" option
- Retrieve page content again

## Troubleshooting Common Issues

| Issue | Solution |
|-------|----------|
| daemon already running | Execute subsequent commands directly, or close then reopen |
| Invalid element reference | Execute snapshot -i to get latest references |
| Page not fully loaded | Add wait --load networkidle |
| Need to re-login | Use --headed mode to manually login once and save state |
| Sorting not applied | Confirm you clicked the correct sorting option |

## Result Output Format
- Project name and link
- Stars count (sorted in descending order)
- Forks count
- Project description (if available)

```

**Source:** https://prompts.chat/prompts/cmn4dm5h60004l504mhq1adw9_github-stars-fetcher-with-agent-browser



---

## 中文翻译

### 标题
带有代理浏览器的 GitHub Stars Fetcher

### 提示词内容

```
# 使用代理浏览器获取 GitHub 星级项目

## 目标
使用代理浏览器技能登录 GitHub 并检索当前登录用户已加星标的项目，按星数排序。

## 执行步骤（按顺序执行）

1. **启动浏览器并打开 GitHub 主页**
   ````bash
   代理浏览器 --headed --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github" 打开 https://github.com && 代理浏览器等待 --load networkidle
   ````

2. **获取当前登录用户信息**
   ````bash
   代理浏览器快照 -i
   # 找到右上角的用户头像或用户名链接来确认登录状态
   # 从页面中提取当前登录用户的用户名
   ````

3. **导航到当前用户的星星选项卡**
   ````bash
   # 构造 URL: https://github.com/{username}?tab=stars
   代理浏览器打开 https://github.com/{用户名}?tab=stars && 代理浏览器等待 --load networkidle
   ````

4. **按星星数排序（星星最多的优先）**
   ````bash
   agent-browser snapshot -i # 首先获取最新的快照来找到排序按钮
   agent-browser click @e_sort_button # 单击排序按钮
   代理浏览器等待--加载网络空闲
   # 从下拉选项中选择“最多星星”
   ````

5. **检索并记录项目信息**
   ````bash
   代理浏览器快照 -i
   # 提取项目名称、描述、星星和分叉信息
   ````

## 重要说明

### 1. 守护进程问题
- 如果您看到“守护程序已在运行”，则浏览器已在运行
- **重要：** 当守护进程已经运行时， `--headed` 和 `--profile` 参数将被忽略，浏览器继续以当前运行模式
- 无需重新打开即可继续执行后续命令
- 要以 Headed 模式重新启动，必须先执行：`agent-browser close`，然后使用 `--headed` 参数重新打开

### 2. 参考文献的动态性质
- 元素引用（@e1、@e2 等）在每次页面修改后都会更改
- 每次交互之前必须执行`snapshot -i`以获取最新的参考
- 永远不要假设参考是固定的

### 3. 命令执行模式
- 使用“&&”链接多个命令，避免重复启动进程
- 每个命令后等待页面加载：`wait --load networkidle`

### 4. 登录状态
- 使用`--profile`参数指定配置文件目录，维护登录状态
- 如果登录过期，手动登录一次以保存状态

### 5.Windows环境变量扩展
- **重要：** 在 Windows 上，环境变量（例如 `%HOMEPATH%`）必须在使用前扩展为实际路径
- **不正确：** `agent-browser --profile "%HOMEPATH%\.agent-browser\chrome-win64\chrome-profiles\github"`
- **正确：** 首先执行 `echo $HOME` 获取实际路径，然后使用扩展后的路径
  ````bash
  # 获取 HOME 路径（例如 /c/Users/xxx）
  回显$HOME
  # 使用扩展后的绝对路径
  agent-browser --profile "/c/Users/xxx/.agent-browser/chrome-win64/chrome-profiles/github" --headed 打开 https://github.com
  ````
- 如果不扩展环境变量，您将遇到连接错误（例如“os error 10060”）

### 6. 排序配置
- 单击“排序方式：最近加星标”按钮（通常参考 e44）
- 选择“最多星星”选项
- 再次检索页面内容

## 常见问题故障排除

|问题 |解决方案 |
|--------|----------|
|守护进程已在运行 |直接执行后续命令，或​​者关闭然后重新打开 |
|无效的元素引用 |执行 snapshot -i 获取最新参考 |
|页面未完全加载|添加等待--load networkidle |
|需要重新登录 |使用--headed模式手动登录一次并保存状态|
|未应用排序 |确认您单击了正确的排序选项 |

## 结果输出格式
- 项目名称和链接
- 星星数量（按降序排列）
- 叉数
- 项目描述（如果有）
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**营销内容与SEO优化**类的提示词。Use the Agent Browser skill to automate logging into GitHub and retrieving starred projects of the currently logged-in user, sorted by star count. Contains complete execution steps, key notes, and troubleshooting.

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

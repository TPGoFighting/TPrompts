# Fix LaTeX dollars

**Description:** Investigate and fix the actual $ usages in Markdown content 

**Type:** TEXT
**Author:** aldinei
**Created:** 2026-06-15T14:24:05.700Z
**Votes:** 0
**Views:** 0

**Category:** Coding

## Prompt Content

```
Investigate and fix the actual $ usages in Markdown content.

The $ fall into three classes:

- Currency (escape these) — $1, $2 billion, R$ 549 → these pairs cause all the warnings
- Real math (leave alone) — $\rightarrow$, $O(1)\text{ streaming}$ → valid, no warnings
- Shell code (leave alone) — $(curl…), ${ZSH_CUSTOM}, $HOME → inside code blocks


Execute in 4 steps:

- Investigate — greps the content, classifies every $ into currency / real math / shell code, and reports counts before changing anything.
- Apply — checks the tree is clean, then writes and runs the exact tested Python script (code-fence-, inline-code-, frontmatter-, and math-span-aware; idempotent via the (?<!\\) lookbehind so re-running never double-escapes).
- Verify the diff — the safety net: greps that must print nothing for real math ($\rightarrow$, \text) and shell vars ($HOME, $(…), ${VAR}). If anything legit was touched, it tells you to git checkout -- . and stops.
- Print instructions — outputs the build-verify and commit/push commands for user to run.

Do not autonomously run any build, commit, or push.
```

**Source:** https://prompts.chat/prompts/cmqfb0kec0004l1043ahi3ys4_fix-latex-dollars

## 中文翻译

### 标题
修复 LaTeX 美元

### 提示词内容

```
调查并修复 Markdown 内容中的实际 $ 用法。

$ 分为三类：

- 货币（忽略这些）— 1 美元、20 亿美元、549 雷亚尔 → 这些货币对引起所有警告
- 真正的数学（不用管） - $\rightarrow$, $O(1)\text{ Streaming}$ → 有效，没有警告
- Shell 代码（不用管）— $(curl…)、${ZSH_CUSTOM}、$HOME → 代码块内


分4步执行：

- 调查 — grep 内容，将每一美元分类为货币/实际数学/shell 代码，并在更改任何内容之前报告计数。
- 应用 - 检查树是否干净，然后编写并运行经过精确测试的 Python 脚本（code-fence-、inline-code-、frontmatter- 和 math-span-aware；通过 (?<!\\) Lookbehind 实现幂等，因此重新运行不会出现双重转义）。
- 验证差异 - 安全网：对于实际数学（$\rightarrow$、\text）和 shell 变量（$HOME、$(…)、${VAR}），greps 必须不打印任何内容。如果触及任何合法内容，它会告诉您 git checkout -- 。并停止。
- 打印指令 — 输出构建验证和提交/推送命令供用户运行。

不要自主运行任何构建、提交或推送。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Investigate and fix the actual $ usages in Markdown content

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
- `${ZSH_CUSTOM}`: 需要您填写
- `${VAR}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整

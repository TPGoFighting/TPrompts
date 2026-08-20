# Create Python Dev Container

**Type:** TEXT
**Author:** bugyboo
**Created:** 2025-12-25T21:28:19.717Z
**Votes:** 0
**Views:** 0

**Tags:** Agent

**Category:** DevOps

## Prompt Content

```
You are a DevOps expert setting up a Python development environment using Docker and VS Code Remote Containers.

Your task is to provide and run Docker commands for a lightweight Python development container based on the official python latest slim-bookworm image.

Key requirements:
- Use interactive mode with a bash shell that does not exit immediately.
- Override the default command to keep the container running indefinitely (use sleep infinity or similar) do not remove the container after running.
- Name it py-dev-container
- Mount the current working directory (.) as a volume to /workspace inside the container (read-write).
- Run the container as a non-root user named 'vscode' with UID 1000 for seamless compatibility with VS Code Remote - Containers extension.
- Install essential development tools inside the container if needed (git, curl, build-essential, etc.), but only via runtime commands if necessary.
- Do not create any files on the host or inside the container beyond what's required for running.
- Make the container suitable for attaching VS Code remotely (Remote - Containers: Attach to Running Container) to enable further Python development, debugging, and extension usage.

Provide:
1. The docker pull command (if needed).
2. The full docker run command with all flags.
3. Instructions on how to attach VS Code to this running container for development.

Assume the user is in the root folder of their Python project on the host.
```

**Source:** https://prompts.chat/prompts/cmjlyfm6d000hjv04prhy8hsu_create-python-dev-container

## 中文翻译

### 标题
创建Python开发容器

### 提示词内容

```
您是一位使用 Docker 和 VS Code 远程容器设置 Python 开发环境的 DevOps 专家。

您的任务是为基于官方 python 最新 slim-bookworm 镜像的轻量级 Python 开发容器提供并运行 Docker 命令。

关键要求：
- 使用交互模式与不会立即退出的 bash shell。
- 覆盖默认命令以保持容器无限期运行（使用 sleep Infinity 或类似命令）运行后不删除容器。
- 将其命名为 py-dev-container
- 将当前工作目录 (.) 作为卷装载到容器内的 /workspace（读写）。
- 以名为“vscode”且 UID 1000 的非 root 用户身份运行容器，以便与 VS Code Remote - Containers 扩展无缝兼容。
- 如果需要，在容器内安装必要的开发工具（git、curl、build-essential 等），但如果需要，只能通过运行时命令安装。
- 不要在主机上或容器内创建超出运行所需的任何文件。
- 使容器适合远程附加 VS Code（远程 - 容器：附加到正在运行的容器），以实现进一步的 Python 开发、调试和扩展使用。

提供：
1. docker pull 命令（如果需要）。
2. 带有所有标志的完整 docker run 命令。
3. 如何将 VS Code 附加到此运行容器进行开发的说明。

假设用户位于主机上 Python 项目的根文件夹中。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Create Python Dev Container相关的任务。

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

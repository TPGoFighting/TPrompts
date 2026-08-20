# trello-integration-skill

**Description:** This skill allows you to interact with Trello account to list boards, view lists, and create cards automatically.

**Type:** SKILL
**Author:** mertogemini
**Created:** 2026-03-06T00:01:23.314Z
**Votes:** 0
**Views:** 0

**Tags:** Agent, Automation, Project Management, API, Claude, skills, Skill

**Category:** Agent Skill

## Prompt Content

```
---
name: trello-integration-skill
description: This skill allows you to interact with Trello account to list boards, view lists, and create cards automatically.
---

# Trello Integration Skill

The Trello Integration Skill provides a seamless connection between the AI agent and the user's Trello account. It empowers the agent to autonomously fetch existing boards and lists, and create new task cards on specific boards based on user prompts.

## Features
- **Fetch Boards**: Retrieve a list of all Trello boards the user has access to, including their Name, ID, and URL.
- **Fetch Lists**: Retrieve all lists (columns like "To Do", "In Progress", "Done") belonging to a specific board.
- **Create Cards**: Automatically create new cards with titles and descriptions in designated lists.

---

##  Setup & Prerequisites

To use this skill locally, you need to provide your Trello Developer API credentials.

1. Generate your credentials at the [Trello Developer Portal (Power-Ups Admin)](https://trello.com/app-key).
2. Create an API Key.
3. Generate a Secret Token (Read/Write access).
4. Add these credentials to the project's root `.env` file:

```env
# Trello Integration
TRELLO_API_KEY=your_api_key_here
TRELLO_TOKEN=your_token_here
```

---

##  Usage & Architecture

The skill utilizes standalone Node.js scripts located in the `.agent/skills/trello_skill/scripts/` directory.

### 1. List All Boards
Fetches all boards for the authenticated user to determine the correct target `boardId`.

**Execution:**
```bash
node .agent/skills/trello_skill/scripts/list_boards.js
```

### 2. List Columns (Lists) in a Board
Fetches the lists inside a specific board to find the exact `listId` (e.g., retrieving the ID for the "To Do" column).

**Execution:**
```bash
node .agent/skills/trello_skill/scripts/list_lists.js <boardId>
```

### 3. Create a New Card
Pushes a new card to the specified list. 

**Execution:**
```bash
node .agent/skills/trello_skill/scripts/create_card.js <listId> "<Card Title>" "<Optional Description>"
```
*(Always wrap the card title and description in double quotes to prevent bash argument splitting).*

---

##  AI Agent Workflow

When the user requests to manage or add a task to Trello, follow these steps autonomously:
1. **Identify the Target**: If the target `listId` is unknown, first run `list_boards.js` to identify the correct `boardId`, then execute `list_lists.js <boardId>` to retrieve the corresponding `listId` (e.g., for "To Do").
2. **Execute Command**: Run the `create_card.js <listId> "Task Title" "Task Description"` script.
3. **Report Back**: Confirm the successful creation with the user and provide the direct URL to the newly created Trello card.
FILE:create_card.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

const listId = process.argv[2];
const cardName = process.argv[3];
const cardDesc = process.argv[4] || "";

if (!listId || !cardName) {
    console.error(`Usage: node create_card.js <listId> "${card_name}" ["${card_description}"]`);
    process.exit(1);
}

async function createCard() {
    const url = `https://api.trello.com/1/cards?idList=${listId}&key=${API_KEY}&token=${TOKEN}`;

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: cardName,
                desc: cardDesc,
                pos: 'top'
            })
        });

        if (!response.ok) {
            const errText = await response.text();
            throw new Error(`HTTP error! status: ${response.status}, message: ${errText}`);
        }
        const card = await response.json();
        console.log(`Successfully created card!`);
        console.log(`Name: ${card.name}`);
        console.log(`ID: ${card.id}`);
        console.log(`URL: ${card.url}`);
    } catch (error) {
        console.error("Failed to create card:", error.message);
    }
}

createCard();
FILE:list_board.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

async function listBoards() {
    const url = `https://api.trello.com/1/members/me/boards?key=${API_KEY}&token=${TOKEN}&fields=name,url`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const boards = await response.json();
        console.log("--- Your Trello Boards ---");
        boards.forEach(b => console.log(`Name: ${b.name}\nID: ${b.id}\nURL: ${b.url}\n`));
    } catch (error) {
        console.error("Failed to fetch boards:", error.message);
    }
}

listBoards();
FILE:list_lists.js
const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '../../../../.env') });

const API_KEY = process.env.TRELLO_API_KEY;
const TOKEN = process.env.TRELLO_TOKEN;

if (!API_KEY || !TOKEN) {
    console.error("Error: TRELLO_API_KEY or TRELLO_TOKEN is missing from the .env file.");
    process.exit(1);
}

const boardId = process.argv[2];
if (!boardId) {
    console.error("Usage: node list_lists.js <boardId>");
    process.exit(1);
}

async function listLists() {
    const url = `https://api.trello.com/1/boards/${boardId}/lists?key=${API_KEY}&token=${TOKEN}&fields=name`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const lists = await response.json();
        console.log(`--- Lists in Board ${boardId} ---`);
        lists.forEach(l => console.log(`Name: "${l.name}"\nID: ${l.id}\n`));
    } catch (error) {
        console.error("Failed to fetch lists:", error.message);
    }
}

listLists();
```

**Source:** https://prompts.chat/prompts/cmme4q2y90004l7049abloaz7_trello-integration-skill

## 中文翻译

### 标题
Trello 集成技能

### 提示词内容

```
---
名称： trello 集成技能
描述：此技能允许您与 Trello 帐户交互以自动列出面板、查看列表和创建卡片。
---

# Trello 集成技巧

Trello 集成技能在 AI 代理和用户的 Trello 帐户之间提供无缝连接。它使代理能够自主获取现有的面板和列表，并根据用户提示在特定面板上创建新的任务卡。

## 特点
- **获取面板**：检索用户有权访问的所有 Trello 面板的列表，包括其名称、ID 和 URL。
- **获取列表**：检索属于特定面板的所有列表（“待办事项”、“进行中”、“完成”等列）。
- **创建卡片**：自动创建新卡片，其标题和描述位于指定列表中。

---

## 设置和先决条件

要在本地使用此技能，您需要提供您的 Trello Developer API 凭据。

1. 在 [Trello 开发者门户（Power-Ups 管理员）](https://trello.com/app-key) 生成您的凭据。
2. 创建 API 密钥。
3. 生成秘密令牌（读/写访问）。
4. 将这些凭据添加到项目的根 `.env` 文件中：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。This skill allows you to interact with Trello account to list boards, view lists, and create cards automatically.

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

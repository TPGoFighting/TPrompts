# TPrompts

TPrompts 是一个零运行时依赖的静态提示词检索站，包含提示词库、灵感和编辑策展三个板块。

## 本地开发

```bash
npm run check   # 校验数据、资源、HTML 和内联 JavaScript
npm test        # 运行静态站点冒烟测试
npm run build   # 生产前检查（静态站无需打包）
npm run serve   # http://127.0.0.1:4173
```

也可以直接双击 `index.html` 打开；站点使用 Hash 路由，不依赖后端服务。

## 数据更新

- `prompts-data.js`：提示词库生成数据。
- `inspire-data.js`：灵感板块生成数据。
- `curated-data.js`：编辑策展数据，手动维护。
- `build-data.js`、`build-inspire-data.py`：数据管线入口。

更新数据后至少执行 `npm run check && npm test`。不要把 `.env`、`__pycache__`、切分/翻译中间产物提交到版本库。

## 工程约定

- 页面保持纯静态，数据通过 `window.*_DATA` 注入，避免引入不必要的框架迁移成本。
- `scripts/check-project.mjs` 是生产前护栏：会校验数据结构、唯一 ID、策展引用、本地资源和入口脚本语法。
- GitHub Actions 会在 push 和 pull request 上执行 Node 检查、冒烟测试和 Python 语法检查。

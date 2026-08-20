/**
 * TPrompts 数据构建脚本
 * 扫描 Obsidian Vault 提示词模板目录，解析 frontmatter + 中英提示词 + 使用说明，
 * 生成 prompts-data.js（浏览器端直接 <script> 加载，兼容 file:// 协议）。
 *
 * 用法: node build-data.js
 */
const fs = require('fs');
const path = require('path');

const ROOT = 'C:/Users/17356/Documents/Obsidian Vault/提示词模板';
const OUT = path.join(__dirname, 'prompts-data.js');

/* ---------- 工具 ---------- */
function walk(dir, list = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'images') continue;
      walk(full, list);
    } else if (entry.name.endsWith('.md')) {
      list.push(full);
    }
  }
  return list;
}

function parseFrontmatter(md) {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return {};
  const fm = {};
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^(\w+):\s*"?([^"]*)"?$/);
    if (!kv) continue;
    const [, key, val] = kv;
    if (key === 'tags') continue; // 数组单独处理
    if (val === 'true' || val === 'false') fm[key] = val === 'true';
    else fm[key] = val.trim();
  }
  const tagsM = md.match(/^tags:\r?\n([\s\S]*?)^\w+:/m);
  if (tagsM) {
    fm.tags = tagsM[1].split(/\r?\n/).map(l => l.replace(/^\s*-\s*/, '').trim()).filter(Boolean);
  }
  return fm;
}

/**
 * 提取某个二级标题后的内容，直到下一个二级标题或文件尾。
 * 逐行扫描 + 追踪代码块围栏：section 内部的 `---` 分隔线和 `## ` 都不应误判。
 * 之前的正则实现因 `---` 是 section 内部子段分隔线，导致所有模板都被截断在第一个子段。
 */
function extractSection(md, headerRe) {
  // 定位 header
  const hRe = new RegExp(headerRe + '\\r?\\n+', '');
  const hM = md.match(hRe);
  if (!hM) return '';
  const start = hM.index + hM[0].length;
  // 逐行扫描：跳过 ``` 代码块，遇到非代码块内的 `## ` 停止
  let inFence = false;
  let end = md.length;
  const lines = md.slice(start).split(/\r?\n/);
  let consumed = 0;
  for (const line of lines) {
    if (/^\s*```/.test(line)) {
      inFence = !inFence;
    } else if (!inFence && /^##\s/.test(line)) {
      end = start + consumed;
      break;
    }
    consumed += line.length + 1; // +1 近似换行符
  }
  let body = md.slice(start, end).trim();
  // 去掉包裹的 ```text ... ``` 围栏
  body = body.replace(/^````?text\r?\n/, '').replace(/````?$/, '');
  // 清理末尾的 `---` 与 `*返回主目录：...*` 脚注
  body = body.replace(/\n*---\s*\n*\*返回主目录[^\n]*$/m, '').trim();
  return body;
}

/** 从使用说明里提炼一句简介：优先取「最佳适用场景」的粗体要点行 */
function makeDesc(fm, usage, zh) {
  for (const line of (usage || '').split(/\r?\n/)) {
    const m = line.match(/^- \*\*(.+?)\*\*：(.+)/);
    if (m) {
      const t = `${m[1]}：${m[2]}`.replace(/[`*[\]]/g, '').trim();
      if (t.length >= 10) return t.slice(0, 88);
    }
  }
  const zhFirst = (zh || '').split(/\r?\n/).find(l => l.trim().length > 15);
  return (zhFirst || `${fm.title} · ${fm.category || ''} 网页组件提示词模板`).slice(0, 88);
}

/* ---------- 主流程 ---------- */
const files = walk(ROOT);
const items = [];
const seen = new Set();
let skipped = 0;

/* ================= 分类归并：14 个目录 → 8 个笼统分类 ================= */
const CATEGORY_MAP = {
  'Hero 首屏': 'Hero 首屏',
  'Landing Page 落地页': 'Landing Page',
  '组件模块': '组件模块',
  'SaaS & 科技': 'SaaS & 商业',
  '商业 & 企业': 'SaaS & 商业',
  '金融 & 电商': '金融 & 电商',
  '健康 & 生活方式': '生活方式',
  '出行 & 娱乐': '生活方式',
  '创意 & 作品集': '创意 & 3D',
  '3D & 沉浸式': '创意 & 3D',
  '特殊页面': '其他页面',
  '移动端 & App': '其他页面',
  'Footer 页脚': '其他页面',
  '教育': '其他页面',
  '待归类': '其他页面',
  '美术资源来源': '其他页面'
};

for (const file of files) {
  const md = fs.readFileSync(file, 'utf8');
  const fm = parseFrontmatter(md);
  if (!fm.id) { skipped++; continue; }
  if (seen.has(fm.id)) { skipped++; continue; }
  seen.add(fm.id);

  const zh = extractSection(md, '## 🇨🇳 中文翻译提示词 \\(Chinese Prompt\\)');
  const en = extractSection(md, '## 🇺🇸 英文原版提示词 \\(English Prompt\\)');
  const usage = extractSection(md, '## 📖 中文使用说明与定制指南 \\(Usage Guide\\)');

  /* 正文里的本地预览图引用：![xxx|600](images/xxx.png) */
  const imgM = md.match(/!\[[^\]]*\]\((images\/([^)\s]+))\)/);
  const imgLocal = imgM ? imgM[2].replace(/[|].*$/, '') : '';

  const folder = path.basename(path.dirname(file));
  items.push({
    id: fm.id,
    title: fm.title || fm.id,
    cat: CATEGORY_MAP[folder] || folder,   // 归并后的笼统分类
    srcCat: folder,                        // 保留原始目录名（备用）
    type: fm.type || 'component',
    pageType: fm.page_type || '',
    free: !!fm.is_free,
    tags: [...new Set((fm.tags || []).filter(t => t && t !== '提示词'))],
    video: fm.video_preview_url || '',
    img: fm.image_preview_url || '',
    imgLocal: imgLocal,                    // 本地预览图（需站点 images/ 目录联接）
    desc: makeDesc(fm, usage, zh),
    zh: zh,
    en: en,
    usage: usage
  });
}

/* 统计体积 */
const zhBytes = items.reduce((s, i) => s + i.zh.length, 0);
const enBytes = items.reduce((s, i) => s + i.en.length, 0);
const usageBytes = items.reduce((s, i) => s + i.usage.length, 0);

const payload = `/* 由 build-data.js 自动生成 · ${new Date().toISOString()} */
/* 源目录: ${ROOT} */
window.PROMPTS_DATA = ${JSON.stringify(items)};\n`;

fs.writeFileSync(OUT, payload, 'utf8');
console.log(`✓ 生成 ${OUT}`);
console.log(`  提示词数量: ${items.length}（跳过 ${skipped} 个无 id 文件）`);
console.log(`  中文提示词: ${(zhBytes/1024).toFixed(0)} KB`);
console.log(`  英文原版  : ${(enBytes/1024).toFixed(0)} KB`);
console.log(`  使用说明  : ${(usageBytes/1024).toFixed(0)} KB`);
console.log(`  数据文件  : ${(payload.length/1024/1024).toFixed(2)} MB`);

/* 分类统计 */
const byCat = {};
for (const i of items) byCat[i.cat] = (byCat[i.cat] || 0) + 1;
console.log('\n分类统计:');
for (const [c, n] of Object.entries(byCat).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${c}: ${n}`);
}

#!/usr/bin/env node
/**
 * 将 prompts_new/all_cases.json 合并进提示词库。
 * 用法：node scripts/import-prompts-new.mjs /path/to/prompts_new
 *
 * 新条目全部 free=true，并以固定种子随机插入现有未上锁序列；
 * 已上锁条目保持在末尾，且相互之间维持原顺序。
 */
import { readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const sourceArg = process.argv[2] || '';
const sourceDir = path.resolve(sourceArg);
const sourceFile = path.join(sourceDir, 'all_cases.json');
const outputFile = path.join(ROOT, 'prompts-data.js');

if (!sourceArg || !path.isAbsolute(sourceArg)) {
  throw new Error('请传入 prompts_new 的绝对路径，例如 /Users/.../prompts_new');
}

function loadBrowserData(file, globalName) {
  const context = { window: {} };
  vm.runInNewContext(readFileSync(file, 'utf8'), context, { filename: file });
  return context.window[globalName];
}

function clean(value) {
  return typeof value === 'string' && value.trim() && value !== '$undefined' ? value.trim() : '';
}

function textOf(item) {
  return [item.title, item.summary, item.promptFull, item.category].map(clean).join(' ').toLowerCase();
}

function classify(item) {
  const text = textOf(item);
  if (/金融|电商|购物|支付|银行|fintech|e-?commerce|commerce|shop|store|checkout|pricing|wallet|crypto/.test(text)) return '金融 & 电商';
  if (/3d|three\.?js|webgl|shader|voxel|immersive|沉浸|粒子|particle|globe|space|太空|spline|canvas|体素|地图|map/.test(text)) return '创意 & 3D';
  if (/navbar|navigation|button|card|modal|carousel|slider|timeline|accordion|table|form|input|menu|loader|tooltip|component|组件|按钮|导航|卡片|弹窗|轮播|表单/.test(text)) return '组件模块';
  if (/saas|dashboard|analytics|crm|admin|startup|agency|business|enterprise|data|数据|商业|企业|管理|后台|分析|工作流|workflow/.test(text)) return 'SaaS & 商业';
  if (/hero|首屏|banner|above the fold/.test(text)) return 'Hero 首屏';
  if (/landing|落地页|homepage|home page|website|网页|portfolio|作品集|personal site|品牌官网/.test(text)) return 'Landing Page';
  if (/travel|restaurant|food|fitness|health|beauty|music|church|education|school|旅行|餐饮|美食|健身|健康|音乐|教育|生活/.test(text)) return '生活方式';
  return '其他页面';
}

function shortDescription(item) {
  const summary = clean(item.summary) || `${clean(item.title)} · AI 编程与 UI 设计案例`;
  return summary.replace(/\s+/g, ' ').slice(0, 180);
}

function usageText(item) {
  const notes = Array.isArray(item.promptContributionNotes)
    ? item.promptContributionNotes.filter(clean)
    : [];
  if (notes.length) return `### 使用方法与核心逻辑\n\n${notes.map((note, i) => `${i + 1}. ${note}`).join('\n\n')}`;
  return `### 使用方法与核心逻辑\n\n${shortDescription(item)}\n\n使用前请根据自己的技术栈、页面目标和素材链接替换提示词中的具体内容，并在真实环境中验证。`;
}

function mediaFields(item) {
  const media = clean(item.mediaUrl);
  const poster = clean(item.posterUrl) || clean(item.thumbnailUrl);
  if (item.mediaType === 'video') return { video: media, img: poster };
  return { video: '', img: media || poster };
}

function normalize(item, index) {
  const en = clean(item.promptFull) || '（暂无英文原文）';
  const translated = clean(item.promptTranslationZh);
  const media = mediaFields(item);
  const category = classify(item);
  return {
    id: `new-${clean(item.slug) || `case-${index + 1}`}`,
    title: clean(item.title) || `AI 编程案例 ${index + 1}`,
    cat: category,
    srcCat: clean(item.category) || 'AI 编程(UI)',
    type: 'AI 编程案例',
    pageType: category,
    free: true,
    isImported: true,
    translationPending: !translated,
    tags: [...new Set(['AI 编程', category, clean(item.mediaType) || 'case'])],
    ...media,
    desc: shortDescription(item),
    zh: translated || en,
    en,
    usage: usageText(item),
    creator: clean(item.creator),
    source: clean(item.source),
    sourceUrl: clean(item.sourceUrl),
    promptContributionNotes: Array.isArray(item.promptContributionNotes) ? item.promptContributionNotes : []
  };
}

/* 固定种子 Fisher-Yates：让位置随机，但每次导入结果一致，便于回滚和复现。 */
function seededRandom(seed) {
  let value = seed >>> 0;
  return () => {
    value += 0x6D2B79F5;
    let t = value;
    t = Math.imul(t ^ t >>> 15, t | 1);
    t ^= t + Math.imul(t ^ t >>> 7, t | 61);
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}

function randomSlots(total, count, random) {
  const slots = Array.from({ length: total }, (_, i) => i);
  for (let i = slots.length - 1; i > 0; i -= 1) {
    const j = Math.floor(random() * (i + 1));
    [slots[i], slots[j]] = [slots[j], slots[i]];
  }
  return new Set(slots.slice(0, count));
}

const source = JSON.parse(readFileSync(sourceFile, 'utf8'));
if (!Array.isArray(source) || source.length === 0) throw new Error('all_cases.json 不是非空数组');

const existing = loadBrowserData(path.join(ROOT, 'prompts-data.js'), 'PROMPTS_DATA');
const existingIds = new Set(existing.map(item => item.id));
const imported = source.map(normalize).filter(item => !existingIds.has(item.id));
const oldFree = existing.filter(item => item.free !== false);
const locked = existing.filter(item => item.free === false);
const random = seededRandom(20260821);
const slots = randomSlots(oldFree.length + imported.length, imported.length, random);
const free = [];
let oldIndex = 0;
let newIndex = 0;
for (let i = 0; i < oldFree.length + imported.length; i += 1) {
  free.push(slots.has(i) ? imported[newIndex++] : oldFree[oldIndex++]);
}

const merged = [...free, ...locked];
const payload = `/* TPrompts prompt library · imported from ${sourceDir} · deterministic mixed seed 20260821 */\nwindow.PROMPTS_DATA = ${JSON.stringify(merged)};\n`;
writeFileSync(outputFile, payload, 'utf8');

const counts = {};
for (const item of imported) counts[item.cat] = (counts[item.cat] || 0) + 1;
console.log(`导入完成：新增 ${imported.length} 条，未上锁 ${free.length} 条，已上锁 ${locked.length} 条`);
console.log('新增分类：', Object.entries(counts).sort((a, b) => b[1] - a[1]).map(([cat, count]) => `${cat} ${count}`).join(' · '));
console.log(`输出：${outputFile}`);

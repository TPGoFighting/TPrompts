import { readFileSync, existsSync } from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import vm from 'node:vm';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');

function fail(message) {
  throw new Error(message);
}

function assert(condition, message) {
  if (!condition) fail(message);
}

function read(relativePath) {
  const absolutePath = path.join(ROOT, relativePath);
  assert(existsSync(absolutePath), `缺少文件: ${relativePath}`);
  return readFileSync(absolutePath, 'utf8');
}

function loadBrowserData(relativePath, globalName) {
  const context = { window: {} };
  vm.runInNewContext(read(relativePath), context, { filename: relativePath });
  const value = context.window[globalName];
  assert(value !== undefined, `${relativePath} 未导出 window.${globalName}`);
  return value;
}

function assertUniqueIds(items, label) {
  const ids = items.map((item) => item.id);
  const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
  assert(duplicates.length === 0, `${label} 存在重复 id: ${[...new Set(duplicates)].join(', ')}`);
}

function assertRequiredFields(items, fields, label) {
  const invalid = items.findIndex((item) =>
    fields.some((field) => typeof item[field] !== 'string' || item[field].trim() === '')
  );
  assert(invalid === -1, `${label}[${invalid}] 缺少必填字段: ${fields.join(', ')}`);
}

function localFileExists(resource) {
  const cleanResource = decodeURIComponent(resource.split(/[?#]/, 1)[0]);
  return existsSync(path.join(ROOT, cleanResource));
}

function walkStrings(value, visit) {
  if (typeof value === 'string') {
    visit(value);
    return;
  }
  if (Array.isArray(value)) {
    value.forEach((item) => walkStrings(item, visit));
    return;
  }
  if (value && typeof value === 'object') {
    Object.values(value).forEach((item) => walkStrings(item, visit));
  }
}

function checkHtml(html) {
  assert(/^<!doctype html>/i.test(html), 'index.html 必须使用 HTML5 doctype');
  assert(/<html[^>]+lang=["']zh-CN["']/i.test(html), 'index.html 缺少 lang="zh-CN"');
  assert(/<title>[^<]+<\/title>/i.test(html), 'index.html 缺少页面标题');

  for (const script of ['prompts-data.js', 'inspire-data.js', 'curated-data.js', 'creator-data.js']) {
    assert(new RegExp(`<script[^>]+(?:src|data-lazy-src)=["']${script}["']`).test(html), `index.html 未加载 ${script}`);
  }

  const inlineScripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter((match) => !/\bsrc\s*=/.test(match[1]))
    .map((match) => match[2]);
  assert(inlineScripts.length > 0, 'index.html 缺少应用脚本');
  inlineScripts.forEach((script, index) => {
    new vm.Script(script, { filename: `index.html:inline-script-${index + 1}` });
  });

  const localResources = [...html.matchAll(/\b(?:src|href)=["']([^"']+)["']/gi)]
    .map((match) => match[1])
    .filter((resource) => /^(assets|images)\//.test(resource))
    .filter((resource) => !resource.includes('${'));
  localResources.forEach((resource) => {
    assert(localFileExists(resource), `index.html 引用了不存在的资源: ${resource}`);
  });
}

function checkJsonAssets() {
  for (const relativePath of ['tippy_manifest.json', 'tippy_scenes.json']) {
    const value = JSON.parse(read(relativePath));
    walkStrings(value, (resource) => {
      if (/^(assets|images)\//.test(resource)) {
        assert(localFileExists(resource), `${relativePath} 引用了不存在的资源: ${resource}`);
      }
    });
  }
}

export function checkProject() {
  const html = read('index.html');
  const prompts = loadBrowserData('prompts-data.js', 'PROMPTS_DATA');
  const inspiration = loadBrowserData('inspire-data.js', 'INSPIRE_DATA');
  const curated = loadBrowserData('curated-data.js', 'CURATED_DATA');
  const creators = loadBrowserData('creator-data.js', 'CREATOR_DATA');

  assert(Array.isArray(prompts) && prompts.length > 0, 'PROMPTS_DATA 必须是非空数组');
  assert(Array.isArray(inspiration) && inspiration.length > 0, 'INSPIRE_DATA 必须是非空数组');
  assertRequiredFields(prompts, ['id', 'title', 'cat', 'en', 'zh'], 'PROMPTS_DATA');
  assertRequiredFields(inspiration, ['id', 'title', 'cat', 'en', 'zh'], 'INSPIRE_DATA');
  assertUniqueIds(prompts, 'PROMPTS_DATA');
  assertUniqueIds(inspiration, 'INSPIRE_DATA');
  const importedPrompts = prompts.filter((prompt) => prompt.isImported);
  if (importedPrompts.length) {
    assertRequiredFields(importedPrompts, ['id', 'title', 'cat', 'en', 'zh', 'usage'], 'PROMPTS_DATA.imported');
    assert(importedPrompts.every((prompt) => prompt.free !== false), '导入提示词必须全部保持未上锁');
  }
  assert(creators && Array.isArray(creators.creators), 'CREATOR_DATA.creators 必须是数组');
  assert(creators && Array.isArray(creators.prompts), 'CREATOR_DATA.prompts 必须是数组');
  assertUniqueIds(creators.creators, 'CREATOR_DATA.creators');
  assertUniqueIds(creators.prompts, 'CREATOR_DATA.prompts');
  assertRequiredFields(creators.creators, ['id', 'name', 'bio'], 'CREATOR_DATA.creators');
  assertRequiredFields(creators.prompts, ['id', 'creatorId', 'title', 'prompt', 'sourceNote'], 'CREATOR_DATA.prompts');
  creators.creators.forEach((creator) => {
    if (creator.avatar) {
      assert(localFileExists(creator.avatar), `CREATOR_DATA.${creator.id} 缺少博主头像: ${creator.avatar}`);
    }
  });
  const creatorIds = new Set(creators.creators.map((creator) => creator.id));
  creators.prompts.forEach((prompt) => {
    assert(creatorIds.has(prompt.creatorId), `CREATOR_DATA 提示词找不到来源博主: ${prompt.creatorId}`);
  });

  prompts.forEach((prompt) => {
    if (prompt.imgLocal) {
      const resource = `images/${prompt.imgLocal}`;
      assert(localFileExists(resource), `PROMPTS_DATA.${prompt.id} 缺少本地预览图: ${resource}`);
      if (!/\.svg$/i.test(prompt.imgLocal)) {
        const thumbnail = `images/thumbs/${prompt.imgLocal}.webp`;
        assert(localFileExists(thumbnail), `PROMPTS_DATA.${prompt.id} 缺少本地缩略图: ${thumbnail}`);
      }
    }
  });

  assert(curated && Array.isArray(curated.sections), 'CURATED_DATA.sections 必须是数组');
  const promptIds = new Set(prompts.map((item) => item.id));
  const inspirationIds = new Set(inspiration.map((item) => item.id));
  curated.sections.forEach((section, sectionIndex) => {
    assert(typeof section.name === 'string' || sectionIndex > 0, `CURATED_DATA.sections[${sectionIndex}] 缺少 name`);
    assert(Array.isArray(section.items), `CURATED_DATA.sections[${sectionIndex}].items 必须是数组`);
    section.items.forEach((item) => {
      const ids = item.src === 'library' ? promptIds : inspirationIds;
      assert(item.src === 'library' || item.src === 'inspire', `策展条目来源无效: ${item.src}`);
      assert(ids.has(item.id), `策展条目找不到对应数据: ${item.src}/${item.id}`);
      assert(typeof item.note === 'string' && item.note.trim(), `策展条目缺少 note: ${item.id}`);
    });
  });

  checkHtml(html);
  checkJsonAssets();

  return {
    promptCount: prompts.length,
    inspirationCount: inspiration.length,
    curatedSectionCount: curated.sections.length,
    creatorCount: creators.creators.length,
    creatorPromptCount: creators.prompts.length,
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(new URL(import.meta.url).pathname)) {
  try {
    const result = checkProject();
    console.log(`项目检查通过：${result.promptCount} 条提示词、${result.inspirationCount} 条灵感、${result.curatedSectionCount} 个策展分区、${result.creatorCount} 位博主、${result.creatorPromptCount} 条博主提示词`);
  } catch (error) {
    console.error(`项目检查失败：${error.message}`);
    process.exitCode = 1;
  }
}

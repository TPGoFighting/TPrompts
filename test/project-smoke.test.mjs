import test from 'node:test';
import assert from 'node:assert/strict';
import { checkProject } from '../scripts/check-project.mjs';

test('静态站点的数据、资源和入口脚本完整', () => {
  const result = checkProject();

  assert.ok(result.promptCount > 400);
  assert.ok(result.inspirationCount > 2000);
  assert.ok(result.curatedSectionCount > 0);
});

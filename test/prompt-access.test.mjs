import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const context = { window: {} };
vm.runInNewContext(
  fs.readFileSync(new URL('../prompt-access.js', import.meta.url), 'utf8'),
  context,
  { filename: 'prompt-access.js' },
);

const { isLocked, sortByAccess } = context.window.TPROMPT_ACCESS;

test('free false prompts are locked and free prompts stay available', () => {
  assert.equal(isLocked({ free: false }), true);
  assert.equal(isLocked({ free: true }), false);
});

test('available prompts come first while preserving source order within each group', () => {
  const prompts = [
    { id: 'locked-first', free: false },
    { id: 'free-first', free: true },
    { id: 'free-second', free: true },
    { id: 'locked-second', free: false },
  ];

  assert.deepEqual(
    sortByAccess(prompts).map((prompt) => prompt.id),
    ['free-first', 'free-second', 'locked-first', 'locked-second'],
  );
  assert.deepEqual(prompts.map((prompt) => prompt.id), [
    'locked-first',
    'free-first',
    'free-second',
    'locked-second',
  ]);
});

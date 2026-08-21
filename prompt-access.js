(function exposePromptAccess(global) {
  function isLocked(prompt) {
    return prompt?.free === false;
  }

  function sortByAccess(prompts) {
    return prompts
      .map((prompt, index) => ({ prompt, index }))
      .sort((a, b) => Number(isLocked(a.prompt)) - Number(isLocked(b.prompt)) || a.index - b.index)
      .map(({ prompt }) => prompt);
  }

  global.TPROMPT_ACCESS = { isLocked, sortByAccess };
})(window);

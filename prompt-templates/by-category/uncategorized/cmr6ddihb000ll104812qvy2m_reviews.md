# reviews

**Description:** reviews

**Type:** TEXT
**Author:** kennynah85
**Created:** 2026-07-04T12:59:55.728Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
Objective: Summarize many reviews

1. **Process available reviews**

    * Note the number of reviews and remember that value as "number_reviews"
    * Overall rating
    * Rating distribution if visible
    * It's possible there aren't any reviews, for example if a product is new or out of stock. If that's the case, don't include any review analysis in your response.

2. **Identify repeated patterns**

    * Common positive themes
    * Common complaints
    * Frequency of each theme

3. **Support themes with evidence**

    * Representative quotes for major themes
    * Specific examples that illustrate points

4. **Evaluate trustworthiness**

    * Do reviews seem genuine?
    * Suspicious patterns (all 5-star, generic language)
    * Verified purchase indicators

5. **Summarize overall sentiment**

    * Would most reviewers buy again?
    * Who loves it vs. who hates it?

6. **Handling exceptions**

    Prioritize excellent content in your response. If you're unable to formulate a response that meets all criteria, you should
    * respond as best you can and
    * acknowledge any limitations or challenges you faced. For example, maybe there wasn't sufficient content on a webpage or the content wasn't compatible with a given request.

    Consider your proposed response objectively and rate it on a scale from 1-10. If you wouldn't give it a 10, either try to create a stronger response or consider acknowledging any limitations or challenges you faced. The score is just for your own purposes; don't share it with the user.

7. **Final response**

    If you have relevant info to share, your final response should follow standard writing guidelines, including:

    * Sentence case: titles, labels, and all other content should be displayed using sentence case (only proper nouns and the first letter of a string appear capitalized).
    * Favor simple sentences that use common words
    If number_reviews is 0, your response should mention that there aren't any reviews and you should jump to the follow-on question.

    **Overview:** [X] reviews, [Y] average rating

    **Pros**

    | Theme | Frequency | Example |
    | :---: | :---: | :---: |

    **Cons**

    | Theme | Frequency | Example |
    | :---: | :---: | :---: |

    **Quality of reviews:** [Do they seem genuine?]

    **Bottom line:** [Would most reviewers buy again?]

8. **Follow-up questions**

    If you can think of a way you can help the user act on information shown in the response, conclude with one (at most two) sentences that offers this help. Frame it as a question so that a simple response like "yes please" might launch the next round.
```

**Source:** https://prompts.chat/prompts/cmr6ddihb000ll104812qvy2m_reviews


## 中文翻译

### 标题
reviews

### 提示词内容

```
【中文翻译说明】以下为英文提示词原文，请参考下方使用说明了解其用途和用法。

Objective: Summarize many reviews

1. **Process available reviews**

    * Note the number of reviews and remember that value as "number_reviews"
    * Overall rating
    * Rating distribution if visible
    * It's possible there aren't any reviews, for example if a product is new or out of stock. If that's the case, don't include any review analysis in your response.

2. **Identify repeated patterns**

    * Common positive themes
    * Common complaints
    * Frequency of each theme

3. **Support themes with evidence**

    * Representative quotes for major themes
    * Specific examples that illustrate points

4. **Evaluate trustworthiness**

    * Do reviews seem genuine?
    * Suspicious patterns (all 5-star, generic language)
    * Verified purchase indicators

5. **Summarize overall sentiment**

    * Would most reviewers buy again?
    * Who loves it vs. who hates it?

6. **Handling exceptions**

    Prioritize excellent content in your response. If you're unable to formulate a response that meets all criteria, you should
    * respond as best you can and
    * acknowledge any limitations or challenges you faced. For example, maybe there wasn't sufficient content on a webpage or the content wasn't compatible with a given request.

    Consider your proposed response objectively and rate it on a scale from 1-10. If you wouldn't give it a 10, either try to create a stronger response or consider acknowledging any limitations or challenges you faced. The score is just for your own purposes; don't share it with the user.

7. **Final response**

    If you have relevant info to share, your final response should follow standard writing guidelines, including:

    * Sentence case: titles, labels, and all other content should be displayed using sentence case (only proper nouns and the first letter of a string appear capitalized).
    * Favor simple sentences that use common words
    If number_reviews is 0, your response should mention that there aren't any reviews and you should jump to the follow-on question.

    **Overview:** [X] reviews, [Y] average rating

    **Pros**

    | Theme | Frequency | Example |
    | :---: | :---: | :---: |

    **Cons**

    | Theme | Frequency | Example |
    | :---: | :---: | :---: |

    **Quality of reviews:** [Do they seem genuine?]

    **Bottom line:** [Would most reviewers buy again?]

8. **Follow-up questions**

    If you can think of a way you can help the user act on information shown in the response, conclude with one (at most two) sentences that offers this help. Frame it as a question so that a simple response like "yes please" might launch the next round.
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。reviews

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

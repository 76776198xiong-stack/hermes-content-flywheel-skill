---
name: content-flywheel
description: Use when a creator wants Hermes to turn raw thoughts, notes, conversations, user questions, or drafts into publishable content through a repeatable content flywheel. Handles topic judgment, one-fish-many-uses repurposing, short-video scripts, posts, article outlines, publishing copy, feedback review, and gradual style learning from the user's edits.
version: 0.1.0
author: Mirror Content System
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [content-creation, creator-workflow, short-video, repurposing, style-learning]
    related_skills: []
---

# Content Flywheel

## Overview

This skill helps a creator turn everyday thinking into a repeatable content system:

```text
raw thought / conversation / user question
-> core insight
-> topic decision
-> publishable content package
-> user edit
-> style learning
-> publishing feedback
-> better next topic
```

The goal is not to generate generic "AI copy." The goal is to reduce blank-page friction while preserving the creator's judgment, taste, and lived experience.

## When to Use

Use this skill when the user asks to:

- turn a messy thought into a short video script, post, article, or content package
- choose today's topic from several ideas
- do "one fish, many uses" repurposing from one idea into multiple formats
- make content for short video, X/Twitter, Xiaohongshu, WeChat, newsletter, community, or course/product material
- compare AI draft vs user-edited draft and learn the user's voice
- review published content data and extract next topics or style rules
- build a daily content workflow after Hermes installation

Don't use this skill for:

- pure literary writing with no publishing or audience goal
- brand strategy divorced from producing a concrete next piece
- automatic posting or platform scraping unless the user explicitly asks and the required tools are available
- pretending to learn the user's style without seeing their edits or examples

## First Run

If the user is using this skill for the first time, ask only the minimum needed to start:

1. What do you create? short video, text posts, articles, community answers, courses, or a mix.
2. Who are you trying to help?
3. What result should the audience get after consuming your content?
4. What topics must Hermes avoid or treat carefully?
5. Paste one piece that sounds like you, if available.

If file tools are available, initialize a workspace by running:

```sh
python3 scripts/init_content_workspace.py --root .
```

The generated `content-workspace/` folder is optional. If files are unavailable, continue in chat and keep the same structure in the response.

## Operating Modes

Infer the mode from the user's request. If unclear, default to **Daily One-Fish**.

| Mode | Trigger | Output |
|---|---|---|
| Onboarding | "帮我初始化", "这是我的定位", "先认识我" | creator profile + first content lanes |
| Daily One-Fish | "今天发什么", "这段思考能做什么" | topic decision + one content package |
| Repurpose | "一鱼多吃", "改成推文/文章/视频" | multiple format variants from one idea |
| Script | "写口播", "写视频稿" | hook + script + title/cover/publishing copy |
| Style Learning | "这是我改后的版本", "学习我的风格" | style rules with examples and confidence |
| Review | "复盘这条内容", "数据如下" | diagnosis + next experiments + reusable lessons |

## Daily One-Fish Flow

When the user gives a raw thought, do the work in this order:

1. **Extract the fish**: identify the strongest claim, tension, story, or practical method.
2. **Judge the topic**: decide go / no-go / needs sharpening.
3. **Choose the lane**: short video, text post, article, community answer, product material, or multiple.
4. **Make the package**: produce the smallest useful publishable set.
5. **Ask for correction**: invite the user to correct logic, tone, or personal truth.
6. **Learn only from evidence**: after edits, update style rules or summarize what changed.

Use this decision gate:

| Gate | Question |
|---|---|
| Real pain | Does this hit a real stuck point, desire, confusion, or argument? |
| Distinct view | Does the creator have a non-generic judgment or lived angle? |
| Platform hook | Can it be opened with a concrete hook in 1-3 seconds? |
| Business relevance | Does it attract the right people or deepen trust with them? |

If fewer than 2 gates pass, don't write a polished draft. Instead, state why and offer 2-3 sharper angles.

## Default Content Package

For most requests, output this compact package:

```markdown
**判断**
go / no-go / needs-sharpening

**核心洞察**
One sentence.

**适合载体**
Primary format + optional repurposes.

**短视频口播**
- 开头钩子
- 正文
- 收束/行动

**一鱼多吃**
- 短帖版
- 长文提纲
- 金句 3 条
- 评论/社群回答版

**发布包装**
- 封面大字
- 标题
- 简介/配文
- CTA

**需要用户确认**
1-3 concrete checks.
```

Adjust length to the user's requested platform. For short video, prefer spoken rhythm and concrete scenes over abstract thesis statements.

## Voice And Style Learning

Only learn from evidence:

- original AI draft + user's edited draft
- multiple examples written by the user
- explicit corrections such as "我不会这样说", "这个不像我", "这个逻辑错了"

When learning, record rules in this shape:

```markdown
## Style Rule
- rule:
- before:
- after:
- why:
- confidence: low / medium / high
- apply_to: hooks / script body / titles / CTA / all
```

Never replace the user's judgment with a style rule. If a style rule conflicts with today's content truth, ask or explain the tradeoff.

For detailed style-learning procedure, read `references/style-learning.md`.

## References

Load only what is needed:

- `references/workflow.md`: detailed workflows, output shapes, and one-fish-many-uses variants.
- `references/creator-profile-template.md`: profile fields and onboarding notes.
- `references/style-learning.md`: evidence-based style learning and rule update method.
- `references/publishing-rubric.md`: hook, script, title, CTA, and review checklist.

## Common Pitfalls

1. **Overbuilding the system before publishing.** Always produce the next publishable artifact first, then improve the system from the artifact.
2. **Making the user fill a long template.** Ask a few high-leverage questions, then draft.
3. **Writing generic advice.** Preserve the user's strange, specific, lived angle.
4. **Confusing repurposing with copy-paste.** Each platform needs a different job: attention, trust, action, or depth.
5. **Claiming style learning too early.** Learn from edits and examples, not from vibes.
6. **Hiding the judgment.** Always say whether the idea is worth publishing now.

## Verification Checklist

- [ ] The response identifies the core insight before drafting.
- [ ] The topic is judged go / no-go / needs-sharpening.
- [ ] The output includes at least one publishable artifact.
- [ ] Repurposed variants have different platform jobs.
- [ ] Any style rule is backed by user edits or examples.
- [ ] The next action is concrete enough for the user to publish, record, or correct.

## Update Record

| Date | Change | Reason |
|---|---|---|
| 2026-06-14 | Created v0.1.0 Hermes content flywheel skill | Package the creator workflow into a portable Hermes skill after installation |

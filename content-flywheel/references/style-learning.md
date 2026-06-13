# Style Learning

## Principle

Hermes learns the creator's style from evidence, not assumptions.

Good evidence:

- an AI draft and the user's edited version
- 3-5 user-written examples
- direct corrections from the user
- published pieces with notes about what worked

Weak evidence:

- "write like me" with no example
- a vague preference such as "高级一点"
- one isolated sentence with no context

## Compare Drafts

When given an AI draft and user edit:

1. Compare sentence length.
2. Compare opening style.
3. Compare use of examples and concrete scenes.
4. Compare emotional temperature.
5. Compare forbidden phrases or AI-sounding phrases removed by the user.
6. Compare what logic the user added, removed, or reordered.

Output:

```markdown
**差距**
1. ...
2. ...

**可学习规则**
- rule:
- before:
- after:
- why:
- confidence:
- apply_to:

**下次生成时我会**
1. ...
2. ...
```

## Rule Confidence

| Confidence | Use when |
|---|---|
| low | one weak signal or uncertain preference |
| medium | repeated once or directly stated by user |
| high | repeated across several edits/examples |

Do not overfit high-confidence rules from a single draft.

## Common Style Fixes

| Problem | Fix |
|---|---|
| Too generic | add lived scene, user-specific judgment, or a concrete contradiction |
| Too polished | make it more spoken and less symmetrical |
| Too abstract | add one concrete example before the concept |
| Too instructional | add the creator's discovery process or emotional stake |
| Too promotional | lower CTA level and restore content value |
| Too long | keep one insight and one action |

## Style Memory Format

```markdown
# Style Rules

## Hooks
- rule:
- example:
- confidence:

## Body
- rule:
- example:
- confidence:

## Titles
- rule:
- example:
- confidence:

## CTA
- rule:
- example:
- confidence:

## Forbidden
- phrase:
- reason:
- replacement:
```

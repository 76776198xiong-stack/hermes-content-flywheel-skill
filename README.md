# Hermes Content Flywheel Skill

`content-flywheel` is a portable Hermes skill for creators who want an AI-assisted content workflow:

```text
raw thought / conversation / user question
-> core insight
-> topic decision
-> one-fish-many-uses content package
-> user edit
-> style learning
-> publishing review
-> better next topic
```

It helps Hermes support short-video scripts, posts, article outlines, publishing copy, content repurposing, feedback review, and gradual voice learning from the creator's edits.

## Install From GitHub

One-line install:

```sh
curl -fsSL https://raw.githubusercontent.com/76776198xiong-stack/hermes-content-flywheel-skill/1cf0888125032b6656bb2b3bb40aa344dd098972/install.sh | bash
```

Or clone first:

```sh
git clone https://github.com/76776198xiong-stack/hermes-content-flywheel-skill.git
cd hermes-content-flywheel-skill
./install.sh
```

Verify:

```sh
hermes skills list | grep content-flywheel
```

## Use

Start Hermes and ask things like:

```text
用 content-flywheel 帮我把这段思考做成今天能发的一条视频。
```

```text
这是一段我改后的文案，请学习我的风格，下次写得更像我。
```

```text
这条内容的数据是这样，帮我复盘并给下一条选题。
```

## Optional Workspace

After installation, initialize a small creator workspace in any project folder:

```sh
python3 ~/.hermes/skills/social-media/content-flywheel/scripts/init_content_workspace.py --root .
```

This creates:

- `content-workspace/creator-profile.md`
- `content-workspace/style-rules.md`
- `content-workspace/idea-inbox.md`
- `content-workspace/published-log.csv`
- `content-workspace/review-notes.md`

## Package Layout

```text
content-flywheel/
  SKILL.md
  references/
    creator-profile-template.md
    publishing-rubric.md
    style-learning.md
    workflow.md
  scripts/
    init_content_workspace.py
install.sh
```

## License

MIT

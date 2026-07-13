# voice-cloner

A Claude Code skill that clones the written voice of a person or brand from real samples and produces a reusable voice skill at `<name>-voice/SKILL.md`.

The generated file works without adaptation as a Claude Code skill, a ChatGPT custom instruction, or a system prompt for any API.

This project works with written voice—idiolect and textual tone of voice. It does not clone audio.

## The problem it solves

Asking an AI to "write like someone" from two samples usually produces parody or generic copy. The model fills the gaps with its defaults: polished, agreeable text that says very little.

voice-cloner enforces a three-phase process that cannot be skipped. It first collects labeled samples and separates speech from writing. It then analyzes the material with cited evidence and calibration questions. Only after human validation does it generate the final voice skill.

## Installation

Install it as a personal skill available across projects:

```bash
git clone https://github.com/criminaly-vicious/voice-cloner.git ~/.claude/skills/voice-cloner
```

Or install it as a project skill versioned with your team's repository:

```bash
git clone https://github.com/criminaly-vicious/voice-cloner.git .claude/skills/voice-cloner
```

Restart Claude Code after installation. The skill activates when you make requests such as "clone my client's voice," "extract this brand's tone of voice," or "create a style guide from these texts."

## Usage

Ask in natural language and provide the source material:

```text
Clone my brand's voice. I will send you the website, three campaign emails,
and the tone guide our agency delivered last year.
```

The skill asks for missing material, produces a voice report supported by cited evidence, asks calibration questions, and only then generates the final `SKILL.md`.

Validate the generated file with:

```bash
python3 scripts/validate_skill.py path/to/name-voice/SKILL.md
```

The validator does not judge whether the voice sounds right; only the voice owner can do that. It catches structural problems, missing required sections, leftover placeholders, and common AI writing patterns.

The test that matters is the blind test described in `SKILL.md`: show the voice owner one generated text and one real text without identifying either. If they immediately identify the generated version, the skill is not ready.

## Without Claude Code

Copy the contents of [standalone-prompt.md](standalone-prompt.md) into Claude, ChatGPT, Gemini, or another AI assistant. The complete three-phase process runs inside the conversation.

## Project structure

```text
voice-cloner/
|-- SKILL.md                         Main instructions and three-phase workflow
|-- standalone-prompt.md             Portable prompt for any AI assistant
|-- references/
|   |-- voice-extraction-protocol.md Six analysis dimensions
|   |-- brand-vs-person.md           How brand voice analysis differs
|   `-- anti-patterns.md             Failure modes and common AI patterns
|-- templates/
|   |-- TEMPLATE-voice-skill.md      Generated document skeleton
|   `-- collection-form.md           Material to request before analysis
|-- examples/
|   `-- trail-voice.md               Complete fictional brand example
`-- scripts/
    `-- validate_skill.py            Dependency-free structural validator
```

## Requirements

Python 3.8 or newer is required to run the validator. No external libraries are needed.

## Contributing

Contributions to the skill, templates, examples, references, and validator are welcome. All repository content, branch names, commit messages, and pull request descriptions must be written in English.

This repository follows [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow):

1. Update your local `main` and create a short-lived branch from it. Use a descriptive prefix such as `feat/`, `fix/`, `docs/`, `refactor/`, or `test/`.
2. Make one focused change and update every affected example, template, reference, and validator rule.
3. Validate the example skill before opening a pull request:

   ```bash
   python3 scripts/validate_skill.py examples/trail-voice.md
   ```

4. Commit using [Conventional Commits](https://www.conventionalcommits.org/), for example `feat: add interview voice samples`, `fix: detect unresolved placeholders`, or `docs: clarify the calibration workflow`.
5. Push the branch and open a pull request against `main`. Explain the problem, the chosen approach, and how you tested it.
6. Keep the branch current with `main`, address review feedback, and merge only after validation passes. Do not commit directly to `main`.

When changing the generated voice-skill format, update `templates/TEMPLATE-voice-skill.md`, `standalone-prompt.md`, the validator, and the example in the same pull request so the contract stays consistent.

## Consent

Voice is an identity asset. Use only material you have the right to use, whether the voice is yours or belongs to a client or employer. The skill refuses requests intended for false attribution or impersonation.

## License

MIT. See [LICENSE](LICENSE).

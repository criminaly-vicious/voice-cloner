---
name: voice-cloner
description: Extracts a person's idiolect or a brand's tone of voice from real writing, transcribed speech, or brand material, then generates a reusable voice skill (SKILL.md) that enables any AI to write in that voice. Use when someone asks to clone a voice, capture a writing style, extract tone of voice, create a brand voice, build a style guide from examples, train an AI to write like a specific person, or turn writing samples into a style prompt. Also use when auditing or correcting an existing voice skill that produces generic text.
---

# Voice Cloner

This skill turns real samples into a usable voice skill. The final product is a `<name>-voice/SKILL.md` file that works without adaptation as a Claude Code skill, a ChatGPT custom instruction, or a system prompt for any API.

The classic failure in this work is giving an AI two samples, skipping directly to generation, and letting it invent the rest. This skill prevents that. Its three mandatory phases must be completed in order.

## Before anything else: consent and scope

Voice is an identity asset. Before starting, confirm that the requester has the right to use the material because the voice is theirs or belongs to their client or employer. If the request is to imitate an unrelated person for impersonation, fraud, or false attribution, refuse and explain why in one sentence without lecturing.

This skill works only with written voice—idiolect and textual tone of voice. It does not clone audio.

## Phase 1: Collection

Never analyze before collecting enough material. Request the samples and explain why each type matters.

For an individual, the minimum viable set is:

- Five samples of carefully written text, such as long emails, posts, documents, or substantial messages. Label each with its audience, purpose, and formality.
- Three speech samples, such as audio transcripts, dictated messages, or meeting excerpts. Mark them explicitly as speech because speech and writing are separate systems and must be analyzed separately.
- An explicit note identifying samples edited by someone else or written with AI assistance. These samples contaminate the signal and should carry less weight or be excluded.

For a brand, the minimum viable set is:

- Published text from at least three channels, such as the website, email, social media, documentation, or sales proposals. Brands often use different registers by channel.
- Any existing brand guide, manifesto, mission statement, or internal glossary, even when outdated. These materials reveal declared intent and make it possible to compare intent with actual practice.
- Examples the brand considers off-tone, when available. Counterexamples are some of the most efficient evidence you can collect.

If every sample comes from the same context, state the limitation and ask for other registers before continuing. If the requester chooses to proceed with too little material, continue but mark every hypothesis that is not supported by evidence in the final document.

The complete collection form is in [templates/collection-form.md](templates/collection-form.md).

## Phase 2: Analysis and voice report

Analyze the samples using the dimensions in [references/voice-extraction-protocol.md](references/voice-extraction-protocol.md): vocabulary, syntax, rhythm, punctuation, argument structure, personal markers, tone by context, and differences between speech and writing.

The most important step is isolating invariants: traits that appear across registers and channels. Invariants form the core of the voice and receive the highest priority in the final skill. A trait found in only one sample is noise until supported by more evidence.

End the phase with a voice report containing three parts:

- Findings, with every claim supported by a direct excerpt from the samples. A claim without evidence is an invention.
- What could not be determined confidently, stated openly instead of filled with guesses.
- Three to five calibration questions in the form "Would you say X or Y in this situation?" Use concrete pairs built from the gaps in the evidence.

Move to Phase 3 only after the requester validates the report.

## Phase 3: Voice skill generation

Generate the final document using [templates/TEMPLATE-voice-skill.md](templates/TEMPLATE-voice-skill.md). Write it in the language of the samples; never translate the generated voice skill unless explicitly requested.

The final document must follow these quality rules:

- Calibrated examples matter more than abstract rules because an AI learns voice more reliably from examples. Each incorrect/correct pair must address the same topic. The incorrect version must be plausible generic AI writing, not a ridiculous straw man.
- Make every instruction operational and positive when possible, such as "open with the context in one sentence" instead of a vague prohibition such as "do not be generic."
- Make each rule specific enough that two different AIs following it produce similar text. A statement that allows ten interpretations is not a rule.
- Include no trait unless it appears in the samples or was confirmed through calibration. When uncertain, leave it out because false positives turn imitation into parody.

Run validation after generation:

```bash
python3 scripts/validate_skill.py path/to/<name>-voice/SKILL.md
```

The script checks frontmatter, description length, required sections, placeholders, and common AI writing patterns. It does not judge voice accuracy; it only prevents structurally broken output.

## Acceptance test

A voice skill is ready only after passing this test. Generate a new text on a topic absent from the samples. Show it to the voice owner beside one of their real texts without identifying either. If they hesitate before identifying the generated text, the skill works. If they identify it immediately, return to Phase 2 and determine which trait is missing.

## Special cases

A brand is not a person. The protocol changes because a brand has multiple authors, needs stricter rules, and often has a declared tone that differs from its practiced tone. See [references/brand-vs-person.md](references/brand-vs-person.md).

Common failure modes—including falling back to generic AI writing, mistaking a verbal crutch for a style signature, or copying subject matter instead of voice—are cataloged in [references/anti-patterns.md](references/anti-patterns.md). Read it before generation, not after.

## Using the process without Claude Code

Anyone who does not use Claude Code can paste [standalone-prompt.md](standalone-prompt.md) into another AI assistant and run the same three-phase process in the conversation.

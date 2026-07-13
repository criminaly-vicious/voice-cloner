# Anti-patterns

A catalog of failure modes that appear whenever someone tries to clone a voice without a method. Read this before generation. Once a text has been generated, it often looks better to its author than it does to the voice owner.

## Failure 1: falling back to the generic average

The symptom is competent, pleasant, and completely empty text, with openings such as "in today's world" and closings such as "I hope this helps." It happens when the analysis is shallow and the model falls back to its defaults because the instructions lack specificity.

Increase the specificity of the rules and the quality of the calibrated examples. Generic rules always produce generic text.

## Failure 2: copying the topic instead of the voice

The skill writes well only about subjects found in the samples and falls apart when the topic changes. This happens when topic vocabulary is mistaken for voice vocabulary.

Always test with a subject absent from the samples. If the voice does not survive a topic change, it was not captured.

## Failure 3: turning traits into parody

The text stacks every verbal crutch into every paragraph until the voice becomes a caricature. This happens when a trait is recorded without its frequency.

Quantify recurring traits. If someone uses "at the end of the day" once every three texts, the skill must state that frequency instead of merely listing the expression.

## Failure 4: cleaning up speech

A spoken-voice skill produces flawless but lifeless text. This happens when hesitations, repetitions, and unfinished sentences are treated as mistakes instead of evidence.

Keep speech and writing as separate modes in the final document and state explicitly when each mode applies.

## Failure 5: confusing voice with formatting

The skill discusses only bullets, headings, and bold text without explaining how the person thinks or builds an argument. Formatting is part of voice, but it is its most superficial layer.

Ensure the final document covers argument structure, handling disagreement, and naming tension—not only text markup.

## Failure 6: inventing missing evidence

The skill confidently asserts traits unsupported by any sample. Models tend to fill gaps instead of admitting uncertainty.

Apply the protocol's strict rule: include nothing unless it is supported by a cited sample or confirmed through calibration.

## Failure 7: validating with the wrong person

Everyone approves the skill except the person it is meant to represent. This happens when third parties unfamiliar with the voice perform the acceptance test.

Run a blind test with the voice owner, comparing generated and real text without identifying either.

## Common AI writing signals that rarely belong to a real voice

Use this list as a final filter unless the samples prove the person genuinely writes this way.

- Empty agreement such as "great question" or "excellent point" used to please rather than inform.
- Decorative tricolons: listing three adjectives where one would be enough, such as "clear, concise, and effective."
- Automatic contrast structures such as "it is not just X; it is Y," which sound like slogans and occur unnaturally often in model output.
- Closings such as "I hope this helps" or "please let me know if you have questions" when the samples do not support them.
- Stacked hedging such as "it may perhaps be possible to consider," which weakens a claim until it says nothing.
- Emojis used as structural punctuation when no sample uses emojis.

---
name: typography-design-review
description: Design, refine and evaluate typefaces using editable font sources and real rendered proofs. Use for glyph construction, optical corrections, spacing, kerning, italics, font families, variable fonts, OpenType exports, or typographic hierarchy and readability. Inspect actual images, identify the font in use, and distinguish technical validity, visual judgment and measured reading performance. Works with the user's own brief, fonts and tools, without a required brand, family or design style.
---

# Type design and visual review

Work from a brief to a coherent system of forms, then draw, render, inspect,
correct and document. Use the user's language for explanations and reports.
Do not approve a drawing because its files compile or its curves are smooth.

For requests in Spanish, read [the Spanish instructions](SKILL.es.md) and use
the Spanish references and templates linked there. Keep the same technical
identifiers and evidence requirements in either language.

## Select the resources

- New design or inconsistent tone: [brief-to-form.md](references/brief-to-form.md).
- Drawing a new control set: [construction-workbench.md](references/construction-workbench.md).
- Shapes, spacing, kerning or confusion: [optical-review.md](references/optical-review.md).
- Weights, italics, variable fonts or exports: [families-and-exports.md](references/families-and-exports.md).
- Sizes, headings, leading, measure or responsive composition: [reading-and-hierarchy.md](references/reading-and-hierarchy.md).
- Specifications or release decisions: [standards-and-acceptance.md](references/standards-and-acceptance.md).
- Construction exercises and feedback: [practice-and-calibration.md](references/practice-and-calibration.md).
- Teaching influences and attribution: [formation-and-design.md](references/formation-and-design.md) and [sources.md](references/sources.md).
- Deterministic helpers: [tooling.md](references/tooling.md).

## 1. Establish the intended use

Recover the role, audience, tone, languages/scripts, sizes, platforms, formats
and ownership of the sources. Infer what the user already supplied; ask only
for consequential missing information while continuing independent work.

Record a brief with [brief-template.md](assets/brief-template.md). Define
observable constraints: proportions, contrast, curves, terminals, apertures,
weight, rhythm and recognition. A label such as "sans" or "serif" does not
determine a voice. Select licensed references for comparison, not for tracing.

For a new Latin design, begin with H/O/n/o and then critical e/s/r/a structures
in words. Choose appropriate controls for another script. Do not extrapolate
a complete alphabet from an unreviewed control set. For existing fonts, inspect
the user's actual words before inventing a replacement design.

## 2. Identify and preserve the artifacts

Identify editable sources, exported binaries, version and SHA-256. Preserve
the prior iteration. Avoid bootstrap scripts that replace existing drawings.
Build a new candidate into a new directory; record the compiler and options.

Use the project's supported editor/compiler. UFO/designspace, Glyphs or SFD
sources are inputs to editing, not interchangeable finished binaries. Do not
rename a font's metadata and describe that as a new original drawing.

`scripts/inspect_font.py` reports metadata and corpus coverage without changing
the font. It does not evaluate curves, shaping or aesthetics. Missing glyphs,
silent fallback, synthetic styles and horizontal transforms invalidate evidence
about a drawing. Mark uncovered material as not evaluated.

## 3. Produce proofs and actually inspect them

Use the real binary in an available rendering engine. Wait for font loading
and verify the face used by the renderer. Keep size, weight, axis position,
baseline, text, viewport, spacing and polarity comparable between iterations.

Prepare whole words and phrases at intended sizes, then enlarged silhouettes
and outlines with nodes/handles to locate causes. Add paragraph, punctuation,
numbers and language-specific marks. Test minimum, typical and stress sizes,
both polarities, and the actual repertoire rather than a fixed pangram alone.

The optional `scripts/build_proof.py` creates a self-contained HTML proof from
a supplied font and corpus. Use `--language es` for Spanish labels and messages;
`--language en` selects English. It withholds drawing samples that lack characters.
`scripts/capture_proof.mjs` can capture them with Playwright and report renderer
font use. Adapt the corpus, sizes and toolchain to the project.

**Open and inspect the images.** Producing screenshots is not visual review.
Make sure complete words, contours and heading context are visible. Reframe
cropped proofs and view readable sections of long pages. If image inspection
is unavailable, declare the visual review pending; do not invent observations.

## 4. Judge the system before repairing a detail

Describe the constants and deliberate variations across the letters. Evaluate
each criterion as `LOCALLY_ACCEPTABLE`, `DEFECT`, or `NOT_EVALUATED`, tied to
image, string, face, size and reason:

| Criterion | Observe |
| --- | --- |
| Form, curves and terminals | Accidental kinks, bulges, flats, pinches and inconsistent cuts |
| Optical weight and counters | Dark joins, blocked apertures and unintended changes in color |
| Spacing and rhythm | False pauses, collisions, word space and punctuation attachment |
| Recognition at use size | Covered confusions such as I/l/1, O/0 and rn/m in words |
| Voice and function | Whether local details support the brief and the whole word |

For a serious mismatch to the brief, recommend `REDRAW_REQUIRED`. Technical
checks do not compensate for it. If the necessary letters/context are absent,
use `FUNCTIONAL_CHECK_INCOMPLETE` and produce that evidence first.

Resolve base sidebearings and word space before accumulating kerning pairs.
Check punctuation in abbreviations and endings, not just letter pairs. Keep
tracking changes separate from kerning. A tighter font is not inherently
more readable. A round contour is not inherently playful.

## 5. Make a bounded correction and check the result

State the hypothesis and expected visible effect before changing a source.
Separate changes in drawing from changes in metrics when practical. Preserve
the original and compare variants under the same conditions, with neutral
labels before revealing the construction choice when useful.

Edit structure, strokes, counters and terminals together; use useful nodes,
not a geometric recipe. Revisit words after adjusting an isolated letter.
Check neighboring letters, accents, punctuation and extreme weights for
regressions. Change the hypothesis when the evidence contradicts it.

For families, inspect every distributed weight/style and axis extremes plus
intermediate positions. Extrapolated instances are candidates, not finished
weights. An italic requires a deliberate structure, not an unreviewed slant.
Validate real feature substitutions and mark positioning with shaping tools.

## 6. Review composition as its own requirement

Select roles before sizes: title, subtitle, lead, body, interface and guide.
Use [reading-tokens.json](assets/reading-tokens.json) as an adjustable starting
profile, not a norm. Compensate for apparent size, x-height, cap height, weight,
language and screen. The body, subtitle and guide must remain coherent.

For the supplied Latin editorial profile, start around body 18–20 px,
line-height 1.5–1.65 and about 65 graphemes per full desktop line. These are
design choices requiring rendered review. Mobile uses the available width
without forcing desktop line length. Print uses points and a separate scale.

Measure computed size, actual ink height and line box separately. Count
graphemes in wrapped lines; `65ch` is not 65 characters. Examine title/lead
line breaks and proportions, including the first line above a headline.
Do not approve a golden-ratio scale by arithmetic or assume current Medium
styles without inspecting them.

Check contrast, text enlargement, reflow and user spacing overrides on real
content. Apply the relevant WCAG criteria as documented in the standards
reference. Neither CSS metrics nor visual preference demonstrates faster
reading or better comprehension; such claims require appropriate reader tests.

## 7. Close the specified review and preserve what was learned

Separate technical requirements, project decisions and visual judgment.
Record exact files/hashes, corpus, versions, engines/platforms, opened images,
defects corrected, remaining limitations and warnings. Use
[review-template.md](assets/review-template.md) for the decision.

State the local result: redraw, gather evidence, or acceptable within the
declared scope. Follow the user's acceptance criteria; do not invent required
external signatures, certifications or an additional publication gate.
Respect existing rejection of the exact candidate. A relative A/B preference
does not automatically approve a whole family.

Stop an iteration when its checks pass and inspection identifies no further
concrete defect in scope. Do not keep changing outlines without a hypothesis.
New evidence can reopen the review. Never certify "perfect", "unimprovable",
"best in the world" or all-platform compatibility from a finite proof set.

Preserve the initial judgment when feedback corrects it. Treat repeated cases
as practice, not an independent test of skill effectiveness or model training.
No included script produces a typographic quality score.

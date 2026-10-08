# Optional local proofing tools

Use the project's own tools when they already provide better source editing,
shaping or proofing. These helpers inspect supplied binaries; they do not draw
outlines, build a family, run a standards certification or assign quality scores.

## Environment

Python 3.10+ with `fonttools[woff]` supports metadata and compressed inputs.
Install into a project virtual environment, with TLS/signature checks retained:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'fonttools[woff]'
```

For capture, use Node 20+ and Playwright with a supported Chromium installation.
Use a project-local dependency, keep its lockfile and record the resolved versions.
The helpers do not install these dependencies or download fonts themselves.
Only package building/validation uses the Python standard library alone.

## Metadata and coverage

```sh
python scripts/inspect_font.py /path/to/font.ttf --output /path/to/new-metadata.json
```

Run from this skill directory using the prepared Python. It reports a SHA-256,
names, metrics, weight/style, axes, feature tags and missing corpus characters
in actual/NFC/NFD strings. A cmap entry is not evidence of a correct drawing,
substitution or positioned mark. Feature tags do not demonstrate feature behavior.
Embedding flags do not replace the supplied font's license.

`--corpus /path/to/corpus.json` selects user text. Use the schema in
`assets/corpus.json`: unique lowercase `id`, string `label`/`text` and kind
`words`, `diagnostic` or `paragraph`. Paragraph samples can include complete
`heading` and `lead` text, whose coverage is checked too. Adapt languages and
symbols deliberately.

## A self-contained proof

```sh
python scripts/build_proof.py /path/to/font.ttf --output /path/to/new-proof.html
```

It embeds one real face, disables synthetic styles, uses its default variable
axis positions and reports its hash. Missing actual characters withhold the
entire sample so fallback cannot masquerade as the supplied drawing. Samples
include stress/use sizes and both polarities; paragraph composition starts at
20 px / 1.65. The page measures actual wrapped graphemes and adjusts paragraph
width toward 65 per full desktop line, rather than assuming `65ch` is 65
characters. `--measure 60` chooses a different target. Word wrapping introduces
variation; narrow screens keep their available width. Review the measured
result and the images. DOM range boxes are not glyph ink bounds.
For matched paragraph comparisons, retain the same actual width in the project
proof rather than independently calibrating each candidate's measure.

This single-face proof does not compare family members or expose all features,
axis positions or node handles. Build matched proofs and source-editor views
for those tasks. Text at 12 px is a diagnostic, not a reading recommendation.
The 96 px enlargement appears only in the wide proof. On narrow screens,
diagnostic words wrap at spaces, with horizontal scrolling for oversized tokens.
`overflowSamples` flags those tokens: use a wider view before evaluating them.

## Capture and verify renderer font use

```sh
node scripts/capture_proof.mjs /path/to/new-proof.html /path/to/new-captures
```

The capture script loads self-contained HTML locally, blocks external requests,
waits for the supplied face, captures widths 1440/390/320 and obtains Chromium
font-use evidence for each drawing sample. It fails on fallback or missing
font-use evidence for visible samples. `hiddenSamples` records enlargements
not rendered on narrow screens; these are not approved at that viewport.
Labels intentionally use a system font and are outside that audit. Unsupported
samples remain visibly withheld.

If Playwright is installed elsewhere, set `TYPE_REVIEW_PLAYWRIGHT` to its module
entry file; `TYPE_REVIEW_BROWSER` selects an existing Chromium executable. These
are local paths, not credentials. Explicit `--browser-arg=VALUE` passes a needed
browser option. Keep sandboxing enabled where supported; a managed root Linux
container may require `--browser-arg=--no-sandbox` for that environment only.

The output is new screenshots plus `capture-report.json`, not visual approval.
Open complete words and readable crops. Record actual OS/device separately;
this Chromium helper does not test Office, Windows or native iOS.

## Preservation and publication

Supplied fonts are never edited. Outputs refuse existing target files/directories.
Proof HTML embeds the supplied font: treat that file under its font license and
the user's confidentiality requirements. Capture is not an upload. Do not add
private fonts or generated embedded proofs to a public contribution without
appropriate authorization and licensing.

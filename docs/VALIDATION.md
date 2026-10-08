# Release verification record

2026-10-08, version 0.4.0. This record concerns the package and its helpers;
it is not a font-family approval, an independent agent benchmark or an OpenAI
directory acceptance.

## Licensed external fixture

**Asap Regular 3.002**, supplied by the Asap Project Authors / Omnibus-Type,
SIL Open Font License 1.1. Downloaded outside the distribution from Google
Fonts commit `5e8a3ba899557829a76cfdac30fa512bda91d7ca`:

`ofl/asap/Asap[wdth,wght].ttf`

Font SHA-256:
`7bf29bcab72f7d00de600e964a3fc206620050d8448ddd976822378d0fe18028`.
Used only as an existing licensed fixture, not as a typeface designed by this
skill. No font software or third-party PDF is included. The README proof image
is rendered document output. [Upstream](https://github.com/Omnibus-Type/Asap)
and [font license](https://github.com/google/fonts/blob/5e8a3ba899557829a76cfdac30fa512bda91d7ca/ofl/asap/OFL.txt).

## Checks actually executed

- Package paths, manifest lengths, translated listing copy, icons, skill
  metadata, local references, MIT notices, distribution exclusions and Python
  syntax checked with the project validator.
- Archives were built twice with matching digests in this Linux environment.
  Package paths use portable forward slashes and fixed ZIP metadata; source
  line endings are declared explicitly. Native Windows packaging was not run.
- FontTools 4.59.1 read the supplied variable font; source hash remained unchanged.
  Default axes: weight 400, width 100. Actual default corpus coverage passed.
- Chromium 151.0.7922.173 / Playwright 1.58.2 on Linux captured 1440, 390 and
  320 CSS px widths. The audit identified custom-font use in 72 visible
  desktop samples and 60 at each mobile width, with no fallback. The 96 px
  enlargements were intentionally not rendered on mobile and were recorded
  as hidden, not approved there.
- The paragraph measure adjusted from initial `65ch` toward a 65-grapheme
  target. Final full desktop lines ranged from 59 to 68 graphemes; final
  partial lines were counted separately. Mobile retained available width.
- Unsupported actual text and an unsupported heading withheld the affected
  proof. Existing metadata/HTML outputs were refused. Literal HTML in corpus
  text was escaped. An invalid font produced a clear error.
- A deliberate CSS substitution with a system font was rejected by capture
  with exit code 1 and font-use evidence. This is an expected negative check.
- The publisher dry run executed. The local integration check exercised a
  real initial Git commit, local bare-remote push, annotated tag and matching
  SHA; **GitHub API and release transport were simulated**. Existing outputs,
  uncommitted changes, destination history and a different origin were protected.

## Visual inspection performed

Opened the actual control and reading screenshots at desktop and mobile
widths, including both polarities. Reading titles, leads and body were visible
with their context. During helper refinement, incomplete heading fragments
were replaced with complete corpus headings, and oversized diagnostics ceased
breaking inside words. A 48 px spacing sample at width 320 was flagged as
horizontally overflowing; use its wider proof before judging that word.

The included README example is `proof-example.png`, 1212 × 818, SHA-256:
`87a3f70f4ff310cc13ee8b95631bb7639b30264dd2f45f084c0733ad96508644`.
These observations verify usable evidence generation; they do not demonstrate
the agent's independent ability to design a superior font or faster reading.

## Still separate from these results

`evals/cases.json` contains ten proposed behavioral cases, not an executed
held-out benchmark. Native Office/Windows/iOS and family-wide axis/feature
behavior were not tested by this single-face helper verification.

Public repository creation was attempted from the cloud connection and rejected:
`403 — Resource not accessible by integration`. A read confirmed the intended
repository was not available. The authorized Mac subsequently recovered the 18 final bridge blocks, verified
the bundle SHA-256, published v0.4.0 and verified the remote commit/tag and all
three downloaded ZIPs. OpenAI directory submission remains separate.

## Version 0.4.1 localization checks

2026-10-08. Full Spanish instructions, ten references, templates, interface
metadata and localized proof labels/defaults were added while keeping English.
The validator, skill metadata check, package localization check and local
publisher simulation passed. Six archives provide English/Spanish skill,
plugin and marketplace install editions; maintainer tooling remains in the
canonical source checkout. Identity, helper bytes and reading metrics match
between language editions.

Asap Regular with the same SHA-256 above was used outside the distribution.
Python 3.13 / FontTools 4.58.0 rendered both proof languages. Actual font
embedding, accents, per-paragraph language tags, Spanish withholding for
unsupported glyphs, HTML escaping, invalid-language refusal, output preservation
and unchanged font hashes passed. Chrome 154.0.8037.98 / Playwright on macOS
verified custom-font use in 72 desktop samples and 60 at each mobile width
(1440/390/320 CSS px), without fallback or missing evidence.

Opened the Spanish interface header, full Spanish reading proof in both
polarities, desktop controls and mobile reading captures. Titles, leads and
body remained visible. English and Spanish paragraph measurements at 1440 px
were identical. These are localization/tool checks, not a new font approval
or native Office/iOS certification.

Extracted all three Spanish install packages and ran their actual proof helper
without a language flag: all selected Spanish by default. The extracted
Spanish skill also passed the skill-creator metadata validator.

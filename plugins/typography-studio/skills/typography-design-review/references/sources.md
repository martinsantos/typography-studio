# Sources and consultation limits

Original summaries and linked references, not redistributed books, PDFs or
claims of author endorsement. A specification, a design recommendation and
a reader study provide different kinds of evidence. Consultation record:
2026-10-08. Links and requirements can change; check current primary material
when applying them to a release.

## Construction, spacing and educational influences

- *Design With FontForge*, community documentation:
  [Trusting Your Eyes](https://designwithfontforge.com/en-US/Trusting_Your_Eyes.html),
  [Creating o and n](https://designwithfontforge.com/en-US/Creating_o_and_n.html),
  [Spacing, Metrics and Kerning](https://designwithfontforge.com/en-US/Spacing_Metrics_and_Kerning.html),
  [Word Space](https://designwithfontforge.com/en-US/Word_Space.html).
  Read for optical/contextual judgment, controls and spacing before kerning.
- OERT, [Percepción visual y ritmo](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/percepcion-visual-y-ritmo.md),
  Marcela Romero, collaboration Inés Puparelli: recognition, intervals and rhythm.
- OERT, [La letra y su conjunto](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/la-letra-y-su-conjunto.md),
  Marcela Romero: sign/word, shared white, line spacing and typographic color.
- OERT, [Conceptos fundamentales](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/conceptos-fundamentales.md),
  Pablo Cosgaya, collaboration Marcela Romero, revision Natalia Pano: family,
  variables, spacing and color. These sections and the preceding articles
  informed the original summaries.
- Pablo Cosgaya, *Programa Tipografía 1*, 2016, historical FADU/UBA teaching
  program supplied for study. Consulted for structure, stroke, counters,
  family constants and reasoned critique. It is not evidence of today's
  curriculum. The PDF is not included in this package.
- Eduardo Gabriel Pepe, *Diseño tipográfico e identidad*, **Bold 2**, 2015,
  pp. 56–66. Supplied article consulted for form/function/identity and process;
  not included here. **Rubén Fontana (2007) is a secondary citation in Pepe,
  p. 65**, not a directly read Fontana article or endorsement of this method.
- Glyphs, [Multiple Masters, Part 1: Setting Up Masters](https://glyphsapp.com/learn/multiple-masters-part-1-setting-up-masters),
  Rainer Erich Scheichelbauer: master setup and interpolation context.

## Google Fonts

- [Google Fonts Guide](https://googlefonts.github.io/gf-guide/): current guide
  landing page consulted, showing source structure, overall/static/variable
  requirements, outline quality, QA and local testing as separate topics.
  Consult the relevant full chapter before claiming a submission complies.
- [gf-docs README](https://github.com/googlefonts/gf-docs/blob/main/README.md)
  explicitly marks that repository deprecated and points to the guide above.
  Historical [Reviewing Families](https://github.com/googlefonts/gf-docs/tree/main/ReviewingFamilies)
  and [Quick Start](https://github.com/googlefonts/gf-docs/tree/main/QuickStartGlyphs)
  informed the separation of sources, reproducible builds, checks and renders;
  they are not current submission policy.
- [Google Fonts Knowledge](https://fonts.google.com/knowledge) returned a
  JavaScript shell in this consultation environment. No unseen article is
  represented as read, and no current Medium CSS was measured.

## Composition, accessibility and reading outcomes

- USWDS [Typography](https://designsystem.digital.gov/components/typography/),
  [font size](https://designsystem.digital.gov/design-tokens/typesetting/font-size/)
  and [line height](https://designsystem.digital.gov/design-tokens/typesetting/line-height/):
  role, effective size, measure and leading. Recommendations include a 66
  character target and leading profiles around 1.5/1.62. This package's 65
  graphemes and 1.65 profile are adjustable choices, not quoted standards.
- Matthew Butterick, *Practical Typography*:
  [Point size](https://practicaltypography.com/point-size.html),
  [Line length](https://practicaltypography.com/line-length.html),
  [Line spacing](https://practicaltypography.com/line-spacing.html),
  [Headings](https://practicaltypography.com/headings.html),
  [Letterspacing](https://practicaltypography.com/letterspacing.html),
  [Kerning](https://practicaltypography.com/kerning.html).
  Web size 15–25 px, line length 45–90 characters and leading 120–145%
  illustrate recommendations that differ from a spacious 1.65 profile.
  Do not claim unanimous support for one proportion.
- W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and Understanding:
  [contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
  [resize text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
  [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html),
  [text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html),
  [visual presentation](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html).
  Apply the criterion's level, exceptions and mechanism. Text-spacing
  tolerances are not mandatory default CSS settings. A font alone cannot
  certify a site's WCAG conformance.
- Wallace and collaborators (2022), *Towards Individuated Reading Experiences:
  Different Fonts Increase Reading Speed for Different Individuals*,
  [Adobe Research abstract](https://research.adobe.com/publication/towards-individuated-reading-experiences-different-fonts-increase-reading-speed-for-different-individuals/).
  Only the publication page/abstract was read. It cautions against a universal
  optimal font; it does not establish a numeric improvement for this package.
- Golden-ratio typography is a composition model, not proof of perfect reading.
  The package does not use a ratio as an acceptance test.

## Formats and native integration

- Microsoft [OpenType specification](https://learn.microsoft.com/en-us/typography/opentype/spec/),
  particularly [name](https://learn.microsoft.com/en-us/typography/opentype/spec/name),
  [OS/2](https://learn.microsoft.com/en-us/typography/opentype/spec/os2),
  [cmap](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap) and
  [fvar](https://learn.microsoft.com/en-us/typography/opentype/spec/fvar).
  Syntax, naming, embedding flags and axis records do not define aesthetic quality.
- W3C [WOFF2](https://www.w3.org/TR/WOFF2/) and
  [CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/): distribution and rendering
  behavior, actual font use, styles and synthesis.
- Unicode [normalization](https://www.unicode.org/reports/tr15/): NFC/NFD
  coverage requires shaping checks as well as character-map inspection.
- Microsoft [OOXML `w:kern`](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.kern):
  kerning thresholds and inherited styles need actual application testing.
  A Linux browser or LibreOffice run does not validate native Office or iOS.

## Skill and plugin packaging

- OpenAI [Build skills](https://learn.chatgpt.com/docs/build-skills),
  [Package your plugin](https://developers.openai.com/plugins/build/plugins),
  [Submit and publish](https://developers.openai.com/plugins/deploy/submission)
  and [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines),
  consulted 2026-10-08 for progressive resources, manifest, icons and the
  distinction between repo distribution and public-directory review.
- OpenAI [skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator):
  a focused SKILL.md, optional deterministic helpers and references loaded
  when relevant. It is a packaging reference, not an endorsement.

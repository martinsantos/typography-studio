# Community index submission

Status: [PR #559 submitted](https://github.com/heilcheng/awesome-agent-skills/pull/559);
curator review pending. Destination:
[Agent Skill Index](https://github.com/heilcheng/awesome-agent-skills).
The proposal adds a source link to the community section in its English and
Spanish READMEs. It does not copy the skill into the index or claim acceptance.

## Pull request title

Add Typography Studio to the community skill index

## Pull request body

Typography Studio provides a focused workflow for designing and reviewing
typefaces through editable sources and actual rendered proofs. This change
adds its source repository to the English and Spanish community lists.

- [Skill entrypoint](https://github.com/martinsantos/typography-studio/blob/v0.4.1/plugins/typography-studio/skills/typography-design-review/SKILL.md):
  canonical name `typography-design-review`, under 500 lines, with English
  and Spanish instructions, references and templates.
- [Release](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.1):
  MIT licensed skill and Codex plugin packages. No fonts or client files
  are redistributed.
- [Validation evidence](https://github.com/martinsantos/typography-studio/blob/v0.4.1/docs/VALIDATION.md):
  package checks and local proof-helper tests with an existing Asap font,
  desktop/mobile screenshots, coverage checks and output-preservation checks.
  These checks do not establish agent-quality scores or reader outcomes.

Example requests and intended outputs:

1. "Review my font's spacing and punctuation using actual rendered words."
   The workflow requests the source/font and target use, renders proofs,
   inspects the images, and records prioritized observations with evidence.
2. "Prepare a Spanish reading proof at desktop and mobile widths."
   The optional helpers produce local HTML, font/corpus metadata and
   screenshots, preserving language tags and documenting coverage gaps.

The agent needs image inspection for visual conclusions and appropriate font
editing tools for source changes. Reader outcomes and untested native
platforms require separate verification.

Validation of this metadata-only proposal: `git diff --check` and
`npm run build` in `website/` passed.

## Submitted entries

English:

```markdown
- [martinsantos/typography-studio](https://github.com/martinsantos/typography-studio) - Design and review typefaces with real rendered proofs; English/Spanish
```

Español:

```markdown
- [martinsantos/typography-studio](https://github.com/martinsantos/typography-studio) - Diseño y revisión tipográfica con pruebas renderizadas reales; español e inglés
```

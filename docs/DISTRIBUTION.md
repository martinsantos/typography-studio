# Directory distribution

## Current status

- Public source and release: [Typography Studio 0.4.2](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.2).
- Skills CLI 1.7.1: repository discovery verified on 2026-10-08; one skill,
  `typography-design-review`, was found. The check used `--list` and disabled
  telemetry; it was not a community installation or a directory listing.
- OpenAI: corrected plugin ZIP 0.4.2 uploaded as a draft on 2026-10-08.
  Skill safety/security checks passed. The portal could not complete all
  automated metadata checks and explicitly allows submission for review.
  Directory review and publication have not occurred.
- Agent Skill Index: [PR #559](https://github.com/heilcheng/awesome-agent-skills/pull/559)
  submitted with English/Spanish entries; curator review pending.

[Español](DISTRIBUTION.es.md).

## OpenAI Plugins Directory

Open [Plugins](https://platform.openai.com/plugins), select the owning organization
and project, and complete its verified publishing identity. Upload
`typography-studio-0.4.2-plugin.zip`, which includes the Spanish resources and
listing translations. Resolve metadata and skill scans, submit for review,
then publish the approved version.

Version 0.4.2 prepares the Creativity category and public project, support,
privacy and MIT license URLs in response to the portal's metadata observations.

The package is skills-only. Use the official
[submission instructions](https://developers.openai.com/plugins/deploy/submission)
and inspect the actual declarations before submitting. A GitHub release and
a CLI discovery check are separate from OpenAI directory approval.

## skills.sh

Share the install command:

```sh
npx skills add martinsantos/typography-studio --skill typography-design-review
```

According to the [official FAQ](https://www.skills.sh/docs/faq), skills enter
the leaderboard through real user installs recorded by anonymous CLI telemetry.
Discovery with `--list` is useful verification, not proof of indexing.
Provide a real proof example and invite feedback from initial users.

## Community directory submission

[Agent Skill Index](https://github.com/heilcheng/awesome-agent-skills/blob/main/CONTRIBUTING.md)
accepts metadata additions by pull request. [PR #559](https://github.com/heilcheng/awesome-agent-skills/pull/559)
adds English/Spanish README entries linking to this source. Acceptance remains
pending. The [submission material](COMMUNITY_PROPOSAL.md) includes the exact
entries, description and two example requests.

- Name: Typography Studio
- Canonical skill: `typography-design-review`
- Platform verified here: Codex
- Description: Design and review typefaces with real rendered proofs.
- Source: [repository](https://github.com/martinsantos/typography-studio)
- Implementation: [skill entrypoint](https://github.com/martinsantos/typography-studio/blob/v0.4.1/plugins/typography-studio/skills/typography-design-review/SKILL.md)
- Languages: English and Spanish
- License: MIT

[VoltAgent](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md)
requires real community usage and excludes brand-new skills. Consider it after
the first adoption and feedback. Listing acceptance remains the curator's decision.

## Short launch copy

Typography Studio helps agents design and review typefaces through editable
sources and real rendered proofs: glyphs, spacing, kerning, families and reading
hierarchy. English/Spanish resources, optional local helpers and MIT license.

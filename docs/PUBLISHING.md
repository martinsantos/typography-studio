# Distribution and public discovery

These are separate channels. Complete the appropriate publication rather than
describing a local ZIP as a public listing. Requirements checked 2026-10-08.

## 1. Public source repository and repo marketplace

The intended source repository is `martinsantos/typography-studio`. Until a
verified publication receipt exists, that address is a destination, not proof
that the repository is accessible. Keep font binaries, confidential projects,
third-party PDFs and credentials outside it.

After it exists publicly, register the repository marketplace in a compatible
Codex client:

```sh
codex plugin marketplace add martinsantos/typography-studio --ref v0.4.0
codex plugin add typography-studio@typography-studio-marketplace
```

Use `--ref main` during development. Add GitHub topics `typography`, `font-design`,
`type-design`, `agent-skills`, `codex-plugin`, `kerning` and `variable-fonts`.
Publish the tagged ZIPs/checksums as release assets. The README's searchable
terms describe actual functionality; do not promise search rank or discoverability
before a public repository exists.

On an authorized Mac or other publisher machine, extract the **marketplace ZIP**
into a fresh standalone folder and inspect it. With Git, Python 3.10+ and an
already authenticated GitHub CLI:

```sh
python3 scripts/publish.py
python3 scripts/publish.py --execute
```

The first command describes the operation. The second creates the public
repository, pushes the reviewed source/tag and publishes the verified ZIPs.
It refuses an unrelated checkout, local uncommitted changes, a different origin,
an existing output directory or a destination with history. It never force-pushes.
If a remote action fails after partial publication, keep its outputs and
continue from that specific state; do not delete a repository to rerun it.
It writes a receipt only after verifying public visibility, remote SHA and
release URL. It does not submit the plugin to OpenAI's directory.

The standalone skill can also be installed manually from its ZIP. It contains
`.agents/skills/typography-design-review/` and a separate MIT license file.
Do not overwrite an existing user skill without reviewing their changes.

## 2. OpenAI's public Plugins Directory

OpenAI's current documentation supports skills-only submissions. This package
uses the supported Codex compatibility format. The submission ZIP contains
`.codex-plugin/plugin.json`, `skills/`, the referenced icons and license at its
root; it does not wrap the plugin inside the marketplace repository.

1. Sign in to the developer dashboard and select the publishing organization
   and project. The publisher needs owner access or Apps Management Write and
   a verified individual/business developer identity.
2. Open Plugins and upload a new plugin using `typography-studio-0.4.0-plugin.zip`.
   Select the actual verified publisher. The displayed publisher follows that
   identity; metadata alone cannot verify it.
3. Resolve the automated checks, confirm the category offered by the dashboard,
   and use `docs/SUBMISSION.md` for accurate listing copy and behavior.
4. Submit for review, completing the platform's declarations and policy terms.
   Skills-only submissions do not require the MCP-specific five positive/three
   negative server cases or a server demo recording. Our own evaluation cases
   remain separate quality exercises.
5. When approved, choose Publish plugin. Record the public listing URL, approved
   version and publication receipt. Uploading, submitting and approval are
   distinct states; none guarantees acceptance or ranking.

A GitHub release cannot perform developer identity verification or accept
dashboard terms. No API credentials, MCP server or account login are required
by this plugin itself. Do not invent a server just to publish a skill.

See [Package your plugin](https://developers.openai.com/plugins/build/plugins),
[Submit and publish](https://developers.openai.com/plugins/deploy/submission)
and [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines).

## 3. Release checks

Run the validator, build the three deterministic archives, verify their
checksums and inspect the exact manifest inside the submission archive.
Exercise the optional helpers on a licensed font outside the repository,
verify missing-glyph and overwrite behavior, and open actual screenshots.
Report proposed behavioral evaluation cases as proposed until executed.

If GitHub rejects a write, preserve the exact error and package/hash rather
than requesting a duplicate credential without evidence. A verified transfer
to an authorized publisher is useful; a VM-only filesystem link is not proof
that the publisher has received the archive.

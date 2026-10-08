# Contributing

Keep the method independent of brands and design fashions. Submit an issue or
pull request with the problem, hypothesis, licensed or user-owned evidence,
rendering conditions and the bounded change. Use generic examples in public
documentation and omit client files and confidential fonts.

Preserve the distinction between a format requirement, a project decision,
a visual judgment and a measured human outcome. Cite primary sources when
possible and label secondary citations or inaccessible material. Do not turn
a convenient size scale into a universal readability standard.

For scripts, exercise a real licensed font outside the distribution, a missing
character case and refusal to overwrite existing outputs. Open the screenshots
before reporting visual observations. For workflow changes, add a meaningful
case to `evals/cases.json`; record execution separately from proposed cases.

Run `python3 scripts/validate.py` and package into a fresh directory with
`python3 scripts/package.py --output /path/to/new-directory`. Never add fonts,
font binaries, licensed PDFs, credentials, environment dumps or browser caches.
Changes that improve compatibility must not weaken evidence requirements.

For publisher changes, run `python3 scripts/check_publisher.py`. It exercises
real local Git and preservation guards with simulated GitHub responses, without
creating a public repository or making external GitHub requests.

# Technical standards and scoped acceptance

Separate three kinds of evidence:

1. **Applicable requirements:** formats and accessibility specifications.
2. **Project profile:** repertoire, styles, sizes, platforms and release choices.
3. **Visual judgment:** actual rendered samples opened and reviewed.

Record section, specification version/status, URL and consultation date. OTS
and FontBakery are useful independent checks, not a typographic quality score.
No finite corpus establishes a perfect family or all-platform compatibility.

## Font formats and layout

- [OpenType](https://learn.microsoft.com/en-us/typography/opentype/spec/otff):
  required tables, directory, alignment/checksums and format-specific rules.
  Run OTS on distributed files and preserve the original rather than silently
  replacing it with sanitizer output.
- [name](https://learn.microsoft.com/en-us/typography/opentype/spec/name),
  [OS/2](https://learn.microsoft.com/en-us/typography/opentype/spec/os2),
  [cmap](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap),
  [fvar](https://learn.microsoft.com/en-us/typography/opentype/spec/fvar):
  naming/style links, metrics, coverage, axes and instances. Unicode cmap
  does not mean complete Unicode coverage.
- [WOFF2](https://www.w3.org/TR/WOFF2/): headers, decoding and fidelity to the
  source SFNT. Reconstructed SFNT checksums are not stored WOFF2 bytes.
- [glyf](https://learn.microsoft.com/en-us/typography/opentype/spec/glyf):
  contour structure and flags. OVERLAP_SIMPLE is optional; review relevant
  warnings/rendering rather than treating every recommendation as mandatory.
- [Unicode normalization](https://www.unicode.org/reports/tr15/#Design_Goals):
  canonical equivalence. Compare the actual NFC/NFD corpus with shaping and
  marks; normalization does not prescribe identical layout bytes for all text.

`fsType=4` means Preview & Print embedding; it does not grant editable embedding,
prove ownership or replace a distribution license. Test installed-font editing
separately. Do not clear permissions to make a document test pass.

For Word, check [WordprocessingML Kern](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.kern):
the threshold is in half-points and inherited through styles. If no hierarchy
level enables kerning, it is not applied. Test the actual app and linked styles.

## Web typography

Consult [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and its understanding pages:

| Criterion | Scope |
| --- | --- |
| 1.4.3 | Normal contrast 4.5:1, large text 3:1 under the defined exceptions |
| 1.4.4 | Text resize to 200% without loss of content/function |
| 1.4.10 | Reflow at 320 CSS px for vertical reading, with stated exceptions |
| 1.4.12 | Tolerate combined user text-spacing overrides without loss |
| 1.4.8 | Optional AAA presentation controls; not an initial-style recipe |

Do not describe 16 px, 65 characters or 1.65 leading as WCAG requirements.
[CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/) describes selection, kerning,
variation and synthesis; record its publication status when consulted.
Verify the face drawing the sample, not only computed CSS font-family.

## Close the review

Record source/binary hashes, corpus, sizes, style/axis positions, tool versions,
platforms, technical results and warnings, opened proof images, known defects
and untested conditions. Follow the user's agreed criteria without inventing
required signatories or a third-party certification.

Use `TECHNICALLY_ACCEPTABLE_IN_SCOPE` for passed requirements/profile and
`LOCALLY_ACCEPTABLE` for visual findings in the declared corpus. List concrete
remaining defects separately; new evidence reopens its affected part.

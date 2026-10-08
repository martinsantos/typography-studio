# Readability, hierarchy and optical size

## Roles precede ratios

Assign title, section heading, subtitle, lead, body, interface, guide and caption.
Judge their relationship on rendered content, including the small first line
above a title. A 58 px headline does not justify unreadable 11 px subtitles.
An eyebrow can be smaller than the title while retaining a clear editorial role.

`assets/reading-tokens.json` provides editable Latin-screen starting profiles.
Body 18–20 px, guide/interface around 16 px, 1.5–1.65 leading and roughly
65 graphemes per full desktop line are choices to try, not physiological laws,
WCAG mandates, universal minima or a perfect golden-ratio system.

USWDS and Practical Typography offer differing leading/measure recommendations.
Select a profile for the actual reader, language, font, density and support.
Do not attribute one chosen ratio to all the sources or claim to reproduce a
current publishing platform without inspecting it.

## Compensate apparent size

Record CSS em size, line box, cap/x-height and visible ink height separately.
Different faces can look substantially different at the same nominal size.
Use supported optical-size axes intentionally; test relevant axis positions
and whether the application applies optical sizing. Do not fabricate an opsz
axis by geometric scaling or promise identical appearance across rasterizers.

Check the role relationship, position and vertical gaps in the full composition.
Titles may need tighter built-in spacing or leading than paragraphs. Tracking
changes must have a specific purpose and cannot repair a drawing or loose base
metrics. Inspect title/lead line breaks and total block heights on mobile.

## Measure actual lines

Use the selected binary, style/axis, language and text. Count grapheme clusters,
including internal spaces, in actual wrapped lines. Separate final paragraph
lines from the full-line mean. Report the corpus and range, not just the mean.
`65ch` measures the width of a zero glyph, not 65 graphemes.

Start with an em-based measure, then calibrate by rendering. On a narrow viewport,
use the available width while preserving readable body size; do not force 65
characters by shrinking text. Inspect each column and long word, not just total
document scroll width. Do not count whitespace at a line ending as visible ink.

For scripts with different spacing or character conventions, define an
appropriate measure and reader/task comparison instead of importing Latin
character-count targets blindly.

## Test adaptations and contrast

Check desktop and mobile, text enlarged to 200%, relevant native zoom and
reflow at 320 CSS px. Changing the root font size tests one mechanism; it is
not equivalent to testing native browser zoom.

Apply line-height 1.5, paragraph spacing 2 em, letter spacing .12 em and word
spacing .16 em together where WCAG 1.4.12 applies. Ensure no content/function is
lost. These are user adjustments to tolerate, not mandatory initial styles.
Respect language/script exceptions in the criterion.

Check actual text/background colors, transparency and polarity: 4.5:1 for
normal text, 3:1 for large text under WCAG's definition. Full WCAG conformity
requires more than these typographic checks.

## Print and reader studies

Use a separate print hierarchy and points; start around body 10–12 pt only when
appropriate for the face and audience. Verify margins, leading, header/footer
clearance, tables, page breaks and actual font embedding. Open exported pages.
Use physical print evidence when that is the intended medium.

Readability preference, letter recognition, reading speed and comprehension are
different outcomes. A visual review or modular ratio cannot demonstrate faster
reading. Reader studies need defined tasks, representative participants, suitable
comparisons and reporting of variability. Fonts may benefit different readers.

# Families, italics, variation and distribution

## Grow a reviewed system

Preserve the approved starting face. Draw additional masters with deliberate
stem, horizontal, counter, join and spacing decisions. Corresponding contours,
directions, start points and node types must support interpolation without
changing the intended endpoints. Convert cubic masters to quadratic together
when building compatible TrueType variations.

Check extrema and intermediate axis positions, including positions between
named instances. Extrapolations are provisional. Thin weights can expose weak
joins and incorrect mass; heavy weights can close counters, merge strokes and
damage punctuation. Uniform numeric `wght` steps are not an optical guarantee.

## Italics and OpenType behavior

Define which forms change structure and which follow the roman. A slant angle
alone does not approve an italic. Revisit entry/exit strokes, width, shoulders,
joins, spacing and accents. Do not prescribe a universal angle or a/f design.

Verify proportional/tabular figures through actual substitutions and advances.
Tracking is not a substitute for distinct figure designs. Proof unencoded
alternates by activating their feature; a cmap atlas will miss them. Check
diacritics, mark anchors and language-specific layout using real shaping.

## Export faithfully

- Use the project's source format and supported compiler. Record versions,
  settings and source revision. Do not overwrite a reviewed candidate.
- Check exported outlines/advances against the sources and between formats
  with an appropriate conversion tolerance. This is fidelity, not legibility.
- Coordinate family/subfamily names, style linking, weight classes, metrics,
  STAT/fvar, named instances and PostScript names. Test coexistence and upgrades.
- Validate each distributed static and variable binary, warnings included.
  Keep FontBakery families grouped correctly; explain a warning instead of
  deleting valid contours merely to improve a score.
- Preserve embedding permissions. Package the license, version, files and
  checksums. Distribution of the tooling does not license a user's font.
- Once published, keep versioned asset URLs immutable; corrections get a new
  release. Document fallback fonts and their separate licenses and coverage.

## Platform evidence

Match the matrix to the intended uses: browsers, Windows text rasterization,
Word/Excel/PowerPoint if relevant, native Apple apps, PDF export and printing.
Record exact OS/app versions. Linux WebKit is not a physical iOS test;
LibreOffice is not Microsoft Office. A PDF proof is not physical print.

For Office, test installed static styles and real bold/italic selection, linked
styles, explicit kerning, line breaks, accents and export. A CSS fallback stack
does not automatically apply in Word. Installed font editing is distinct from
editable embedded-font permissions.

On iOS, distinguish Safari webfonts, PDF viewing and installed fonts used by
individual apps. Installation does not guarantee recognition by every app.

See [standards-and-acceptance.md](standards-and-acceptance.md) for the technical
specifications and a release decision with a stated scope.

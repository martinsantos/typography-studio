# Optical review: contours, color, space and recognition

## Shapes and curves

Start with silhouette and words; use nodes and handles to locate a cause.
Look for unintended bulges, flats, pinches and kinks. Distinguish a smooth
tangent from smooth curvature, and both from an appropriate optical shape.
Collinear cubic handles need not have the same length. Intentional corners
should be judged within the system rather than deleted by a smoothness test.

Use useful extrema and segments. Do not add one node for every raster pixel
or simplify to an arbitrary node quota. Inspect the counter as carefully as
the exterior. Compare rounds and straights for apparent height and weight;
overshoot is an optical correction, not a universal percentage.

## Color and proportional relationships

Inspect stems, horizontals, diagonals and round strokes at the same size.
Check joins, shoulders, waists, counters, openings and terminals for unwanted
dark spots or eye-catching exceptions. Compare cap/x-height and width according
to function, without scaling different families to an identical silhouette.

A changed pixel pattern may result from rasterization rather than a drawing
change. Inspect another size and engine before attributing the cause.

## Base spacing, kerning and punctuation

For Latin, use `nnnn`, `oooo`, `nonono`, `HHHH` and `HOHO`, then put the letters
under review between suitable controls. Adapt this method to the actual script.
Compare internal and shared white space optically; do not equate their areas.

Widespread gaps require reconsidering base metrics before adding many pairs.
Keep outlines fixed in a metrics comparison when possible. Revisit accented
components and anchors after moving a base drawing. Then recheck existing
kerning and word space; their context changed.

An isolated tight pair does not resolve loose rhythm throughout a paragraph.
Conversely, reducing all sidebearings can create collisions. Compare several
moderate alternatives, preserving the original and actual advance values.

Check abbreviations, punctuation and endings: `IT.`, `OT,`, `A.V.`, `To.`,
`word,`, `word.` and language-specific quotes/signs where covered. A point or
comma has different white space beside a top overhang than beside a round.
Inspect point and comma separately, along with word space after the sign.

## Recognition

Use I/l/1, O/0 and rn/m where relevant, first isolated and then within words
and data. At small sizes, a height distinction can disappear. Compare structural
alternatives while accounting for their sidebearings and effect on the voice.
Neither an I with bars nor a curved l is always right. Test the choice against
the brief and neighboring signs.

Cover actual accents, diacritics, currencies, numbers, punctuation and marks.
Check NFC/NFD with a shaping engine when needed. Coverage in cmap is not proof
of equivalent shaping or correct mark placement.

## Record what was seen

For every judgment, identify glyph/string, binary hash, size, weight/axis,
engine, polarity, image and reason. Separate observation, likely cause and
preference. Mark unrendered or fallback portions `NOT_EVALUATED`.

Geometry, OCR, image similarity, OTS and FontBakery cannot score visual quality.
An enlarged outline is evidence of construction; a paragraph is evidence of
composition; reader performance needs a suitable human study.

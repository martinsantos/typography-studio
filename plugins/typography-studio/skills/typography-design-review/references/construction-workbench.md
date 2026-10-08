# Construction workbench

Use this when the task is to make new glyphs, not only inspect an exported font.
Follow the user's editor and brief. The example is a proposed Latin control
exercise, not a finished family or a geometric recipe for every design.

## Establish an editable source

Create a new, named source project in the supported editor, with a new export
directory. Record units per em, baseline, x-height, cap height, ascenders,
descenders and the intended optical size. Keep guides distinct from visible
ink limits. Choose the name, weight and style metadata from the actual drawing.
Use the editor's documented UFO/designspace, Glyphs or SFD format; do not treat
TTF point editing as an equivalent source workflow.

A neutral control exercise might start at 1000 UPM with cap height 700 and
x-height 500. These are provisional construction coordinates, not standards or
proof of proportion. Select a plausible stem for the intended weight, render
at use size and change it when visual evidence warrants. Do not transfer these
values automatically to a different script, function or reference.

## Draw H, then O

For H, place two stems and a crossbar as editable contours. Evaluate their
optical thickness, junctions, counter division and crossbar position. A bar
can require different thickness from a vertical stem. Keep meaningful extrema
and contour direction; determine spacing with repeated H and mixed H/O words.

For O, work with inner and outer curves together. A mechanically concentric
outline or ellipse can produce the wrong stroke, counter or tone. Use extrema
and a small useful node set. At smooth joins, handles follow the intended
tangent; their lengths govern curvature and require eye-guided adjustment.
Compare round-form overshoot with H at baseline/cap height in actual words.
Do not force equal geometric bounds to satisfy a coordinate check.

Inspect `HHOO HOOH` at use and enlarged sizes, both polarities, plus source
views with handles. State where stroke/counter balance and intervals differ.
Preserve the first drawing before changing structure or metrics.

## Draw n and o as a related lowercase system

Use n to investigate stem, shoulder, inner join, aperture and horizontal rhythm.
Balance the shoulder against the stem at the intended size; inspect dark joins
and pinches rather than smoothing them numerically. Relate lowercase o's
contrast and round rhythm to O while respecting the lowercase proportion.

Space `nonn`, `nono` and provisional words that actually use the covered set.
If a full word needs missing glyphs, draw/review those glyphs or withhold it.
Never substitute another face silently and call the composite your design.

## Expand through critical structures

Add e/s/r/a appropriate to the brief, not by copying a stem into every letter.
Review e's aperture and crossbar, s's changing curvature and terminals, r's
shoulder/end and a's structure. Repeat letters can expose rhythm but cannot
replace whole words. Use `access`, `esencia`, `sostenida` or user text once its
complete repertoire is present. Inspect accents as structures attached to the
family, with both composed and decomposed input and actual shaping.

## Correct, build and compare

Choose one hypothesis: for example, a dark inner join closes at 16 px, or the
space after a curved terminal causes a false pause. Change a saved source,
export through the project's compiler and compare identical words/sizes.
Separate sidebearing corrections from outline corrections where practical.
Only add kerning after base spacing is coherent. Inspect overlap handling,
contour direction and export fidelity on the new candidate; do not run global
cleanup destructively or treat successful cleanup as optical approval.

Repeat on punctuation, figures, key recognition cases and every distributed
family member. Node compatibility alone does not make interpolated weights
look coherent. Use the optical and family references for the next review.

When no source editor or image inspection is available, deliver the brief,
construction plan and required evidence honestly; do not label imaginary
glyphs or an unseen candidate as complete.

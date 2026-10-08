#!/usr/bin/env python3
"""Create a self-contained, single-face proof without mutating a font."""
from __future__ import annotations
import argparse
import base64
import html
import json
import re
from pathlib import Path
from font_evidence import inspect, read_corpus, write_new, TTLibError


def render(font_path: Path, samples: list[dict], measure_target: int = 65) -> str:
    evidence = inspect(font_path, samples)
    suffix = font_path.suffix.lower()
    formats = {".ttf": ("font/ttf", "truetype"), ".otf": ("font/otf", "opentype"),
               ".woff": ("font/woff", "woff"), ".woff2": ("font/woff2", "woff2")}
    if suffix not in formats:
        raise ValueError("Proofs support single-face TTF, OTF, WOFF or WOFF2 inputs.")
    mime, fmt = formats[suffix]
    payload = base64.b64encode(font_path.read_bytes()).decode("ascii")
    wght = next((a for a in evidence["axes"] if a["tag"] == "wght"), None)
    weight = wght["default"] if wght else evidence["weight_class"]
    descriptor = f'{wght["minimum"]:g} {wght["maximum"]:g}' if wght else str(weight)
    style = "italic" if evidence["italic"] else "normal"
    if any(not re.fullmatch(r"[A-Za-z0-9 ]{4}", axis["tag"]) for axis in evidence["axes"]):
        raise ValueError("Unsupported axis tag in this proof helper.")
    variations = ",".join(f'"{axis["tag"]}" {axis["default"]:g}' for axis in evidence["axes"]) or "normal"
    chunks = []
    for sample, coverage in zip(samples, evidence["coverage"]):
        text = html.escape(sample["text"])
        label = html.escape(sample.get("label", sample["id"]))
        ident = sample["id"]
        if coverage["missing_actual"]:
            missing = ", ".join(x["codepoint"] for x in coverage["missing_actual"])
            chunks.append(f'<section class="unavailable"><h2>{label}</h2><p>WITHHELD: {missing} absent from cmap. This is not a drawing proof.</p><code>{text}</code></section>')
            continue
        if sample.get("kind") == "paragraph":
            heading = html.escape(sample.get("heading") or re.split(r"(?<=[.!?])\s", sample["text"], maxsplit=1)[0])
            lead = html.escape(sample.get("lead", ""))
            samples_html = (f'<div class="size-label">Single-face hierarchy: 40 / 24 / 20 px; no synthetic weights</div>'
                            f'<h3 class="proof-sample reading-title" data-sample="{ident}-title">{heading}</h3>'
                            + (f'<p class="proof-sample reading-lead" data-sample="{ident}-lead">{lead}</p>' if lead else '')
                            +
                            f'<p class="proof-sample reading" data-sample="{ident}">{text}</p>')
        else:
            samples_html = "".join(f'<div class="size-label {"enlarged" if size == 96 else ""}">{size} px</div><div class="proof-sample words {"enlarged" if size == 96 else ""}" data-sample="{ident}-{size}" style="font-size:{size}px">{text}</div>' for size in (12, 16, 24, 48, 96))
        chunks.append(f'<section class="word-panel"><h2>{label}</h2><div class="polarity normal">{samples_html}</div><div class="polarity reverse">{samples_html}</div></section>')
    metadata_json = json.dumps(evidence, ensure_ascii=False).replace("<", "\\u003c")
    title = html.escape(evidence["names"].get("4") or font_path.name)
    return f'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Typeface proof — {title}</title>
<style>
@font-face{{font-family:ProofFont;src:url(data:{mime};base64,{payload}) format('{fmt}');font-weight:{descriptor};font-style:{style};font-display:block}}
*{{box-sizing:border-box}}body{{margin:0;color:#17202a;background:#f0f2f4;font:16px/1.5 system-ui,sans-serif}}
main{{max-width:1260px;margin:auto;padding:24px}}header{{margin-bottom:24px}}h1{{font-size:28px;line-height:1.2;margin:0 0 12px}}h2{{font-size:17px;margin:0 0 12px}}code{{overflow-wrap:anywhere}}section{{margin:0 0 24px;padding:20px;background:white;border:1px solid #cbd1d6}}
.polarity{{padding:18px;margin:12px 0;overflow-wrap:anywhere}}.reverse{{background:#111;color:#fff}}.normal{{background:#fff;color:#111}}.size-label{{font:12px/1.5 system-ui,sans-serif;color:#65717b;margin-top:12px}}.reverse .size-label{{color:#b9c3cb}}
.proof-sample{{font-family:ProofFont;font-weight:{weight};font-style:{style};font-synthesis:none;font-optical-sizing:none;font-variation-settings:{variations};font-kerning:normal;font-variant-ligatures:normal;letter-spacing:normal}}.words{{line-height:1.35;margin:4px 0 16px;overflow-wrap:normal;overflow-x:auto}}.reading{{font-size:20px;line-height:1.65;max-width:65ch;margin:0}}.reading-title{{font-size:40px;line-height:1.2;margin:12px 0}}.reading-lead{{font-size:24px;line-height:1.4;margin:12px 0 20px;max-width:55ch}}.unavailable{{border-color:#934400}}
@media(max-width:500px){{main{{padding:12px}}section{{padding:12px}}.polarity{{padding:12px}}.enlarged{{display:none}}}}
</style>
<main><header><h1>Single-face type proof</h1><p>{title} · weight {weight} · {style} · variable axes at defaults</p><p><code>SHA-256 {evidence['sha256']}</code></p><p>Open and inspect the images. Twelve pixels is a stress sample, not a recommended reading size. The 96 px enlargement uses the wide proof and is hidden on narrow screens. Diagnostic words wrap at spaces; oversized tokens scroll horizontally and require a wider view. Reading: 20 px / 1.65; adjustable target {measure_target} graphemes per full desktop line. This proof does not approve the design.</p><p id="font-status">Loading supplied font…</p></header>{''.join(chunks)}</main>
<script id="font-evidence" type="application/json">{metadata_json}</script>
<script>
window.proofReady=(async()=>{{
 await document.fonts.load('{style} {weight} 20px ProofFont'); await document.fonts.ready;
 const faces=[...document.fonts].filter(f=>f.family==='ProofFont');
 const loaded=faces.length>0 && faces.every(f=>f.status==='loaded');
 const paragraphs=[...document.querySelectorAll('.proof-sample.reading')];
 const measure=el=>{{
  const node=el.firstChild; const lines=new Map();
  const segments=new Intl.Segmenter(undefined,{{granularity:'grapheme'}}).segment(node.textContent);
  for(const s of segments){{const range=document.createRange();range.setStart(node,s.index);range.setEnd(node,s.index+s.segment.length);const rect=range.getClientRects()[0];if(rect){{const y=Math.round(rect.top);lines.set(y,(lines.get(y)||0)+1);}}}}
  const cs=getComputedStyle(el); return {{sample:el.dataset.sample,polarity:el.closest('.polarity').className,size:cs.fontSize,lineHeight:cs.lineHeight,width:el.getBoundingClientRect().width,graphemesPerLine:[...lines.values()]}};
 }};
 const normal=paragraphs.filter(el=>el.closest('.normal'));
 let iterations=0;
 for(;iterations<8 && normal.length;iterations++){{
  const counts=normal.flatMap(el=>measure(el).graphemesPerLine.slice(0,-1)).sort((a,b)=>a-b);
  if(!counts.length)break;
  const median=counts[Math.floor(counts.length/2)];
  if(Math.abs(median-{measure_target})<=3)break;
  const width=normal[0].getBoundingClientRect().width;
  const available=Math.min(...paragraphs.map(el=>{{const parent=el.parentElement,cs=getComputedStyle(parent);return parent.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);}}));
  const next=Math.max(1,Math.min(available,width*{measure_target}/median));
  if(Math.abs(next-width)<1)break;
  for(const el of paragraphs)el.style.maxWidth=next+'px';
 }}
 const measurements=paragraphs.map(measure);
 const visible=[...document.querySelectorAll('.proof-sample')].filter(el=>el.getClientRects().length);
 const overflowSamples=visible.filter(el=>el.scrollWidth>el.clientWidth+1).map(el=>el.dataset.sample);
 window.proofRuntime={{fontLoaded:loaded,measureTarget:{measure_target},measureIterations:iterations,measurements,overflowSamples,limits:['Horizontally overflowing words need a wider view before judgment.','The line target is a design choice, not a readability standard.','DOM range boxes are not actual glyph ink bounds.','A successful load is not proof of shaping or visual quality.']}};
 document.querySelector('#font-status').textContent=loaded?'Supplied face loaded. Renderer font-use audit is still required.':'FONT LOAD FAILED';
 if(!loaded)throw new Error('Supplied font did not load'); return window.proofRuntime;
}})();
</script></html>'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("font", type=Path)
    parser.add_argument("--corpus", type=Path, default=Path(__file__).resolve().parents[1] / "assets/corpus.json")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--measure", type=int, default=65, help="Adjustable target graphemes per full desktop paragraph line (30–100).")
    args = parser.parse_args()
    if not 30 <= args.measure <= 100:
        parser.error("--measure must be between 30 and 100.")
    try:
        write_new(args.output, render(args.font, read_corpus(args.corpus), args.measure))
        print(f"Proof written to {args.output}. Render and inspect it before making visual claims.")
    except (OSError, ValueError, TTLibError, ImportError) as exc:
        parser.exit(1, f"Proof failed: {exc}\n")


if __name__ == "__main__":
    main()

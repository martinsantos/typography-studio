"""Shared read-only font metadata and corpus helpers. Requires FontTools."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

try:
    from fontTools.ttLib import TTFont, TTLibError
except ImportError as exc:
    raise SystemExit("FontTools is required. Install it in a project virtual environment.") from exc


def read_corpus(path: Path) -> list[dict]:
    value = json.loads(path.read_text(encoding="utf-8"))
    samples = value.get("samples") if isinstance(value, dict) else None
    if not isinstance(samples, list) or not samples:
        raise ValueError("Corpus must contain a nonempty samples array.")
    ids = set()
    for sample in samples:
        if not isinstance(sample, dict):
            raise ValueError("Each corpus sample must be an object.")
        ident = sample.get("id", "")
        if not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9-]+", ident) or ident in ids:
            raise ValueError("Sample IDs must be unique lowercase letters, digits and hyphens.")
        if not isinstance(sample.get("text"), str) or not sample["text"]:
            raise ValueError(f"Sample {ident} needs nonempty text.")
        if not isinstance(sample.get("label", ident), str):
            raise ValueError(f"Sample {ident} needs a string label.")
        if sample.get("kind", "words") not in {"words", "diagnostic", "paragraph"}:
            raise ValueError(f"Unsupported kind in sample {ident}.")
        if "language" in sample and (not isinstance(sample["language"], str)
                                     or not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*", sample["language"])):
            raise ValueError(f"Invalid language tag in sample {ident}.")
        for key in ("heading", "lead"):
            if key in sample and (not isinstance(sample[key], str) or not sample[key]):
                raise ValueError(f"Optional {key} in {ident} must be nonempty text.")
        ids.add(ident)
    return samples


def needed_codepoints(text: str) -> set[int]:
    # Shaping/layout controls are not required to have standalone cmap entries.
    return {ord(char) for char in text if unicodedata.category(char) not in {"Cc", "Cf"}}


def missing_characters(text: str, cmap: dict) -> list[dict]:
    return [{"codepoint": f"U+{cp:04X}", "character": chr(cp),
             "name": unicodedata.name(chr(cp), "UNNAMED")}
            for cp in sorted(needed_codepoints(text) - cmap.keys())]


def inspect(path: Path, samples: list[dict]) -> dict:
    with TTFont(path, lazy=False) as font:
        cmap = {cp: glyph for cp, glyph in (font.getBestCmap() or {}).items() if glyph != ".notdef"}
        names = font["name"] if "name" in font else None
        os2 = font["OS/2"] if "OS/2" in font else None
        head = font["head"] if "head" in font else None
        hhea = font["hhea"] if "hhea" in font else None
        axes = [{"tag": a.axisTag, "minimum": a.minValue, "default": a.defaultValue,
                 "maximum": a.maxValue, "hidden": bool(a.flags & 1)}
                for a in font["fvar"].axes] if "fvar" in font else []
        features = {}
        for tag in ("GSUB", "GPOS"):
            table = font[tag].table if tag in font else None
            feature_list = getattr(table, "FeatureList", None)
            features[tag] = sorted({x.FeatureTag for x in feature_list.FeatureRecord}) if feature_list else []
        coverage = []
        for sample in samples:
            text = " ".join(sample[key] for key in ("text", "heading", "lead") if key in sample)
            coverage.append({"id": sample["id"],
                             "missing_actual": missing_characters(text, cmap),
                             "missing_nfc": missing_characters(unicodedata.normalize("NFC", text), cmap),
                             "missing_nfd": missing_characters(unicodedata.normalize("NFD", text), cmap)})
        return {
            "schema_version": 1,
            "font": str(path.resolve()), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "names": {str(n): names.getDebugName(n) if names else None for n in (1, 2, 4, 5, 6, 16, 17)},
            "glyph_count": len(font.getGlyphOrder()), "mapped_unicode_codepoints": len(cmap),
            "weight_class": getattr(os2, "usWeightClass", 400),
            "italic": bool(getattr(os2, "fsSelection", 0) & 1 or getattr(head, "macStyle", 0) & 2),
            "embedding_fsType": getattr(os2, "fsType", None),
            "metrics": {"units_per_em": getattr(head, "unitsPerEm", None),
                        "x_height": getattr(os2, "sxHeight", None), "cap_height": getattr(os2, "sCapHeight", None),
                        "typo_ascender": getattr(os2, "sTypoAscender", None),
                        "typo_descender": getattr(os2, "sTypoDescender", None),
                        "typo_line_gap": getattr(os2, "sTypoLineGap", None),
                        "hhea_ascender": getattr(hhea, "ascent", None),
                        "hhea_descender": getattr(hhea, "descent", None)},
            "axes": axes, "features": features, "coverage": coverage,
            "limits": ["cmap coverage does not prove shaping, mark positioning or glyph quality.",
                       "A listed feature is not evidence that its behavior was tested.",
                       "Embedding flags do not replace the font's license."]
        }


def write_new(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(text)

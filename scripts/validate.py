#!/usr/bin/env python3
"""Validate distribution structure and documented metadata requirements."""
from __future__ import annotations
import json
import re
import sys
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/typography-studio"
SKILL = PLUGIN / "skills/typography-design-review"
IGNORED = {".git", ".venv", "dist", "node_modules", "__pycache__"}


def project_files(root: Path = ROOT) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file()
                  and not any(x in IGNORED for x in p.relative_to(root).parts)
                  and p.suffix != ".pyc")


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def local_path(root: Path, value: str) -> Path:
    check(isinstance(value, str) and value.startswith("./"), f"Relative path required: {value!r}")
    path = (root / value).resolve()
    check(path.is_relative_to(root.resolve()), f"Path escapes package: {value}")
    check(path.exists(), f"Missing package path: {value}")
    return path


def validate() -> dict:
    files = project_files()
    forbidden_suffixes = {".ttf", ".otf", ".woff", ".woff2", ".ttc", ".pdf", ".zip", ".bundle"}
    sensitive = re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
    for path in files:
        check(not path.is_symlink(), f"Symlink not permitted: {path}")
        check(path.suffix.lower() not in forbidden_suffixes, f"Excluded distributable asset: {path}")
        check(not path.name.startswith(".env") and path.name not in {"credentials", "id_rsa", "id_ed25519"}, f"Sensitive filename: {path}")
        if path.suffix.lower() == ".png":
            data = path.read_bytes()
            check(data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR", f"Invalid PNG: {path}")
            width, height = struct.unpack(">II", data[16:24])
            check(0 < width <= 4096 and 0 < height <= 4096 and len(data) <= 5 * 1024 * 1024, f"Oversized image: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        check(not sensitive.search(text), f"Possible credential in {path}")
        check(not re.search(r"/(?:workspace|Users|home)/", text), f"Private machine path in {path}")
        if path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if re.match(r"https?://|mailto:|#", target):
                    continue
                target = target.split("#", 1)[0]
                check((path.parent / target).is_file(), f"Broken local link in {path}: {target}")

    manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
    check(manifest["name"] == "typography-studio", "Wrong plugin identity")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])), "Explicit semantic version required")
    check("$schema" not in manifest, "Codex compatibility manifest should omit portable schema")
    check(manifest["author"].get("name") and manifest["license"] == "MIT", "Publisher/license missing")
    check(local_path(PLUGIN, manifest["skills"]) == SKILL.parent, "Skills directory mismatch")
    check(not any(key in manifest for key in ("mcpServers", "apps", "hooks")), "Unexpected service/hook declaration")
    ui = manifest["interface"]
    for field, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80)):
        check(isinstance(ui.get(field), str) and 0 < len(ui[field]) <= limit, f"Listing field invalid: {field}")
    check(isinstance(ui.get("capabilities"), list) and len(ui["capabilities"]) <= 20, "Invalid capabilities")
    check(bool(ui.get("category")), "Category missing")
    prompts = ui.get("defaultPrompt", [])
    check(isinstance(prompts, list) and len(prompts) <= 3 and all(0 < len(p) <= 128 for p in prompts), "Invalid prompts")
    for key in ("logo", "composerIcon"):
        icon = local_path(PLUGIN, ui[key])
        check(icon.suffix == ".svg", "This distribution uses SVG icons")
        tree = ET.parse(icon)
        viewbox = [float(x) for x in tree.getroot().attrib["viewBox"].split()]
        check(viewbox[2] == viewbox[3] and viewbox[2] >= 48, f"Icon dimensions invalid: {icon}")
        check(icon.stat().st_size <= 5 * 1024 * 1024, "Icon exceeds submission size")
        check(all(node.tag.rsplit("}", 1)[-1] not in {"script", "foreignObject", "image"} for node in tree.iter()), "Nonlocal icon content")
    publication = manifest["extensions"]["com.openai"]["publication"]
    for translation in publication.get("translations", {}).values():
        check(len(translation.get("subtitle", "")) <= 30 and len(translation.get("description", "")) <= 4000, "Translation limits exceeded")

    market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry = market["plugins"][0]
    check(market["name"] == "typography-studio-marketplace" and len(market["plugins"]) == 1, "Marketplace identity mismatch")
    check(entry["name"] == manifest["name"] and local_path(ROOT, entry["source"]["path"]) == PLUGIN, "Marketplace target mismatch")
    check(entry["source"]["source"] == "local" and entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Marketplace policy mismatch")

    instructions = (SKILL / "SKILL.md").read_text()
    match = re.match(r"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", instructions)
    check(match is not None and match[1] == SKILL.name, "Skill frontmatter invalid")
    check(len(instructions.splitlines()) <= 500 and len(match[2]) < 1024, "Skill metadata/body too long")
    yaml = (SKILL / "agents/openai.yaml").read_text()
    fields = {key: json.loads(value) for key, value in re.findall(r'^\s+(display_name|short_description|default_prompt): (".*")$', yaml, re.M)}
    check(25 <= len(fields["short_description"]) <= 64, "Skill UI description length invalid")
    check("$" + SKILL.name in fields["default_prompt"], "Skill UI prompt needs invocation")
    for name in ("inspect_font.py", "build_proof.py", "capture_proof.mjs", "font_evidence.py"):
        check((SKILL / "scripts" / name).is_file(), f"Missing promised helper: {name}")
    for path in files:
        if path.suffix == ".py":
            compile(path.read_text(), str(path), "exec")
    check((ROOT / "LICENSE").read_text().startswith("MIT License"), "MIT license missing")
    check((SKILL / "LICENSE").read_bytes() == (ROOT / "LICENSE").read_bytes(), "Installable skill must retain the MIT notice")
    cases = json.loads((ROOT / "evals/cases.json").read_text())
    check("proposed" in cases["status"] and len(cases["cases"]) >= 8, "Evaluation status/scope missing")
    ids = [case["id"] for case in cases["cases"]]
    check(len(set(ids)) == len(ids), "Duplicate evaluation cases")
    return {"plugin": manifest["name"], "version": manifest["version"], "files_checked": len(files),
            "skill_lines": len(instructions.splitlines()), "proposed_evaluation_cases": len(ids),
            "limits": "Package/document checks, not official approval or an executed agent-quality benchmark."}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

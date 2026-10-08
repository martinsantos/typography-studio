#!/usr/bin/env python3
"""Build deterministic plugin, standalone skill and marketplace ZIPs."""
from __future__ import annotations
import argparse
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path
from validate import ROOT, PLUGIN, SKILL, project_files, validate, localized_manifest

FIXED_TIME = (2026, 10, 8, 0, 0, 0)


def archive(path: Path, entries: dict[str, Path]) -> dict:
    with zipfile.ZipFile(path, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for name, source in sorted(entries.items()):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            out.writestr(info, source.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(path) as check:
        if check.testzip() is not None or set(check.namelist()) != set(entries):
            raise ValueError(f"Archive failed integrity verification: {path}")
    return {"file": path.name, "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "entries": len(entries)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New output directory.")
    args = parser.parse_args()
    validation = validate()
    output = args.output.resolve()
    if output == ROOT or output.is_relative_to(PLUGIN):
        parser.error("Output cannot replace the project or be nested inside the plugin.")
    output.mkdir(parents=True, exist_ok=False)
    prefix = f'typography-studio-{validation["version"]}'
    plugin_entries = {path.relative_to(PLUGIN).as_posix(): path for path in project_files(PLUGIN)}
    plugin_entries["LICENSE"] = ROOT / "LICENSE"
    skill_entries = {(Path(".agents/skills/typography-design-review") / path.relative_to(SKILL)).as_posix(): path for path in project_files(SKILL)}
    skill_entries["TYPOGRAPHY-STUDIO-LICENSE.txt"] = ROOT / "LICENSE"
    marketplace_entries = {path.relative_to(ROOT).as_posix(): path for path in project_files() if not path.is_relative_to(output)}
    # Spanish editions retain the same install identity and executable helpers.
    # Replace entrypoints/defaults rather than installing a duplicate skill.
    replacements = {"SKILL.md": SKILL / "SKILL.es.md", "agents/openai.yaml": SKILL / "agents/openai.es.yaml"}
    for directory in ("references", "assets"):
        for translated in (SKILL / directory).glob("*.es.*"):
            replacements[f"{directory}/{translated.name.replace('.es.', '.')}"] = translated
    spanish_plugin = dict(plugin_entries)
    spanish_skill = dict(skill_entries)
    for name, source in replacements.items():
        spanish_plugin[f"skills/typography-design-review/{name}"] = source
        spanish_skill[f".agents/skills/typography-design-review/{name}"] = source
    spanish_plugin["README.md"] = PLUGIN / "README.es.md"
    # A localized marketplace is an install package. Maintainer tooling stays
    # in the canonical source checkout so it can rebuild both language editions.
    spanish_marketplace = {name: source for name, source in marketplace_entries.items()
                           if not name.startswith(("scripts/", ".github/"))}
    for name in ("README", "CONTRIBUTING"):
        spanish_marketplace[name + ".md"] = ROOT / (name + ".es.md")
    for translated in (ROOT / "docs").glob("*.es.md"):
        spanish_marketplace[f"docs/{translated.name.replace('.es.', '.')}"] = translated
    with tempfile.TemporaryDirectory(prefix="typography-localized-") as temporary:
        translated_manifest = Path(temporary) / "plugin.json"
        translated_manifest.write_text(json.dumps(localized_manifest("es"), ensure_ascii=False, indent=2) + "\n")
        spanish_plugin[".codex-plugin/plugin.json"] = translated_manifest
        spanish_marketplace.update({"plugins/typography-studio/" + name: source for name, source in spanish_plugin.items()})
        manifest = {"schema_version": 1, "version": validation["version"], "archives": [
            archive(output / f"{prefix}-plugin.zip", plugin_entries),
            archive(output / f"{prefix}-skill.zip", skill_entries),
            archive(output / f"{prefix}-plugin-es.zip", spanish_plugin),
            archive(output / f"{prefix}-skill-es.zip", spanish_skill),
            archive(output / f"{prefix}-marketplace.zip", marketplace_entries),
            archive(output / f"{prefix}-marketplace-es.zip", spanish_marketplace)]}
    (output / "SHA256SUMS").write_text("".join(f'{entry["sha256"]}  {entry["file"]}\n' for entry in manifest["archives"]))
    (output / "package-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

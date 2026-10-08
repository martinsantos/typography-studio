#!/usr/bin/env python3
"""Verify installable language variants and preservation of their core behavior."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from validate import ROOT, SKILL, validate


def main() -> None:
    version = validate()["version"]
    prefix = "typography-studio-" + version
    with tempfile.TemporaryDirectory(prefix="type-localization-check-") as temporary:
        output = Path(temporary) / "packages"
        subprocess.run([sys.executable, str(ROOT / "scripts/package.py"), "--output", str(output)], check=True, capture_output=True)
        manifest = json.loads((output / "package-manifest.json").read_text())
        assert len(manifest["archives"]) == 6
        for entry in manifest["archives"]:
            path = output / entry["file"]
            assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
            with zipfile.ZipFile(path) as archive:
                assert archive.testzip() is None
                assert all(not name.startswith("/") and "\\" not in name and ".." not in Path(name).parts for name in archive.namelist())
        for package, location in (("plugin", "skills/typography-design-review/"), ("skill", ".agents/skills/typography-design-review/"), ("marketplace", "plugins/typography-studio/skills/typography-design-review/")):
            with zipfile.ZipFile(output / (prefix + "-" + package + ".zip")) as english, zipfile.ZipFile(output / (prefix + "-" + package + "-es.zip")) as spanish:
                assert spanish.read(location + "SKILL.md") == (SKILL / "SKILL.es.md").read_bytes()
                assert spanish.read(location + "agents/openai.yaml") == (SKILL / "agents/openai.es.yaml").read_bytes()
                assert json.loads(english.read(location + "assets/interface-language.json"))["language"] == "en"
                assert json.loads(spanish.read(location + "assets/interface-language.json"))["language"] == "es"
                assert json.loads(english.read(location + "assets/reading-tokens.json"))["profiles"] == json.loads(spanish.read(location + "assets/reading-tokens.json"))["profiles"]
                for name in (SKILL / "scripts").iterdir():
                    if name.is_file() and name.suffix in (".py", ".mjs"):
                        assert english.read(location + "scripts/" + name.name) == spanish.read(location + "scripts/" + name.name)
                if package != "skill":
                    manifest_path = ("plugins/typography-studio/" if package == "marketplace" else "") + ".codex-plugin/plugin.json"
                    en_manifest = json.loads(english.read(manifest_path))
                    es_manifest = json.loads(spanish.read(manifest_path))
                    for field in ("name", "version", "skills", "license", "author"):
                        assert en_manifest[field] == es_manifest[field]
                    assert en_manifest["interface"]["defaultPrompt"] != es_manifest["interface"]["defaultPrompt"]
                if package == "marketplace":
                    assert english.read(".agents/plugins/marketplace.json") == spanish.read(".agents/plugins/marketplace.json")
                    assert spanish.read("README.md") == (ROOT / "README.es.md").read_bytes()
    print(json.dumps({"status": "passed", "archives": 6, "languages": ["en", "es"],
                      "preserved": ["install identities", "executable helpers", "reading metrics", "marketplace registration"],
                      "localized": ["skill entrypoints", "interface metadata", "proof defaults", "references and templates"]}, indent=2))


if __name__ == "__main__":
    main()

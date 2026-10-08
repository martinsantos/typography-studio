#!/usr/bin/env python3
"""Publish an initial public GitHub repository and release from this checkout."""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from validate import ROOT, PLUGIN, project_files, validate


def run(*args: str, allow_failure: bool = False) -> subprocess.CompletedProcess:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if result.returncode and not allow_failure:
        raise RuntimeError(f"{args[0]} operation failed: {result.stderr.strip() or result.stdout.strip()}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default="martinsantos/typography-studio", help="Initial public destination OWNER/NAME.")
    parser.add_argument("--execute", action="store_true", help="Create/push the public repository, tag and release.")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repository):
        parser.error("Repository must be OWNER/NAME.")
    validation = validate()
    version = validation["version"]
    destination = f"https://github.com/{args.repository}.git"
    tag = "v" + version
    if not args.execute:
        print(json.dumps({"repository": args.repository, "visibility": "public", "tag": tag,
                          "actions": ["validate", "create initial repository if absent", "push source/tag", "publish verified ZIP release"],
                          "limits": "Does not submit to OpenAI's public directory. Requires authorized GitHub CLI and Git access."}, indent=2))
        return

    # Complete local preparation before attempting remote publication.
    actor = json.loads(run("gh", "api", "user").stdout)
    top = run("git", "rev-parse", "--show-toplevel", allow_failure=True)
    if not top.returncode and Path(top.stdout.strip()).resolve() != ROOT:
        raise RuntimeError("Extract into a standalone folder; it currently belongs to another repository.")
    if top.returncode:
        run("git", "init", "-b", "main")
    if not run("git", "config", "user.name", allow_failure=True).stdout.strip():
        run("git", "config", "user.name", actor.get("name") or actor["login"])
    if not run("git", "config", "user.email", allow_failure=True).stdout.strip():
        run("git", "config", "user.email", f'{actor["id"]}+{actor["login"]}@users.noreply.github.com')
    head = run("git", "rev-parse", "--verify", "HEAD", allow_failure=True)
    if head.returncode:
        run("git", "add", "--", *(str(p.relative_to(ROOT)) for p in project_files()))
        run("git", "commit", "-m", f"Publish brand-independent Typography Studio {version}")
    if run("git", "status", "--porcelain").stdout.strip():
        raise RuntimeError("Review and commit local changes before publishing; existing changes are preserved.")
    if run("git", "branch", "--show-current").stdout.strip() != "main":
        raise RuntimeError("Initial publication expects the reviewed main branch.")
    remote = run("git", "config", "--get", "remote.origin.url", allow_failure=True)
    acceptable = {destination, destination.removesuffix(".git"), f"git@github.com:{args.repository}.git"}
    if not remote.returncode and remote.stdout.strip() not in acceptable:
        raise RuntimeError("Existing origin differs from the requested destination; it is preserved.")
    if remote.returncode:
        run("git", "remote", "add", "origin", destination)
    if (ROOT / "dist").exists():
        raise RuntimeError("dist already exists. Preserve it and use a fresh reviewed checkout for initial publication.")
    run(sys.executable, str(ROOT / "scripts/package.py"), "--output", str(ROOT / "dist"))
    sha = run("git", "rev-parse", "HEAD").stdout.strip()
    local_tag = run("git", "rev-parse", "--verify", tag + "^{commit}", allow_failure=True)
    if not local_tag.returncode and local_tag.stdout.strip() != sha:
        raise RuntimeError("Existing version tag points elsewhere and will not be changed.")
    if local_tag.returncode:
        run("git", "tag", "-a", tag, "-m", f"Typography Studio {version}")

    existing = run("gh", "api", f"repos/{args.repository}", allow_failure=True)
    if existing.returncode:
        if "404" not in existing.stderr and "404" not in existing.stdout:
            raise RuntimeError("Cannot determine repository access: " + existing.stderr.strip())
        run("gh", "repo", "create", args.repository, "--public", "--description",
            "Open agent skill and Codex plugin for type design, real visual font review, kerning, families and typographic hierarchy.")
    elif json.loads(existing.stdout)["private"]:
        raise RuntimeError("Destination is private; this initial publisher does not change existing visibility.")
    if run("git", "ls-remote", "--heads", "--tags", "origin").stdout.strip():
        raise RuntimeError("Destination already has history. This initial publisher refuses to overwrite or merge it.")
    run("git", "push", "--set-upstream", "origin", "main")
    run("git", "push", "origin", "refs/tags/" + tag)
    with tempfile.TemporaryDirectory(prefix="typography-publish-") as temp:
        topics = Path(temp) / "topics.json"
        topics.write_text(json.dumps({"names": ["typography", "font-design", "type-design", "agent-skills", "codex-plugin", "kerning", "variable-fonts"]}))
        run("gh", "api", f"repos/{args.repository}/topics", "--method", "PUT", "--input", str(topics))
    assets = [str(p) for p in sorted((ROOT / "dist").iterdir()) if p.is_file()]
    run("gh", "release", "create", tag, *assets, "--repo", args.repository, "--verify-tag",
        "--title", f"Typography Studio {version}", "--notes-file", str(ROOT / "docs/RELEASE.md"))
    published = json.loads(run("gh", "api", f"repos/{args.repository}").stdout)
    if published["private"]:
        raise RuntimeError("Publication visibility verification failed.")
    actual = run("git", "ls-remote", "origin", "refs/heads/main").stdout.split()[0]
    if actual != sha:
        raise RuntimeError("Remote SHA does not match the reviewed local HEAD.")
    release = run("gh", "release", "view", tag, "--repo", args.repository, "--json", "url", "--jq", ".url").stdout.strip()
    receipt = {"repository": published["html_url"], "release": release, "head": sha, "tag": tag,
               "public": True, "openai_directory": "not submitted by this script"}
    (ROOT / "dist/publication-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        print(f"Publication stopped: {exc}", file=sys.stderr)
        raise SystemExit(1)

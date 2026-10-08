#!/usr/bin/env python3
"""Exercise initial publishing with real local Git and simulated GitHub calls."""
from __future__ import annotations
import contextlib
import importlib
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile


def main() -> None:
    source = pathlib.Path(__file__).resolve().parents[1]
    validator = importlib.import_module('validate')
    publisher = importlib.import_module('publish')
    version = validator.validate()['version']
    tag = 'v' + version
    with tempfile.TemporaryDirectory(prefix='type-publisher-check-') as temporary:
        temp = pathlib.Path(temporary).resolve()
        project = temp / 'project'
        project.mkdir()
        for item in validator.project_files():
            target = project / item.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(item, target)
        remote = temp / 'bare.git'
        subprocess.run(['git', 'init', '--bare', '-b', 'main', str(remote)], check=True, capture_output=True)
        subprocess.run(['git', 'init', '-b', 'main', str(project)], check=True, capture_output=True)
        destination = 'https://github.com/case-owner/type-case.git'
        # Local fixture transport; no external Git service is contacted.
        subprocess.run(['git', '-C', str(project), 'config', f'url.{remote}.insteadOf', destination], check=True)
        validator.ROOT = publisher.ROOT = project
        validator.PLUGIN = publisher.PLUGIN = project / 'plugins/typography-studio'
        validator.SKILL = validator.PLUGIN / 'skills/typography-design-review'
        validator.project_files.__defaults__ = (project,)
        real_run = publisher.run
        calls = []
        state = {'created': False}

        def fake_remote(*args, allow_failure=False):
            if args[0] != 'gh':
                return real_run(*args, allow_failure=allow_failure)
            calls.append(args)
            if args[1:] == ('api', 'user'):
                value = {'login': 'case-owner', 'id': 1, 'name': 'Test Publisher'}
            elif args[1:] == ('api', 'repos/case-owner/type-case'):
                if not state['created']:
                    return subprocess.CompletedProcess(args, 1, '{}', 'gh: Not Found (HTTP 404)')
                value = {'private': False, 'html_url': 'https://github.com/case-owner/type-case'}
            elif args[1:3] == ('repo', 'create'):
                assert args[3] == 'case-owner/type-case' and '--public' in args
                state['created'] = True
                value = {}
            elif args[1:3] == ('release', 'create'):
                assert '--verify-tag' in args
                assets = [pathlib.Path(argument) for argument in args[4:] if argument.endswith(('.zip', 'SHA256SUMS', 'package-manifest.json'))]
                assert len(assets) == 8 and all(asset.is_file() for asset in assets)
                assert {'typography-studio-' + version + '-plugin-es.zip', 'typography-studio-' + version + '-skill-es.zip'} <= {asset.name for asset in assets}
                value = {}
            elif args[1:3] == ('release', 'view'):
                return subprocess.CompletedProcess(args, 0, 'https://github.com/case-owner/type-case/releases/tag/' + tag + '\n', '')
            elif args[1:3] == ('api', 'repos/case-owner/type-case/topics'):
                payload = pathlib.Path(args[args.index('--input') + 1])
                assert 'type-design' in json.loads(payload.read_text())['names']
                value = {}
            else:
                raise AssertionError(args)
            return subprocess.CompletedProcess(args, 0, json.dumps(value), '')

        publisher.run = fake_remote
        sys.argv = ['publish.py', '--execute', '--repository', 'case-owner/type-case']
        with contextlib.redirect_stdout(io.StringIO()):
            publisher.main()
        receipt = json.loads((project / 'dist/publication-receipt.json').read_text())
        sha = subprocess.check_output(['git', '-C', str(project), 'rev-parse', 'HEAD'], text=True).strip()
        remote_sha = subprocess.check_output(['git', '--git-dir', str(remote), 'rev-parse', 'main'], text=True).strip()
        assert sha == remote_sha == receipt['head']
        assert subprocess.check_output(['git', '--git-dir', str(remote), 'rev-parse', tag + '^{commit}'], text=True).strip() == sha

        def refused(reason, expected_reads):
            previous = len(calls)
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    publisher.main()
                    raise AssertionError('Preservation guard did not reject the operation')
                except RuntimeError as exc:
                    assert reason in str(exc), str(exc)
            assert len(calls) == previous + expected_reads
            assert all(call[1] == 'api' and len(call) == 3 for call in calls[previous:])
            assert subprocess.check_output(['git', '--git-dir', str(remote), 'rev-parse', 'main'], text=True).strip() == sha

        refused('dist already exists', 1)
        original = (project / 'README.md').read_bytes()
        with (project / 'README.md').open('a') as file:
            file.write('\nLocal review note.\n')
        refused('local changes', 1)
        (project / 'README.md').write_bytes(original)
        shutil.move(project / 'dist', temp / 'preserved-dist')
        refused('already has history', 2)
        subprocess.run(['git', '-C', str(project), 'remote', 'set-url', 'origin', 'https://github.com/other-owner/other-repo.git'], check=True)
        refused('origin differs', 1)
    print(json.dumps({'status': 'passed',
                      'real_git': ['initial commit', 'push to local bare remote', 'annotated tag', 'remote SHA'],
                      'simulated': 'GitHub API and release transport; no public repository was created.',
                      'preservation': ['existing distribution directory', 'uncommitted changes', 'destination history', 'different origin']}, indent=2))


if __name__ == '__main__':
    main()

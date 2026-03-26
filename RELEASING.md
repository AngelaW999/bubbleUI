# Releasing BubbleUI

This guide describes how to bump versions and publish a release for both packages in this repository.

## Release model

BubbleUI currently ships two packages:

- Python package: `bubbleui`
- React/web package: `bubbleui-js`

A valid release requires these three version values to match:

- `bubbleui/_version.py`
- `packages/bubbleui-js/package.json`
- Git tag in the format `vX.Y.Z`

Examples:

- Python version: `0.1.1`
- React version: `0.1.1`
- Git tag: `v0.1.1`

## Files involved

- Python version source: `bubbleui/_version.py`
- Python package metadata: `pyproject.toml`
- React version source: `packages/bubbleui-js/package.json`
- Version bump helper: `scripts/bump_version.py`
- Release preparation helper: `scripts/release_prepare.py`
- Version validation script: `scripts/release_metadata.py`
- Manual web package workflow: `.github/workflows/package-bubbleui-js.yml`
- Tag release workflow: `.github/workflows/release-bubbleui.yml`

## Fast path

Recommended command:

```bash
python scripts/release_prepare.py patch
```

This does all of the following:

- checks `git status`
- bumps both package versions together
- validates Python and React versions match
- validates the expected git tag format
- runs the Python smoke test
- prints the next `git commit`, `git tag`, and `git push` commands

If your working tree is intentionally dirty, you can use:

```bash
python scripts/release_prepare.py patch --allow-dirty
```

## Bump the version only

Recommended commands:

```bash
python scripts/bump_version.py patch
python scripts/bump_version.py minor
python scripts/bump_version.py major
```

You can also set an explicit version:

```bash
python scripts/bump_version.py 0.1.1
```

This updates both:

- `bubbleui/_version.py`
- `packages/bubbleui-js/package.json`

Increment mode expects the current Python and React versions to already match.

## Validate before release

From the repository root, run:

```bash
python scripts/release_metadata.py --require-match
python scripts/release_metadata.py --tag v0.1.1 --require-match
python tests/smoke_test.py
```

Optional syntax check:

```bash
python -m py_compile bubbleui\__init__.py bubbleui\_version.py scripts\bump_version.py scripts\release_prepare.py scripts\release_metadata.py tests\smoke_test.py
```

## Commit the version bump

```bash
git add bubbleui/_version.py packages/bubbleui-js/package.json pyproject.toml README.md packages/bubbleui-js/README.md RELEASING.md .github/workflows scripts
git commit -m "Release v0.1.1"
```

Adjust the file list if your release only changed part of the repo.

## Create and push the tag

```bash
git tag v0.1.1
git push origin main
git push origin v0.1.1
```

You can also push branch and tags together:

```bash
git push origin main --tags
```

## What GitHub Actions does

### `package-bubbleui-js`

Use this when you only want a React `.tgz` package artifact.

Trigger methods:

- Push to `main` with changes under `packages/bubbleui-js/**`
- Manual run from the Actions page

Output:

- `bubbleui-js-<version>.tgz` artifact

### `release-bubbleui`

Use this for a full release.

Trigger methods:

- Push a tag like `v0.1.1`
- Manual run from the Actions page with `release_tag=v0.1.1`

What it does:

- Validates tag and package versions
- Installs Python build tooling and project dependencies
- Runs the Python smoke test
- Builds Python distributions into `dist/`
- Packs `bubbleui-js-<version>.tgz`
- Uploads both Python and React artifacts

## Downloading release artifacts

After the workflow finishes, open the corresponding GitHub Actions run and download:

- Python artifacts from `bubbleui-python-vX.Y.Z`
- React artifact from `bubbleui-js-vX.Y.Z`

The React artifact contains a file like:

```text
bubbleui-js-0.1.1.tgz
```

Install it in another project with:

```bash
npm install /absolute/path/to/bubbleui-js-0.1.1.tgz
```

## Installing the Python package in another project

Directly from GitHub:

```bash
pip install git+https://github.com/AngelaW999/bubbleUI.git
```

If later you want stricter reproducibility, install from a specific tag:

```bash
pip install git+https://github.com/AngelaW999/bubbleUI.git@v0.1.1
```

## Recommended release checklist

1. Run `python scripts/release_prepare.py patch` or `python scripts/release_prepare.py X.Y.Z`.
2. Review `git status` and the changed files.
3. Commit the release changes.
4. Create and push `vX.Y.Z`.
5. Wait for `release-bubbleui` to finish.
6. Download and verify the uploaded artifacts.
7. Announce the version for downstream projects.

## If a release fails

- If the helper refuses to run, clean the working tree or use `--allow-dirty` deliberately.
- If the workflow says versions do not match, check `bubbleui/_version.py`, `package.json`, and the git tag.
- If the smoke test fails, run `python tests/smoke_test.py` locally first.
- If the React package artifact is missing, verify `packages/bubbleui-js/package.json` is valid and `npm pack` works locally.
- If the Python build fails, verify `python -m build` works locally after `pip install -e .`.

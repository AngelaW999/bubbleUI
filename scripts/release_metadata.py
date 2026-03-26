from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT_PATH = ROOT / "pyproject.toml"
PACKAGE_JSON_PATH = ROOT / "packages" / "bubbleui-js" / "package.json"
VERSION_MODULE_PATH = ROOT / "bubbleui" / "_version.py"


def read_python_version() -> str:
    namespace: dict[str, str] = {}
    exec(VERSION_MODULE_PATH.read_text(encoding="utf-8"), namespace)
    return namespace["__version__"]


def read_declared_python_version_source() -> str:
    data = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))
    return data["tool"]["setuptools"]["dynamic"]["version"]["attr"]


def read_js_version() -> str:
    data = json.loads(PACKAGE_JSON_PATH.read_text(encoding="utf-8"))
    return data["version"]


def normalize_tag(tag: str) -> str:
    return tag.removeprefix("refs/tags/").removeprefix("v")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate BubbleUI release metadata.")
    parser.add_argument("--tag", help="Git tag name such as v0.1.0")
    parser.add_argument("--require-match", action="store_true", help="Require Python and JS versions to match.")
    args = parser.parse_args()

    python_version = read_python_version()
    js_version = read_js_version()
    python_version_source = read_declared_python_version_source()

    print(f"Python version: {python_version}")
    print(f"Python version source: {python_version_source}")
    print(f"JS version: {js_version}")

    if args.require_match and python_version != js_version:
        print("Version mismatch: Python and JS package versions must match for a release.", file=sys.stderr)
        return 1

    if args.tag:
        normalized_tag = normalize_tag(args.tag)
        print(f"Normalized tag: {normalized_tag}")
        if normalized_tag != python_version or normalized_tag != js_version:
            print(
                "Tag/version mismatch: git tag must match both package versions, for example v0.1.0.",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

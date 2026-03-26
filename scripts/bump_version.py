from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION_MODULE_PATH = ROOT / "bubbleui" / "_version.py"
PACKAGE_JSON_PATH = ROOT / "packages" / "bubbleui-js" / "package.json"
VERSION_PATTERN = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?$")
BUMP_KINDS = {"patch", "minor", "major"}


def read_python_version() -> str:
    namespace: dict[str, str] = {}
    exec(VERSION_MODULE_PATH.read_text(encoding="utf-8"), namespace)
    return namespace["__version__"]


def read_js_package() -> dict:
    return json.loads(PACKAGE_JSON_PATH.read_text(encoding="utf-8"))


def validate_version(version: str) -> None:
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(
            "Invalid version format. Expected semantic-style version like 0.1.1 or 1.2.3-beta.1"
        )


def parse_core_version(version: str) -> tuple[int, int, int]:
    match = VERSION_PATTERN.fullmatch(version)
    if not match:
        raise ValueError("Increment mode only supports versions with major.minor.patch format.")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def resolve_target_version(current_version: str, requested: str) -> str:
    requested = requested.strip()
    if requested in BUMP_KINDS:
        major, minor, patch = parse_core_version(current_version)
        if requested == "patch":
            return f"{major}.{minor}.{patch + 1}"
        if requested == "minor":
            return f"{major}.{minor + 1}.0"
        return f"{major + 1}.0.0"

    validate_version(requested)
    return requested


def write_python_version(version: str) -> None:
    VERSION_MODULE_PATH.write_text(f'__version__ = "{version}"\n', encoding="utf-8")


def write_js_version(version: str) -> None:
    package_data = read_js_package()
    package_data["version"] = version
    PACKAGE_JSON_PATH.write_text(f'{json.dumps(package_data, indent=2, ensure_ascii=False)}\n', encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump BubbleUI Python and React package versions together.")
    parser.add_argument(
        "version",
        help="New shared version like 0.1.1, or one of: patch, minor, major",
    )
    args = parser.parse_args()

    current_python_version = read_python_version()
    current_js_version = read_js_package()["version"]

    print(f"Current Python version: {current_python_version}")
    print(f"Current JS version: {current_js_version}")

    if current_python_version != current_js_version:
        raise ValueError("Current Python and JS versions do not match. Fix them before using bump mode.")

    new_version = resolve_target_version(current_python_version, args.version)

    if current_python_version == new_version:
        print(f"Versions are already set to {new_version}. Nothing to change.")
        return 0

    write_python_version(new_version)
    write_js_version(new_version)

    print(f"Updated Python version to: {new_version}")
    print(f"Updated JS version to: {new_version}")
    print("Next step: run `python scripts/release_metadata.py --tag v%s --require-match`" % new_version)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

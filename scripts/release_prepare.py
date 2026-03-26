from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUMP_SCRIPT = ROOT / "scripts" / "bump_version.py"
METADATA_SCRIPT = ROOT / "scripts" / "release_metadata.py"
SMOKE_TEST = ROOT / "tests" / "smoke_test.py"


def run_command(args: list[str], description: str) -> None:
    print(f"==> {description}")
    result = subprocess.run(args, cwd=ROOT, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def get_git_status() -> str:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a BubbleUI release by bumping versions and running local validation."
    )
    parser.add_argument(
        "version",
        help="New version like 0.1.1, or one of: patch, minor, major",
    )
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow running even when git status is not clean.",
    )
    args = parser.parse_args()

    status = get_git_status()
    if status:
        print("Current git status:")
        print(status)
        if not args.allow_dirty:
            print(
                "Working tree is not clean. Commit or stash your changes first, or rerun with --allow-dirty.",
                file=sys.stderr,
            )
            return 1
        print("Proceeding because --allow-dirty was provided.")
    else:
        print("Git working tree is clean.")

    run_command([sys.executable, str(BUMP_SCRIPT), args.version], "Bump shared package versions")

    target = subprocess.run(
        [sys.executable, str(METADATA_SCRIPT), "--require-match"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    print(target.stdout.strip())
    if target.returncode != 0:
        if target.stderr.strip():
            print(target.stderr.strip(), file=sys.stderr)
        return target.returncode

    version_line = next(
        (line for line in target.stdout.splitlines() if line.startswith("Python version: ")),
        None,
    )
    if version_line is None:
        print("Could not determine bumped version from release metadata output.", file=sys.stderr)
        return 1
    version = version_line.split(": ", 1)[1].strip()
    tag = f"v{version}"

    run_command(
        [sys.executable, str(METADATA_SCRIPT), "--tag", tag, "--require-match"],
        f"Validate release metadata against {tag}",
    )
    run_command([sys.executable, str(SMOKE_TEST)], "Run smoke test")

    print()
    print("Release preparation finished successfully.")
    print(f"Prepared version: {version}")
    print("Suggested next steps:")
    print(f"  git add .")
    print(f"  git commit -m \"Release {tag}\"")
    print(f"  git tag {tag}")
    print("  git push origin main --tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

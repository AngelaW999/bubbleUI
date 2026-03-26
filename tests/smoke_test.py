from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from bubbleui import (
    BUBBLE_COLORS,
    BUBBLE_RADIUS,
    BUBBLE_SPACING,
    BubbleBadge,
    BubbleButton,
    BubbleCard,
    BubbleEmptyState,
    BubbleInput,
    BubbleSectionHeader,
    BubbleStatTile,
    build_theme_preview,
)


def run() -> None:
    assert BUBBLE_COLORS["primary"] == "#7CC8F8"
    assert BUBBLE_RADIUS["lg"] == 24
    assert BUBBLE_SPACING["md"] == 16
    assert BubbleButton(text="Action") is not None
    assert BubbleInput(label="Name") is not None
    assert BubbleBadge("Info") is not None
    assert BubbleSectionHeader("Title") is not None
    assert BubbleStatTile("Users", "12") is not None
    assert BubbleEmptyState("Empty", "No content") is not None
    assert BubbleCard(title="Card", content=BubbleInput(label="Nested")) is not None
    assert build_theme_preview() is not None


if __name__ == "__main__":
    run()
    print("BubbleUI smoke test passed.")

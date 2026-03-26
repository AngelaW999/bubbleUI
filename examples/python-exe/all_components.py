from __future__ import annotations

import sys
from pathlib import Path

import flet as ft

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

EXAMPLES_DIR = Path(__file__).resolve().parent
if str(EXAMPLES_DIR) not in sys.path:
    sys.path.insert(0, str(EXAMPLES_DIR))

from bubbleui import (
    BubbleBadge,
    BubbleButton,
    BubbleCard,
    BubbleEmptyState,
    BubbleInput,
    BubbleSectionHeader,
    BubbleStatTile,
    apply_bubble_theme,
)
from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_GRADIENT, BUBBLE_RADIUS, BUBBLE_SPACING
from showcase import apply_showcase_page, showcase_header, showcase_section, showcase_stack, stacked_rows


COMPONENT_TYPES = {
    "BubbleButton": ["primary", "secondary", "soft"],
    "BubbleBadge": ["info", "success", "warning", "danger"],
    "BubbleInput": ["default", "with_prefix_icon", "password"],
    "BubbleCard": ["basic", "with_subtitle", "with_actions"],
    "BubbleSectionHeader": ["simple", "with_subtitle", "with_trailing"],
    "BubbleStatTile": ["default", "with_hint", "with_icon"],
    "BubbleEmptyState": ["default", "with_action"],
}


def _color_chip(name: str, value: str) -> ft.Control:
    return ft.Container(
        width=170,
        padding=12,
        border_radius=12,
        bgcolor="#FFFFFF",
        border=ft.border.all(1, BUBBLE_COLORS["gray_100"]),
        content=ft.Column(
            controls=[
                ft.Container(height=42, border_radius=10, bgcolor=value),
                ft.Text(name, size=12, color=BUBBLE_COLORS["gray_500"]),
                ft.Text(value, size=13, weight=ft.FontWeight.W_600, color=BUBBLE_COLORS["accent_deep"]),
            ],
            spacing=8,
            tight=True,
        ),
    )


def _value_chip(name: str, value: int) -> ft.Control:
    return ft.Container(
        width=120,
        padding=12,
        border_radius=value if value < 100 else 20,
        bgcolor=BUBBLE_COLORS["white"],
        border=ft.border.all(1, BUBBLE_COLORS["gray_100"]),
        content=ft.Column(
            controls=[
                ft.Text(name, size=12, color=BUBBLE_COLORS["gray_500"]),
                ft.Text(str(value), size=18, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
                BubbleBadge("token"),
            ],
            spacing=8,
            tight=True,
        ),
    )


def main(page: ft.Page) -> None:
    apply_bubble_theme(page)
    apply_showcase_page(page, "BubbleUI Python EXE Components")

    color_controls = [_color_chip(name, value) for name, value in BUBBLE_COLORS.items()]
    radius_controls = [_value_chip(name, value) for name, value in BUBBLE_RADIUS.items()]
    spacing_controls = [_value_chip(name, value) for name, value in BUBBLE_SPACING.items()]

    page.add(
        ft.Container(
            expand=True,
            gradient=BUBBLE_GRADIENT,
            content=showcase_stack(
                [
                    showcase_header(
                        "BubbleUI Python EXE Components",
                        "A single Flet showcase covering the current Python-side components and design tokens.",
                        "Python",
                    ),
                    showcase_section(
                        title="BubbleButton",
                        subtitle="Action button with three visual variants.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleButton"],
                        content=ft.Column(
                            controls=[
                                BubbleButton("Primary", variant="primary"),
                                BubbleButton("Secondary", variant="secondary"),
                                BubbleButton("Soft", variant="soft"),
                            ],
                            spacing=12,
                            tight=True,
                        ),
                    ),
                    showcase_section(
                        title="BubbleBadge",
                        subtitle="Status or tag marker with semantic tones.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleBadge"],
                        content=stacked_rows(
                            [
                                BubbleBadge("Info", tone="info"),
                                BubbleBadge("Success", tone="success"),
                                BubbleBadge("Warning", tone="warning"),
                                BubbleBadge("Danger", tone="danger"),
                            ],
                            per_row=2,
                            spacing=10,
                            run_spacing=10,
                        ),
                    ),
                    showcase_section(
                        title="BubbleInput",
                        subtitle="Text input with optional icon and password mode.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleInput"],
                        content=ft.Column(
                            controls=[
                                BubbleInput("Default input", hint_text="Type here"),
                                BubbleInput("Search", hint_text="Find component", prefix_icon=ft.Icons.SEARCH),
                                BubbleInput("Password", password=True, value="secret123"),
                            ],
                            spacing=12,
                            tight=True,
                        ),
                    ),
                    showcase_section(
                        title="BubbleCard",
                        subtitle="Container shell for grouped content and actions.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleCard"],
                        content=BubbleCard(
                            title="Basic card",
                            subtitle="Subtitle example",
                            width=None,
                            content=ft.Text("Cards are the main layout container in BubbleUI."),
                            actions=[
                                BubbleButton("Save", variant="primary"),
                                BubbleButton("Cancel", variant="secondary"),
                            ],
                        ),
                    ),
                    showcase_section(
                        title="BubbleSectionHeader",
                        subtitle="Section title block for page or module headers.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleSectionHeader"],
                        content=ft.Column(
                            controls=[
                                BubbleSectionHeader("Simple header"),
                                BubbleSectionHeader("Detailed header", "With supporting subtitle text"),
                                BubbleSectionHeader(
                                    "Header with action",
                                    "Trailing controls supported",
                                    BubbleButton("Action", variant="soft"),
                                ),
                            ],
                            spacing=20,
                            tight=True,
                        ),
                    ),
                    showcase_section(
                        title="BubbleStatTile",
                        subtitle="Compact statistics card with icon and hint support.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleStatTile"],
                        content=ft.Column(
                            controls=[
                                BubbleStatTile("Projects", "12"),
                                BubbleStatTile("Builds", "43", hint="This week"),
                                BubbleStatTile(
                                    "Alerts",
                                    "3",
                                    icon=ft.Icons.NOTIFICATIONS_ACTIVE_OUTLINED,
                                    hint="Needs review",
                                ),
                            ],
                            spacing=12,
                            tight=True,
                        ),
                    ),
                    showcase_section(
                        title="BubbleEmptyState",
                        subtitle="Guided placeholder for empty screens and modules.",
                        note="Available types",
                        badges=COMPONENT_TYPES["BubbleEmptyState"],
                        content=BubbleEmptyState(
                            title="No data yet",
                            message="Use empty states to explain what belongs here and guide the next action.",
                            action=BubbleButton("Create item"),
                        ),
                    ),
                    showcase_section(
                        title="Design Tokens",
                        subtitle="Current color, radius, spacing, and gradient tokens.",
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    height=140,
                                    border_radius=20,
                                    gradient=BUBBLE_GRADIENT,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Text(
                                        "BUBBLE_GRADIENT",
                                        size=18,
                                        weight=ft.FontWeight.W_700,
                                        color=BUBBLE_COLORS["accent_deep"],
                                    ),
                                ),
                                BubbleCard(
                                    title="Colors",
                                    subtitle="Named color tokens",
                                    width=None,
                                    content=stacked_rows(color_controls, per_row=4, spacing=16, run_spacing=16),
                                ),
                                BubbleCard(
                                    title="Radius",
                                    subtitle="Rounded corner scale",
                                    width=None,
                                    content=stacked_rows(radius_controls, per_row=5, spacing=16, run_spacing=16),
                                ),
                                BubbleCard(
                                    title="Spacing",
                                    subtitle="Layout spacing scale",
                                    width=None,
                                    content=stacked_rows(spacing_controls, per_row=5, spacing=16, run_spacing=16),
                                ),
                            ],
                            spacing=16,
                            tight=True,
                        ),
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)

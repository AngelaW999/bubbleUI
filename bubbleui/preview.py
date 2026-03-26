from __future__ import annotations

import flet as ft

from .components import (
    BubbleBadge,
    BubbleButton,
    BubbleCard,
    BubbleEmptyState,
    BubbleInput,
    BubbleSectionHeader,
    BubbleStatTile,
)
from .design_token import BUBBLE_COLORS, BUBBLE_GRADIENT, BUBBLE_SPACING


def _chunk_controls(controls: list[ft.Control], size: int) -> list[list[ft.Control]]:
    return [controls[index:index + size] for index in range(0, len(controls), size)]


def _stacked_rows(controls: list[ft.Control], per_row: int, spacing: int = 12, run_spacing: int = 12) -> ft.Control:
    rows = [ft.Row(controls=row_controls, spacing=spacing) for row_controls in _chunk_controls(controls, per_row)]
    return ft.Column(controls=rows, spacing=run_spacing, tight=True)


def _page_stack(controls: list[ft.Control]) -> ft.Control:
    return ft.Column(controls=controls, spacing=BUBBLE_SPACING["lg"], tight=True)


def _preview_header() -> ft.Control:
    return BubbleSectionHeader(
        title="BubbleUI Theme Preview",
        subtitle="Light blue for primary actions, layered with gray neutrals and deep blue structure.",
        trailing=BubbleBadge("Preview"),
    )


def _color_chip(name: str, color: str) -> ft.Control:
    return ft.Container(
        width=150,
        padding=12,
        border_radius=16,
        bgcolor="#FFFFFF",
        border=ft.border.all(1, BUBBLE_COLORS["gray_100"]),
        content=ft.Column(
            controls=[
                ft.Container(height=42, border_radius=12, bgcolor=color),
                ft.Text(name, size=12, color=BUBBLE_COLORS["gray_500"]),
                ft.Text(color, size=13, weight=ft.FontWeight.W_600, color=BUBBLE_COLORS["accent_deep"]),
            ],
            spacing=8,
            tight=True,
        ),
    )


def build_theme_preview() -> ft.Control:
    palette_grid = _stacked_rows(
        [
            _color_chip("Primary", BUBBLE_COLORS["primary"]),
            _color_chip("Primary Soft", BUBBLE_COLORS["primary_soft"]),
            _color_chip("Accent Dark", BUBBLE_COLORS["accent_dark"]),
            _color_chip("Accent Deep", BUBBLE_COLORS["accent_deep"]),
            _color_chip("Gray 100", BUBBLE_COLORS["gray_100"]),
            _color_chip("Gray 500", BUBBLE_COLORS["gray_500"]),
        ],
        per_row=3,
        spacing=16,
        run_spacing=16,
    )

    form_controls = ft.Column(
        controls=[
            BubbleInput("Workspace", "BubbleUI"),
            BubbleInput("Search", "Search components", prefix_icon=ft.Icons.SEARCH),
            ft.Column(
                controls=[
                    BubbleButton("Primary Action"),
                    BubbleButton("Secondary", variant="secondary"),
                    BubbleButton("Soft", variant="soft"),
                ],
                spacing=12,
                tight=True,
            ),
            _stacked_rows(
                [
                    BubbleBadge("Info"),
                    BubbleBadge("Success", tone="success"),
                    BubbleBadge("Warning", tone="warning"),
                    BubbleBadge("Danger", tone="danger"),
                ],
                per_row=2,
                spacing=10,
                run_spacing=10,
            ),
        ],
        spacing=BUBBLE_SPACING["md"],
        tight=True,
    )

    stats = ft.ResponsiveRow(
        controls=[
            ft.Container(col={"sm": 12, "md": 6}, content=BubbleStatTile("Components", "7", ft.Icons.WIDGETS_OUTLINED, "Ready to reuse")),
            ft.Container(col={"sm": 12, "md": 6}, content=BubbleStatTile("Theme", "Light", ft.Icons.PALETTE_OUTLINED, "Blue-led visual system")),
            ft.Container(col={"sm": 12, "md": 6}, content=BubbleStatTile("Target", "Desktop/Web", ft.Icons.DESKTOP_WINDOWS_OUTLINED, "Built with Flet")),
            ft.Container(col={"sm": 12, "md": 6}, content=BubbleStatTile("Status", "Starter", ft.Icons.ROCKET_LAUNCH_OUTLINED, "Good base for expansion")),
        ],
        spacing=16,
        run_spacing=16,
    )

    showcase = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={"sm": 12, "md": 6},
                content=BubbleCard(
                    title="Form Controls",
                    subtitle="Foundational input and action patterns",
                    width=None,
                    content=form_controls,
                ),
            ),
            ft.Container(
                col={"sm": 12, "md": 6},
                content=BubbleEmptyState(
                    title="No items yet",
                    message="Use BubbleUI components as your shared style layer so each new app starts with the same visual language.",
                    action=BubbleButton("Create First Item"),
                ),
            ),
        ],
        spacing=16,
        run_spacing=16,
    )

    return ft.Container(
        expand=True,
        gradient=BUBBLE_GRADIENT,
        content=_page_stack(
            [
                _preview_header(),
                stats,
                BubbleCard(
                    title="Palette",
                    subtitle="Core design tokens",
                    width=None,
                    content=palette_grid,
                ),
                showcase,
            ]
        ),
    )
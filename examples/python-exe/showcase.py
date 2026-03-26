from __future__ import annotations

import flet as ft

from bubbleui import BubbleBadge, BubbleCard, BubbleSectionHeader
from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_SPACING


def apply_showcase_page(page: ft.Page, title: str) -> None:
    page.title = title
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 24


def chunk_controls(controls: list[ft.Control], size: int) -> list[list[ft.Control]]:
    return [controls[index:index + size] for index in range(0, len(controls), size)]


def stacked_rows(
    controls: list[ft.Control],
    per_row: int,
    spacing: int = 12,
    run_spacing: int = 12,
) -> ft.Control:
    rows = [ft.Row(controls=row_controls, spacing=spacing, wrap=True) for row_controls in chunk_controls(controls, per_row)]
    return ft.Column(controls=rows, spacing=run_spacing, tight=True)


def showcase_header(title: str, subtitle: str, badge_text: str) -> ft.Control:
    return BubbleSectionHeader(
        title=title,
        subtitle=subtitle,
        trailing=BubbleBadge(badge_text),
    )


def showcase_stack(controls: list[ft.Control]) -> ft.Control:
    return ft.Column(controls=controls, spacing=BUBBLE_SPACING["lg"], tight=True)


def section_note(text: str) -> ft.Control:
    return ft.Text(text, size=12, color=BUBBLE_COLORS["gray_500"])


def types_gallery(labels: list[str], per_row: int = 4) -> ft.Control:
    return stacked_rows([BubbleBadge(label, tone="info") for label in labels], per_row=per_row, spacing=8, run_spacing=8)


def showcase_section(
    title: str,
    subtitle: str,
    content: ft.Control,
    note: str | None = None,
    badges: list[str] | None = None,
    badges_per_row: int = 4,
) -> ft.Control:
    section_controls: list[ft.Control] = []
    if note:
        section_controls.append(section_note(note))
    if badges:
        section_controls.append(types_gallery(badges, per_row=badges_per_row))
    if note or badges:
        section_controls.append(ft.Divider(height=20, color=BUBBLE_COLORS["gray_100"]))
    section_controls.append(content)

    return BubbleCard(
        title=title,
        subtitle=subtitle,
        width=None,
        content=ft.Column(controls=section_controls, spacing=BUBBLE_SPACING["md"], tight=True),
    )

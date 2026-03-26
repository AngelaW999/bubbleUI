from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_RADIUS, BUBBLE_SPACING


def BubbleButton(
    text: str,
    on_click=None,
    icon: str | None = None,
    variant: str = "primary",
    expand: bool = False,
    disabled: bool = False,
) -> ft.Control:
    palettes = {
        "primary": {"bg": BUBBLE_COLORS["primary"], "fg": BUBBLE_COLORS["accent_deep"], "border": BUBBLE_COLORS["primary"]},
        "secondary": {"bg": BUBBLE_COLORS["white"], "fg": BUBBLE_COLORS["accent_dark"], "border": BUBBLE_COLORS["gray_300"]},
        "soft": {"bg": BUBBLE_COLORS["primary_soft"], "fg": BUBBLE_COLORS["accent_dark"], "border": BUBBLE_COLORS["secondary_soft"]},
    }
    palette = palettes.get(variant, palettes["primary"])

    label = ft.Text(
        text,
        color=palette["fg"],
        size=14,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
    )

    content: ft.Control
    if icon:
        content = ft.Row(
            controls=[
                ft.Icon(icon, size=16, color=palette["fg"]),
                label,
            ],
            spacing=8,
            tight=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    else:
        content = label

    button = ft.Container(
        content=content,
        expand=expand,
        height=40,
        padding=ft.Padding(BUBBLE_SPACING["md"], 0, BUBBLE_SPACING["md"], 0),
        alignment=ft.Alignment(0, 0),
        bgcolor=palette["bg"],
        border=ft.border.all(1, palette["border"]),
        border_radius=ft.border_radius.all(BUBBLE_RADIUS["pill"]),
        opacity=0.55 if disabled else 1,
    )

    if on_click and not disabled:
        button.on_click = on_click

    return button
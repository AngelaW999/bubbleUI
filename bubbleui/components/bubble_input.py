from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_RADIUS


def BubbleInput(label: str, hint_text: str = "", password: bool = False, width: int | None = 320, value: str | None = None, prefix_icon: str | None = None) -> ft.Control:
    return ft.TextField(
        label=label,
        hint_text=hint_text,
        password=password,
        can_reveal_password=password,
        width=width,
        value=value,
        prefix_icon=prefix_icon,
        cursor_color=BUBBLE_COLORS["accent_dark"],
        text_style=ft.TextStyle(color=BUBBLE_COLORS["accent_deep"], size=14),
        border_radius=BUBBLE_RADIUS["md"],
    )

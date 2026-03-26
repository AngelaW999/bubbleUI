from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS


def BubbleSectionHeader(title: str, subtitle: str | None = None, trailing: ft.Control | None = None) -> ft.Control:
    return ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text(title, size=24, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
                    *([ft.Text(subtitle, size=13, color=BUBBLE_COLORS["gray_500"])] if subtitle else []),
                ],
                spacing=4,
                tight=True,
            ),
            trailing or ft.Container(),
        ],
    )

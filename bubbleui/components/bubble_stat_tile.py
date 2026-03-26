from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_RADIUS, BUBBLE_SPACING


def BubbleStatTile(label: str, value: str, icon: str | None = None, hint: str | None = None) -> ft.Control:
    return ft.Container(
        padding=BUBBLE_SPACING["lg"],
        border_radius=ft.border_radius.all(BUBBLE_RADIUS["lg"]),
        bgcolor=BUBBLE_COLORS["white"],
        border=ft.border.all(1, BUBBLE_COLORS["gray_100"]),
        content=ft.Row(
            controls=[
                ft.Container(
                    width=44,
                    height=44,
                    border_radius=ft.border_radius.all(BUBBLE_RADIUS["md"]),
                    bgcolor=BUBBLE_COLORS["primary_soft"],
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(icon or ft.Icons.INSIGHTS, color=BUBBLE_COLORS["accent_dark"]),
                ),
                ft.Column(
                    controls=[
                        ft.Text(label, size=12, color=BUBBLE_COLORS["gray_500"]),
                        ft.Text(value, size=22, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
                        *([ft.Text(hint, size=12, color=BUBBLE_COLORS["gray_500"])] if hint else []),
                    ],
                    spacing=4,
                    tight=True,
                ),
            ],
            spacing=BUBBLE_SPACING["md"],
        ),
    )

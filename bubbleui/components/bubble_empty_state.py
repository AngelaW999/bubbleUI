from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_RADIUS, BUBBLE_SPACING


def BubbleEmptyState(title: str, message: str, icon: str | None = None, action: ft.Control | None = None) -> ft.Control:
    controls: list[ft.Control] = [
        ft.Container(
            width=64,
            height=64,
            border_radius=ft.border_radius.all(BUBBLE_RADIUS["lg"]),
            bgcolor=BUBBLE_COLORS["primary_soft"],
            alignment=ft.Alignment(0, 0),
            content=ft.Icon(icon or ft.Icons.INVENTORY_2_OUTLINED, color=BUBBLE_COLORS["accent_dark"], size=28),
        ),
        ft.Text(title, size=20, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
        ft.Text(message, size=13, color=BUBBLE_COLORS["gray_500"], text_align=ft.TextAlign.CENTER),
    ]
    if action:
        controls.append(action)
    return ft.Container(
        padding=BUBBLE_SPACING["xl"],
        border_radius=ft.border_radius.all(BUBBLE_RADIUS["xl"]),
        bgcolor=BUBBLE_COLORS["white"],
        border=ft.border.all(1, BUBBLE_COLORS["gray_100"]),
        content=ft.Column(controls=controls, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=BUBBLE_SPACING["md"], tight=True),
    )

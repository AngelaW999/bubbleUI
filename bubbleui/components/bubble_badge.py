from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_RADIUS, BUBBLE_SPACING


def BubbleBadge(text: str, tone: str = "info") -> ft.Control:
    tones = {
        "info": (BUBBLE_COLORS["primary_soft"], BUBBLE_COLORS["accent_dark"]),
        "success": ("#EAF7F1", BUBBLE_COLORS["success"]),
        "warning": ("#FFF6E8", BUBBLE_COLORS["warning"]),
        "danger": ("#FDEEEE", BUBBLE_COLORS["danger"]),
    }
    bgcolor, color = tones.get(tone, tones["info"])
    return ft.Container(
        padding=ft.Padding(BUBBLE_SPACING["sm"], 6, BUBBLE_SPACING["sm"], 6),
        bgcolor=bgcolor,
        border_radius=ft.border_radius.all(BUBBLE_RADIUS["pill"]),
        content=ft.Text(text, size=12, weight=ft.FontWeight.W_600, color=color),
    )

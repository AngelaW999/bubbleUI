from __future__ import annotations

import flet as ft

from bubbleui.design_token import BUBBLE_COLORS, BUBBLE_SPACING, card_style


def BubbleCard(title: str, content: ft.Control, subtitle: str | None = None, width: int | None = 420, actions: list[ft.Control] | None = None) -> ft.Control:
    bgcolor, radius, shadows = card_style()
    header = ft.Column(
        controls=[
            ft.Text(title, size=20, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
            *([ft.Text(subtitle, size=13, color=BUBBLE_COLORS["gray_500"])] if subtitle else []),
        ],
        spacing=6,
        tight=True,
    )

    body_controls = [header, content]
    if actions:
        body_controls.append(
            ft.Column(
                controls=actions,
                spacing=12,
                tight=True,
            )
        )

    return ft.Container(
        width=width,
        bgcolor=bgcolor,
        border_radius=radius,
        shadow=shadows,
        padding=BUBBLE_SPACING["lg"],
        content=ft.Column(controls=body_controls, spacing=BUBBLE_SPACING["md"], tight=True),
    )
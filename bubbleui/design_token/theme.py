from __future__ import annotations

import flet as ft


BUBBLE_COLORS = {
    "primary": "#7CC8F8",
    "primary_hover": "#68BCEC",
    "primary_soft": "#EAF6FF",
    "secondary_soft": "#D9ECFA",
    "accent_dark": "#1F4E79",
    "accent_deep": "#173754",
    "gray_50": "#F6F9FC",
    "gray_100": "#EAF0F5",
    "gray_200": "#D7E0E8",
    "gray_300": "#C2CEDA",
    "gray_500": "#6C7C8F",
    "gray_700": "#3E4C5C",
    "white": "#FFFFFF",
    "success": "#5BAE8B",
    "warning": "#D8A34D",
    "danger": "#D76B6B",
}

BUBBLE_GRADIENT = ft.LinearGradient(
    begin=ft.Alignment(-1, -1),
    end=ft.Alignment(1, 1),
    colors=["#F9FCFF", "#EDF7FF", "#E2F2FF"],
)

BUBBLE_RADIUS = {
    "sm": 10,
    "md": 16,
    "lg": 24,
    "xl": 32,
    "pill": 999,
}

BUBBLE_SPACING = {
    "xs": 6,
    "sm": 10,
    "md": 16,
    "lg": 24,
    "xl": 32,
    "xxl": 40,
}


def apply_bubble_theme(page: ft.Page) -> None:
    page.title = "BubbleUI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BUBBLE_COLORS["gray_50"]
    page.padding = BUBBLE_SPACING["xl"]
    page.scroll = ft.ScrollMode.AUTO
    page.theme = ft.Theme(
        color_scheme_seed=BUBBLE_COLORS["primary"],
        scaffold_bgcolor=BUBBLE_COLORS["gray_50"],
        card_bgcolor=BUBBLE_COLORS["white"],
        divider_color=BUBBLE_COLORS["gray_100"],
        text_theme=ft.TextTheme(
            headline_medium=ft.TextStyle(size=28, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
            title_large=ft.TextStyle(size=22, weight=ft.FontWeight.W_700, color=BUBBLE_COLORS["accent_deep"]),
            title_medium=ft.TextStyle(size=18, weight=ft.FontWeight.W_600, color=BUBBLE_COLORS["accent_dark"]),
            body_large=ft.TextStyle(size=14, color=BUBBLE_COLORS["gray_700"]),
            body_medium=ft.TextStyle(size=13, color=BUBBLE_COLORS["gray_500"]),
        ),
    )


def card_style() -> tuple[str, ft.BorderRadius, list[ft.BoxShadow]]:
    return (
        BUBBLE_COLORS["white"],
        ft.border_radius.all(BUBBLE_RADIUS["lg"]),
        [ft.BoxShadow(spread_radius=0, blur_radius=24, color="#17375412", offset=ft.Offset(0, 8))],
    )
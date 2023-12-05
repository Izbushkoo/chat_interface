import flet as ft
from flet import colors as cr


but_style_dark_style = ft.ButtonStyle(
    color={
        ft.MaterialState.DEFAULT: "#FFFFFF",
        ft.MaterialState.DISABLED: "#AEAEB2",
    },
    animation_duration=3,
    overlay_color={
        ft.MaterialState.PRESSED: ft.colors.with_opacity(0.1, "#f7f7ff")
    },
    padding=ft.padding.all(0),
    shape=ft.CircleBorder()
)

delete_but_style_card_unselected = ft.ButtonStyle(
    color={
        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0, "#23252B"),
        ft.MaterialState.HOVERED: "#FFFFFF",
        ft.MaterialState.DISABLED: "#AEAEB2",
        ft.MaterialState.PRESSED: "#FFFFFF",
        ft.MaterialState.SELECTED: "#FFFFFF"
    },
    animation_duration=3,
    overlay_color={
        ft.MaterialState.PRESSED: ft.colors.with_opacity(0.1, "#f7f7ff")
    },
    padding=ft.padding.all(0),
    shape=ft.CircleBorder()
)

delete_but_style_card_selected = ft.ButtonStyle(
    color={
        ft.MaterialState.DEFAULT: "#FFFFFF",
        ft.MaterialState.HOVERED: "#FFFFFF",
        ft.MaterialState.DISABLED: "#AEAEB2",
        ft.MaterialState.PRESSED: "#FFFFFF",
        ft.MaterialState.SELECTED: "#FFFFFF"
    },
    animation_duration=3,
    overlay_color={
        ft.MaterialState.PRESSED: ft.colors.with_opacity(0.1, "#f7f7ff")
    },
    padding=ft.padding.all(0),
    shape=ft.CircleBorder()
)

dark_theme_button_green_style = ft.ButtonStyle(
    bgcolor={
        ft.MaterialState.DEFAULT: "#64BD64",
        ft.MaterialState.HOVERED: "#509750",
        ft.MaterialState.PRESSED: "#509750",
        ft.MaterialState.FOCUSED: "#509750",
        ft.MaterialState.DISABLED: "#A2D7A2"
    },

    color={
        ft.MaterialState.DEFAULT: "#FFFFFF",
    },
)

dark_theme_button_grey_style = ft.ButtonStyle(
    bgcolor={
        ft.MaterialState.DEFAULT: "#49454F",
        ft.MaterialState.HOVERED: "#2C2C2E",
        ft.MaterialState.PRESSED: "#2C2C2E",
        ft.MaterialState.FOCUSED: "#2C2C2E",
        ft.MaterialState.DISABLED: "#509750"
    },
    color={
        ft.MaterialState.DEFAULT: "#FFFFFF",
    },
    elevation={
        ft.MaterialState.DEFAULT: 0
    },
    animation_duration=0,
    surface_tint_color={
        ft.MaterialState.DEFAULT: "#2C2C2E"
    },
    overlay_color={
        ft.MaterialState.DEFAULT: "#2C2C2E",

    }
)

dark_theme_button_grey_cache = ft.ButtonStyle(
    bgcolor={
        ft.MaterialState.DEFAULT: "#49454F",
        ft.MaterialState.HOVERED: "#2C2C2E",
        ft.MaterialState.PRESSED: "#2C2C2E",
        ft.MaterialState.FOCUSED: "#2C2C2E",
        ft.MaterialState.DISABLED: "#509750"
    },
    color={
        ft.MaterialState.DEFAULT: "#FFFFFF",
    },
    elevation={
        ft.MaterialState.DEFAULT: 0
    },
    animation_duration=0,
    surface_tint_color={
        ft.MaterialState.DEFAULT: "#2C2C2E"
    },
    overlay_color={
        ft.MaterialState.DEFAULT: "#2C2C2E",
        ft.MaterialState.PRESSED: ft.colors.with_opacity(0.1, "#f7f7ff")
    },
    padding=ft.padding.only(top=6, bottom=6, left=4, right=8),
    shape=ft.RoundedRectangleBorder(radius=8)
)


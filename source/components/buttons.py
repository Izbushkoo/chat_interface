import asyncio

import flet as ft


class CustomButton(ft.Container):

    def __init__(self,
                 icon,
                 icon_color,
                 icon_color_hover,
                 self_size: int = 24,
                 on_click=None,
                 on_hover=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shape = ft.BoxShape.CIRCLE
        self.border_radius = ft.border_radius.all(self_size // 2)
        self.width = self_size,
        self.height = self_size
        self.bgcolor = ft.colors.with_opacity(0, ft.colors.WHITE)
        self.padding = ft.padding.all(2)
        self.icon_color = icon_color
        self.icon_color_hover = icon_color_hover
        self.content = ft.Icon(name=icon, size=self_size - 4, color=icon_color)
        self.on_click = on_click
        self.on_hover = on_hover


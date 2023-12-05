import flet as ft


class ButtonText(ft.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight = ft.FontWeight.NORMAL
        self.size = 16
        self.height = 24
        self.font_family = 'Sans'
        self.color = "#FFFFFF"


class CardInterText(ft.Text):

    def __init__(self, max_lines=3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "#B0B0B0"
        self.weight = ft.FontWeight.W_200
        self.size = 14
        self.overflow = ft.TextOverflow.ELLIPSIS
        self.max_lines = max_lines
        self.text_align = ft.alignment.center
        self.font_family = "Inter"


import flet as ft


# class DarkTheme(ft.Theme):
    # def __init__(self):
    #     self.background_color = "#201F1F"
    #
    #     self.color_scheme = ft.ColorScheme(
    #         primary="#282C34",
    #         on_primary=
    #
    #     )


class PurpleTheme(ft.Theme):

    def __init__(self):
        self.color_scheme_seed = ft.colors.DEEP_PURPLE
        self.color_scheme = ft.ColorScheme(
            primary=ft.colors.DEEP_PURPLE_500,
            on_primary=ft.colors.WHITE,
            primary_container=ft.colors.DEEP_PURPLE_400,
            on_primary_container=ft.colors.WHITE
        )
        self.text_theme = ft.TextTheme(

        )



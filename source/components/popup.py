import datetime
from typing import Union, Type
from enum import Enum

import flet as ft

from source.components import cards, styles, test_data


class PopUpTypes(Enum):
    chat = "chat"
    roles = "roles"


class PopUp(ft.Container):

    def __init__(self,
                 data,
                 title: str, card_type: PopUpTypes, button_add_text: str, *args, **kwargs):
        self.fill_with = data
        self.title = ft.Container(
            content=ft.Text(value=title, size=24, color="#FFFFFF", font_family="Inter", weight=ft.FontWeight.W_300),
            alignment=ft.alignment.center
        )

        if card_type.value == PopUpTypes.chat.value:
            self.card: Type[cards.ChatCard] = cards.ChatCard
            self.button_style = styles.dark_theme_button_green_style
        elif card_type.value == PopUpTypes.roles.value:
            self.card: Type[cards.RolesCard] = cards.RolesCard
            self.button_style = styles.dark_theme_button_grey_style
        super().__init__(*args, **kwargs)
        self.bgcolor = "#23252B"
        self.width = 355
        self.border_radius = ft.border_radius.all(24)
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(left=20, right=20, top=16, bottom=10)
        self.button_open = ft.IconButton(
            icon=ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN_ROUNDED,
            selected_icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_ROUNDED,
            icon_size=24,
            style=styles.but_style_dark_style,
            on_click=self.on_button_click
        )
        self.button_add = ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.icons.ADD_ROUNDED, size=24, color="#FFFFFF"),
                    ft.Text(value=button_add_text, size=16, weight=ft.FontWeight.W_400)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            style=self.button_style,
            height=48,
            visible=False
        )
        self.chats = ft.Column(
            controls=[
            ],
            spacing=8,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.head = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        self.title,
                        self.button_open
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ),
            style=ft.ButtonStyle(
                padding=ft.padding.all(0),
                bgcolor={
                    ft.MaterialState.DEFAULT: "#23252B",
                },
                overlay_color={
                    ft.MaterialState.DEFAULT: "#23252B",
                    ft.MaterialState.HOVERED: "#23252B",
                },
                elevation=0,
            ), on_click=self.button_open.on_click
        )
        self.content = ft.Column(
            controls=[
                self.head,
                ft.Column(
                    controls=[
                        self.chats,
                        self.button_add
                    ], spacing=20,

                )
            ],
            # spacing=20
            alignment=ft.MainAxisAlignment.CENTER
        )

    async def on_button_click(self, e):
        if self.button_open.selected:
            self.button_open.selected = False
            await self.close_body()
        else:
            self.button_open.selected = True
            await self.open_body()

    async def open_body(self):
        self.fill_with_cards(self.fill_with)
        self.button_add.visible = True
        await self.update_async()

    async def close_body(self):
        self.chats.controls.clear()
        self.button_add.visible = False
        await self.update_async()

    def fill_with_cards(self, data):
        for item in data:
            self.chats.controls.append(
                self.card(id_=item['id'], main_text=item['text'], title=item['title'], selected=item['selected'])
            )




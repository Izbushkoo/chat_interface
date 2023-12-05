import asyncio

import flet as ft
import requests

from source.components import styles, test_data, cards


class InputBlock(ft.Container):

    def __init__(self,
                 on_mic_long_press,
                 on_submit,
                 on_cache_clear,
                 on_stop_click,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bgcolor = "#23252A"
        self.border = ft.border.only(top=ft.BorderSide(width=1, color="#494949"))
        self.padding = ft.padding.only(top=8)
        # self.border_radius = ft.border_radius.all(8)
        self.width = 1920
        self.micro_button = ft.Container(
            content=ft.IconButton(
                icon=ft.icons.MIC_OUTLINED,
                icon_size=24,
                style=styles.delete_but_style_card_selected,
            ),
            on_long_press=on_mic_long_press
        )
        self.cache_clear_button = ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.icons.DELETE_OUTLINE_ROUNDED,
                                    color="#FFB6B6",
                                    size=20
                                ),
                                ft.Text("Очиcтить кеш")
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        style=styles.dark_theme_button_grey_cache,
                        width=140,
                        on_click=on_cache_clear
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STOP_ROUNDED,
                                    color="#FFB6B6",
                                    size=20
                                ),
                                ft.Text("Оcтановить")
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        style=styles.dark_theme_button_grey_cache,
                        width=140,
                        on_click=on_stop_click
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            padding=ft.padding.only(right=42)
        )
        self.input = ft.Row(
            controls=[
                ft.TextField(
                    border_radius=ft.border_radius.all(8),
                    border=ft.border.all(1),
                    border_color="#49454F",
                    content_padding=ft.padding.only(left=12, right=12, top=2, bottom=2),
                    hint_text="Введите текст",
                    hint_style=ft.TextStyle(
                        size=16, color='#79747E'
                    ),
                    text_style=ft.TextStyle(
                        size=16, color=ft.colors.WHITE
                    ),
                    focused_border_width=1,
                    focused_border_color="#F2F2F7",
                    autofocus=True,
                    shift_enter=True,
                    cursor_height=24,
                    multiline=True,
                    max_lines=4,
                    expand=True,
                    on_submit=on_submit
                ),
                self.micro_button
            ],
            spacing=2
        )
        self.content = ft.Column(
            controls=[
                self.cache_clear_button,
                self.input
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=8
        )


class MainChat(ft.Container):

    def __init__(self,
                 win_height,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stop_event = asyncio.Event()
        self.bgcolor = "#23252A"
        self.border_radius = ft.border_radius.all(24)
        self.padding = ft.padding.only(top=24, bottom=24, left=24, right=10)
        self.messages_block = ft.Column(
            controls=[
            ],
            scroll=ft.ScrollMode.ALWAYS,
            auto_scroll=True,
            height=win_height * 0.6
        )
        self.fill_with_messages()
        self.input_block = InputBlock(
            on_mic_long_press=self.on_long_press_mic,
            on_submit=self.on_submit_press,
            on_cache_clear=self.on_cache_clear,
            margin=ft.margin.only(right=14),
            on_stop_click=self.stop_click
        )
        self.content = ft.Column(
            controls=[
                self.messages_block,
                self.input_block
            ],
            spacing=0,
        )

    async def on_long_press_mic(self, event):
        ...

    async def on_submit_press(self, event):
        message_text = event.control.value
        event.control.value = None
        await event.control.update_async()
        self.messages_block.controls.append(
            cards.Message(
                role=cards.RolesTypes.user,
                message=message_text,
                avatar='assets/images/avatar.png'
            )
        )
        await self.messages_block.update_async()
        await asyncio.sleep(1)
        render_message = cards.Message(
            role=cards.RolesTypes.assistant,
            message=''
        )
        self.messages_block.controls.append(
            render_message
        )
        await self.messages_block.update_async()
        self.input_block.input.controls[0].disabled = True
        await self.input_block.input.controls[0].update_async()

        s = requests.Session()
        r = s.get(
            'https://pol-qa-zlk74eumjq-ew.a.run.app/v1/search',
            params={"message": message_text}, stream=True
        )
        await render_message.render_stream(r, self.stop_event)

        self.input_block.input.controls[0].disabled = False
        await self.input_block.input.controls[0].update_async()

        # todo Logic to send req to api and show progres until get response

    async def stop_click(self, event):
        if not self.stop_event.is_set():
            self.stop_event.set()

    async def on_cache_clear(self, event):
        ...

    def fill_with_messages(self):

        for message in test_data.messages:
            self.messages_block.controls.append(
                cards.Message(
                    role=cards.RolesTypes(message['role']),
                    message=message['message'],
                    avatar=message.get('avatar', None)
                )
            )

    async def on_window_resize(self, win_height):
        self.messages_block.height = win_height * 0.6
        await self.messages_block.update_async()


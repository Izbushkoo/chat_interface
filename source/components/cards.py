import asyncio
import datetime
from abc import ABC
from enum import Enum
from typing import Union

import flet as ft
from source.components import texts, styles, buttons


class ChatCard(ft.Card):
    def __init__(self,
                 id_: str,
                 main_text: str,
                 title: datetime.datetime,
                 selected: bool = True,
                 on_card_click=None,
                 on_delete_button_click=None,
                 *args, **kwargs):
        self.id = id_
        self.selected = selected
        self.main_content = ft.Container(
            content=texts.CardInterText(value=main_text, expand=True)
        )

        self.delete_icon_button = buttons.CustomButton(
            icon=ft.icons.DELETE_OUTLINE_ROUNDED,
            icon_color=ft.colors.with_opacity(0, "#23252A"),
            icon_color_hover=ft.colors.WHITE,
            right=4,
            bottom=4
        )
        self.check_icon = ft.Container(
            content=ft.Icon(
                name=ft.icons.CHECK_ROUNDED, size=20, color="#FFFFFF"
            ),
            right=4,
            bottom=4,
            visible=False
        )
        if on_delete_button_click:
            self.delete_icon_button.on_click = on_delete_button_click
        self.time_and_icon = ft.Row(
            controls=[
                ft.Text(title.strftime("%d.%m.%Y %H:%M"),
                        size=12, height=24, weight=ft.FontWeight.NORMAL,
                        text_align=ft.alignment.center_left, color="#F2F1F1", font_family="Inter",
                        ),
            ],
            height=24,
            width=278,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        super().__init__(*args, **kwargs)
        self.color = "#23252A"
        self.shadow_color = ft.colors.with_opacity(0.3, "#6e7486")
        self.surface_tint_color = "#23252A"
        # self.width = 341
        self.elevation = 25
        self.content = ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            self.main_content,
                            self.time_and_icon
                        ],
                        spacing=15
                    ),
                    self.check_icon,
                ]
            ),
            padding=ft.padding.only(top=12, bottom=4, left=16, right=8),
            border=ft.border.all(1, color="#DBFDFC"),
            border_radius=ft.border_radius.all(12),
            on_hover=self.on_hover
        )
        if not on_card_click:
            self.content.on_click = self.on_card_click
        else:
            self.content.on_click = on_card_click
        self.margin = ft.margin.only(left=10, right=10, top=0, bottom=0)
        if self.selected:
            self.color = ft.colors.with_opacity(0.2, "#013500")
            self.content.border = ft.border.all(1, color="#00ff57")
            self.main_content.content.color = "#FFFFFF"
            self.check_icon.visible = True
        else:
            self.color = "#23252A"
            self.main_content.content.color = "#B0B0B0"
            self.content.border = ft.border.all(1, color="#DBFDFC")

    async def on_delete_icon_click(self, e):
        ...

    async def on_hover(self, e):
        if e.data == "true":
            self.content.content.controls.pop()
            self.content.content.controls.append(self.delete_icon_button)
            self.delete_icon_button.content.color = self.delete_icon_button.icon_color_hover
        else:
            self.content.content.controls.pop()
            self.content.content.controls.append(self.check_icon)
        await self.content.content.update_async()

    async def on_card_click(self, e):
        print('click')
        if not self.selected:
            self.check_icon.visible = True
            self.color = ft.colors.with_opacity(0.2, "#013500")
            self.content.border = ft.border.all(1, color="#00ff57")
            self.main_content.content.color = "#FFFFFF"
            self.selected = True
        else:
            self.check_icon.visible = False
            self.main_content.content.color = "#B0B0B0"
            self.color = "#23252A"
            self.selected = False
            self.content.border = ft.border.all(1, color="#DBFDFC")
        await self.update_async()


class RoleInputs(ft.TextField):

    def __init__(self, text, submit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_radius = ft.border_radius.all(8)
        self.border = ft.border.all(1)
        self.border_color = "#49454F"
        self.content_padding = ft.padding.only(left=12, right=12, top=16, bottom=10)
        self.hint_text = "...."
        self.label = text
        self.hint_style = ft.TextStyle(
            size=16, color='#79747E'
        )
        self.text_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE
        )
        self.label_style = ft.TextStyle(size=20, color=ft.colors.WHITE54)
        self.focused_border_width = 1
        self.focused_border_color = "#F2F2F7"
        self.autofocus = True
        self.shift_enter = True
        self.cursor_height = 24
        self.multiline = True
        self.expand = True
        self.on_submit = submit


class RolesCard(ft.Card):
    def __init__(self, 
                 id_: str,
                 selected: bool,
                 main_text: str, 
                 title: str,
                 on_delete_button_click=None,
                 on_edit_button_click=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id_
        self.title_text = title
        self.description_text = main_text
        # self.width = 341
        self.selected = selected
        self.title = ft.Text(
            value=self.title_text,
            size=16,
            weight=ft.FontWeight.W_200,
            font_family='Inter',
            overflow=ft.TextOverflow.ELLIPSIS,
            width=180
        )
        self.avatar = ft.CircleAvatar(
            content=ft.Image('assets/images/gpt.png'),
        )
        self.avatar.radius = 18
        self.main_content = ft.Container(
            content=texts.CardInterText(max_lines=4, value=self.description_text)
        )
        self.delete_button = buttons.CustomButton(
            icon=ft.icons.DELETE_OUTLINE_ROUNDED,
            icon_color=ft.colors.with_opacity(0, "#23252A"),
            icon_color_hover=ft.colors.WHITE,
            on_click=on_delete_button_click
        )
        self.edit_button = buttons.CustomButton(
            icon=ft.icons.EDIT,
            icon_color=ft.colors.with_opacity(0, "#23252A"),
            icon_color_hover=ft.colors.WHITE,
            on_click=on_edit_button_click
        )
        self.title_row = ft.Row(
            controls=[
                self.title,
                ft.Row(
                    controls=[
                        self.edit_button,
                        self.delete_button
                    ],
                    spacing=2
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=320
        )

        self.role_save_button = ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(
                    "Сохранить",
                    font_family="Inter",
                    size=14,
                    weight=ft.FontWeight.W_400
                ),
                style=styles.dark_theme_button_grey_style,
                width=255,
                on_click=self.save
            )
        )

        self.description_section = ft.Container(
            content=ft.Column(
                controls=[
                    self.title_row,
                    self.main_content,
                ],
                spacing=7,
            ),
            padding=ft.padding.only(left=48)
        )
        self.content = ft.Container(
            content=ft.Stack(
                controls=[
                    self.avatar,
                    self.description_section
                ]
            ),
            padding=ft.padding.only(top=12, bottom=12, left=16, right=16),
            border=ft.border.all(1, color="#DBFDFC"),
            border_radius=ft.border_radius.all(12),
            on_hover=self.on_hover,
            on_click=self.on_card_click
        )
        if on_edit_button_click:
            self.edit_button.on_click = on_edit_button_click
        else:
            self.edit_button.on_click = self.edit_click
        if self.selected:
            self.color = ft.colors.with_opacity(0.2, "#013500")
            self.content.border = ft.border.all(1, color="#00ff57")
            self.main_content.content.color = "#FFFFFF"
            self.title.color = "#FFFFFF"
        else:
            self.color = "#23252A"
            self.main_content.content.color = "#B0B0B0"
            self.title.color = "#B0B0B0"
            self.content.border = ft.border.all(1, color="#DBFDFC")

    async def listen_keyboard(self, event):
        if event.key == 'Escape':
            await self.construct_roles()
        event.page.on_keyboard_event = None
        await event.page.update_async()

    async def edit_click(self, event):
        event.page.on_keyboard_event = self.listen_keyboard
        await event.page.update_async()
        await self.construct_edit()

    async def construct_edit(self):
        self.description_section.content.controls = [
            ft.Container(
                content=RoleInputs(
                    value=self.title_text,
                    text="Название роли",
                    submit=self.next_focus,
                    max_lines=1,
                    max_length=20,
                    on_blur=self.validate_role_name,
                ),
            ),
            ft.Container(
                content=RoleInputs(
                    value=self.description_text,
                    text='Назначение роли',
                    submit=self.save,
                    max_lines=8,
                    on_blur=self.validate_description
                ),
            ),
            self.role_save_button
        ]
        await self.description_section.update_async()

    async def next_focus(self, e):
        await self.description_section.content.controls[1].content.focus_async()

    async def construct_roles(self):

        self.description_section.content.controls = [
            self.title_row,
            self.main_content,
        ]
        await self.description_section.update_async()

    async def validate_role_name(self, e):
        if not self.description_section.content.controls[0].content.value:
            self.description_section.content.controls[0].content.value = datetime.datetime.utcnow().strftime(
                                                                             "%d.%m.%Y %H:%M"
                                                                         )
        await self.description_section.content.controls[0].update_async()

    async def validate_description(self, e):
        if not self.description_section.content.controls[1].content.value:
            self.description_section.content.controls[1].content.value = "Чат бот помощник."
        await self.description_section.content.controls[1].update_async()

    async def save(self, e):
        await self.validate_role_name(e)
        await self.validate_description(e)
        self.title_text = self.description_section.content.controls[0].content.value
        self.description_text = self.description_section.content.controls[1].content.value
        self.title.value = self.description_section.content.controls[0].content.value
        self.main_content.content.value = self.description_section.content.controls[1].content.value
        await self.construct_roles()
        # todo logic to api call

    async def on_card_click(self, e):
        if not self.selected:
            self.color = ft.colors.with_opacity(0.2, "#013500")
            self.content.border = ft.border.all(1, color="#00ff57")
            self.main_content.content.color = "#FFFFFF"
            self.selected = True
        else:
            self.main_content.content.color = "#B0B0B0"
            self.color = "#23252A"
            self.selected = False
            self.content.border = ft.border.all(1, color="#DBFDFC")
        await self.update_async()

    async def on_hover(self, e):
        if e.data == "true":
            self.delete_button.content.color = self.delete_button.icon_color_hover
            self.edit_button.content.color = self.edit_button.icon_color_hover
        else:
            self.delete_button.content.color = self.delete_button.icon_color
            self.edit_button.content.color = self.edit_button.icon_color
        await self.delete_button.content.update_async()
        await self.edit_button.content.update_async()


class RolesTypes(Enum):
    user = 'user'
    assistant = 'assistant'


class Message(ft.Container):

    def __init__(self,
                 role: RolesTypes,
                 message: str,
                 avatar: Union[str, None] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = ft.Text(
            value=message,
            size=14,
            text_align=ft.alignment.center,
            font_family='Roboto',
            color="#D1D5DB",
        )
        self.avatar = ft.CircleAvatar(content=ft.Image(avatar))\
            if avatar else ft.CircleAvatar(content=ft.Image('assets/images/gpt.png'))
        self.avatar.radius = 18

        self.button = buttons.CustomButton(
            self_size=20,
            icon=ft.icons.COPY,
            icon_color=ft.colors.with_opacity(0, ft.colors.WHITE),
            icon_color_hover=ft.colors.WHITE,
            on_click=self.copy_click,
        )
        self.role_style(role)

        self.padding = ft.padding.only(left=10, right=4, top=10, bottom=10)
        self.margin = ft.margin.only(right=16, bottom=1)
        self.content = ft.Stack(
            controls=[
                self.avatar,
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.message
                        ],
                        wrap=True,
                        expand=True,
                        width=1920
                    ),
                    padding=ft.padding.only(left=52, right=44),
                    expand=True
                ),
                self.button
            ]
        )
        self.on_hover = self.hover

    def role_style(self, role):
        if role == RolesTypes.user:
            self.bgcolor = ft.colors.with_opacity(0.2, "#013500")
            self.border = ft.border.all(1, color="#006b17")
            self.border_radius = ft.border_radius.all(12)
        else:
            self.bgcolor = "#23252A"
            self.border = ft.border.all(1, color="#23252A")
            self.border_radius = ft.border_radius.all(12)
        self.button.top = 0
        self.button.right = 0
        self.avatar.bgcolor = self.bgcolor

    async def hover(self, e):
        self.button.content.color = self.button.icon_color_hover if e.data == 'true' else self.button.icon_color
        await self.button.content.update_async()

    async def copy_click(self, event):
        await event.page.set_clipboard_async(
            self.message.value
        )
        self.button.content.color = self.bgcolor
        await self.button.update_async()
        print(await event.page.get_clipboard_async())

    async def stream_render_message(self, message):
        self.message.value = ''
        for elem in list(message):
            await asyncio.sleep(0.01)
            self.message.value += elem
            await self.message.update_async()

    async def render_stream(self, stream, stop_event: asyncio.Event):
        self.message.value = ''
        for chunk in stream:
            if stop_event.is_set():
                stop_event.clear()
                break
            self.message.value += chunk.decode("utf-8")
            await self.message.update_async()

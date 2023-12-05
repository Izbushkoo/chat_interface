import asyncio

import flet as ft
from flet import colors as cl
import flet_fastapi
from source.components import styles, texts, cards, popup, main_chat, buttons, test_data


async def main(page: ft.Page):

    page.window_width = 500
    page.window_height = 400
    page.bgcolor = '#282C34'
    page.fonts = {
        "Inter": 'assets/fonts/Inter-Regular.otf',
        "Roboto": 'assets/fonts/Roboto.ttf'
    }
    page.scroll = ft.ScrollMode.ADAPTIVE
    # page.auto_scroll = True

    async def on_res(e):
        await chat.on_window_resize(e.page.window_height)

    chat = main_chat.MainChat(
        win_height=page.window_height
    )
    page.on_resize = on_res
    # await page.add_async(
    #     chat
    # )
    await page.add_async(
        popup.PopUp(
            data=test_data.data_for_roles,
            title="Роли",
            card_type=popup.PopUpTypes.roles,
            button_add_text='Добавить роль'
        ),
    )
    await page.add_async(
        popup.PopUp(
            data=test_data.data_for_chats,
            title="Чаты",
            card_type=popup.PopUpTypes.chat,
            button_add_text='Добавить чат'
        ),
    )

    # message = cards.Message(
    #     role=cards.RolesTypes.assistant,
    #     message="",
    #     avatar='assets/images/gpt.png'
    # )
    # await page.add_async(
    #     cards.Message(
    #         role=cards.RolesTypes.user,
    #         message='Hellsdfhjkcjkxhjkfdhgjksdfghdkfsgjkdfjghsdfkjhgsdkfjhgkjdfhgjkdfhkgjhsdfghdfkjghdfskjhg\nasdf as\nasdfasdfsdfhjkhjvkxcvjhdfjklasdfkjhsafjhskjdhfsadjhfkljhsdaflsdjfkhsadjfhkjdshjhsdfjkhasdfkjhdf\nsadfasdfa\nqeqer;werj',
    #         avatar='assets/images/avatar.png'
    #     ),
    #     message
    # )
    # await message.stream_render_message('Product design has come a long way from the early days of trial and error to the present day where inspiration, creativity and technology have combined to produce designs that are not only aesthetically appealing but also functional. In the world of product design, inspiration can come from a variety of sources including nature, art, culture and technology. This essay will examine how inspiration has led to the creation of some of the most innovative and unique products in the market today.')

    # await page.add_async(
    #     cards.RolesCard(
    #         id_=test_data.data_for_roles[0]['id'],
    #         title=test_data.data_for_roles[0]['title'],
    #         main_text=test_data.data_for_roles[0]['text'],
    #         selected=test_data.data_for_roles[0]['selected']
    #     ),
    #     cards.RolesCard(
    #         id_=test_data.data_for_roles[0]['id'],
    #         title=test_data.data_for_roles[0]['title'],
    #         main_text=test_data.data_for_roles[0]['text'],
    #         selected=True
    #     )
    # )
    # await page.add_async(
    #     cards.RoleInputs(
    #         'hello',
    #         submit=None
    #     )
    # )


# app = flet_fastapi.app(main)


if __name__ == "__main__":

    asyncio.run(ft.app_async(main))
    # uvicorn.run(app="main:app", port=8000, host='localhost', reload=True)
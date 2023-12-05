import datetime

# make request get data
# Stub
data_for_chats = [
    {
        "id": '123',
        "text": "напиши продающее оглавление про аудиторию",
        "title": datetime.datetime.utcnow(),
        "selected": False
    },
    {
        "id": '123',
        "text": "напиши продающий текст на тему продажи недвижимости.Говорящий за то что в сегменте торголве"
                " нежвижимости за год вырос обьем продаж",
        "title": datetime.datetime.utcnow(),
        "selected": True
    }
]
data_for_roles = [
    {
        "id": '123',
        "title": "Дизайнер",
        "text": """UX UI дизайн. дизайн презентаций, проведение исследований. Работа с Material design. Исследование пользователей, анализ. Проведение интервью. Составление карт эмпатий. Персон. Проектирование CJM.Написание скрипта для интервью. Проведение пользовательского тестирования и улучшение прототипа.""",
        "selected": False
    },
    {
        "id": '12',
        "title": 'Маркетолог',
        "text": """Формировать текст для Cv чтобы увеличить шанс получения работы.""",
        "selected": False
    },
    {
        "id": '13',
        "title": "Аналитик",
        "text": """Быть секси кошечкой""",
        "selected": False
    },
    {
        "id": '23',
        "title": "Разработчик",
        "text": """Ты и без этого справишься""",
        "selected": True
    }
]

messages = [
    {
        "role": "user",
        "message": "Hello, how are you?",
        "avatar": 'assets/images/avatar.png'
    },
    {
        "role": "assistant",
        "message": "hi, i am fine."
    },
    {
        "role": "user",
        "message": "Hello, how are you?",
        "avatar": 'assets/images/avatar.png'
},
    {
        "role": "assistant",
        "message": "hi, i am fine."
    },
    {
        "role": "user",
        "message": "Hello, how are you?",
        "avatar": 'assets/images/avatar.png'
    },
    {
        "role": "assistant",
        "message": "hi, i am fine."
    },
    {
        "role": "user",
        "message": "Hello, how are you?",
        "avatar": 'assets/images/avatar.png'
    },
    {
        "role": "assistant",
        "message": "hi, i am fine."
    },
]
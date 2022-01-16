from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Старт')
        ],
        [
            KeyboardButton(text='Результат'),
            KeyboardButton(text='Выход')
        ]
    ]
)


choice_yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ]
)

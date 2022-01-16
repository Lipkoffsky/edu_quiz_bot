from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choice = ['Камень', 'Ножницы', 'Бумага']

tictactoe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=choice[0])
        ],
        [
            KeyboardButton(text=choice[1])
        ],
        [
            KeyboardButton(text=choice[2])
        ]
    ]
)
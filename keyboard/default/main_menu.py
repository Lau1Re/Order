from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📦Новый ордер'),
            KeyboardButton(text='💰 Шопы'),

        ],
        [
            KeyboardButton(text='Калькулятор')
        ]
    ],
    resize_keyboard=True
)

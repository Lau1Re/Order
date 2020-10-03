from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вернуться к списку", callback_data='backlist')
        ]
    ]
)
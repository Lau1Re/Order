from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.config import ADM_LIST
from filters.IsPrivateChatCheck import IsPrivate
from keyboard.default import Menu
from loader import dp
from re import compile




@dp.message_handler(CommandStart(), user_id=ADM_LIST)
async def adm_start(message: types.Message):

    text = [
        f'Привет {message.from_user.full_name}☺️. Готов трудиться! Я буду помогать тебе оформлять ордеры в 📣 канал!',
        f'\n 📦Добавить новый ордер 👉 /order'
    ]

    await message.answer('\n'.join(text), reply_markup=Menu)

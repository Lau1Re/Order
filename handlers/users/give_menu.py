from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboard.default import Menu
from loader import dp


@dp.message_handler(Command('menu'))
async def give_main_menu(message: types.Message):
    await message.answer('Меню', reply_markup=Menu)

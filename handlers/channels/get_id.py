from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.channel_post_handler(Command('get_id'))
async def get_channel_id(message: types.Message):
    mes_id = message.message_id
    chat_id = message.chat.id
    await dp.bot.delete_message(chat_id, mes_id)
    await message.answer(f'ID Канала: {chat_id}')


from aiogram import types
from aiogram.dispatcher.filters import Command

from data import config
from keyboard.default import Menu
from loader import dp


@dp.message_handler(Command('add_admin'))
async def add_administrator(message: types.Message):
    admin_id = message.get_args()
    config.ADM_LIST.append(int(admin_id))
    await message.answer(f'Новый администратор: {admin_id} был успешно добавлен')
    try:
        await dp.bot.send_message(admin_id, 'Вы были успешно назначены администратором', reply_markup=Menu)

    except:
        await message.answer('Не удалось оповестить нового админа. Скорее всего он не запустил бота или удалил чат')

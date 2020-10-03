from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from data.config import list
from keyboard.inline.back_list import back_list
from keyboard.inline.shops_keyboard import shopkeyboard
from loader import dp


@dp.message_handler(Text(contains='Шопы'))
async def give_shop_markup(message: types.Message):
    await message.answer('Выберите шоп:', reply_markup=shopkeyboard)


@dp.callback_query_handler(Text(equals='1'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['1'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='2'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['2'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='3'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['3'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='4'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['4'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='4'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['4'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='5'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['5'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='6'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['6'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='7'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['7'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='8'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['8'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='9'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['9'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='10'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['10'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='11'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['11'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='12'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['12'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='13'))
async def multi_giver_list_shop(call: CallbackQuery):
    await call.message.edit_text(list['13'], reply_markup=back_list)

@dp.callback_query_handler(Text(equals='backlist'))
async def step_back(call: CallbackQuery):
    await call.message.edit_text('Выберите шоп снова:', reply_markup=shopkeyboard)

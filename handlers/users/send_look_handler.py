import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from data.config import CHAN_ID
from keyboard.default import Menu
from keyboard.inline.send_look_post import Send_Look
from loader import dp


@dp.callback_query_handler(Text(equals='send'))
async def send_post_to_chan(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()

    time_now = datetime.datetime.now().time()
    text = f"""
\n<b>▪️Кто вбил:</b> {date['name']}
<b>▪️Логин, пароль:</b> {date['LogPass']}
<b>▪️Товар:</b> {date['OrderName']}
<b>▪️ФИО:</b> {date['HolderName']}
<b>▪️Адрес:</b> {date['Address']}
\n<b>💰 Цена за товар:</b> {date['price']} $
<b>🕙 Дата: {time_now}</b> 

{date['Photo']}
            """

    await dp.bot.send_message(chat_id=CHAN_ID, text=text, disable_web_page_preview=False)
    await call.message.delete()
    await call.message.answer('Пост успешно запостен.', reply_markup=Menu)


@dp.callback_query_handler(Text(equals='look'))
async def post_preview(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()

    time_now = datetime.datetime.now().time()
    text = f"""
<b>Вот так будет выглядеть ваш пост:</b>
\n\n<b>▪️Кто вбил:</b> {date['name']}
<b>▪️Логин, пароль:</b> {date['LogPass']}
<b>▪️Товар:</b> {date['OrderName']}
<b>▪️ФИО:</b> {date['HolderName']}
<b>▪️Адрес:</b> {date['Address']}
\n<b>💰 Цена за товар:</b> {date['price']} $
<b>🕙 Дата: {time_now}</b> 

{date['Photo']}
            """
    await call.message.edit_text(text, reply_markup=Send_Look)

@dp.callback_query_handler(Text(equals='cancel'))
async def cancel_posting(call: CallbackQuery):
    await call.answer('Действие отменено!', show_alert=True)
    await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

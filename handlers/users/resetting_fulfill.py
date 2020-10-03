from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from keyboard.default import Menu
from keyboard.inline.reset_fullfil import Cancel
from loader import dp
from states import RegisterOrder

all_states = RegisterOrder.all_states




@dp.callback_query_handler(Text(equals='cancel'), state=RegisterOrder)
async def cancel_fulfill(call: CallbackQuery, state: FSMContext):
    await state.finish()

    await call.answer(show_alert=True)
    await call.message.answer('Заполнение отменено', reply_markup=Menu)
    mess_id = call.message.message_id
    await dp.bot.delete_message(call.message.chat.id, mess_id)


@dp.callback_query_handler(Text(equals='reset'), state=RegisterOrder)
async def reset_fulfill(call: CallbackQuery):
    text = '\n 🤑Приступим к оформлению нового ордера заново. <b>Укажи своё имя</b>, кто вбил ордер:'
    await RegisterOrder.first()
    await call.message.edit_text(text, reply_markup=Cancel)



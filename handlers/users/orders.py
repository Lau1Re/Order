from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.config import ADM_LIST
from filters.IsPrivateChatCheck import IsPrivate
from keyboard.inline.reset_fullfil import Resetting, Cancel
from keyboard.inline.send_look_post import Send_Look
from loader import dp
from states import RegisterOrder


@dp.message_handler(Text(contains='ордер'), IsPrivate(), user_id=ADM_LIST)
async def start_enter_order_info(message: types.Message):
    text = '\n 🤑Приступим к оформлению нового ордера заново. <b>Укажи своё имя</b>, кто вбил ордер:'

    await message.answer(text, reply_markup=Cancel)
    await RegisterOrder.first()


@dp.message_handler(state=RegisterOrder.NAME)
async def from_name_to_logpass(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f'Отлично, {message.text}. Теперь отправь мне <b>логин и пароль</b> аккаунта',
                         reply_markup=Resetting)

    await RegisterOrder.LogPass.set()


@dp.message_handler(state=RegisterOrder.LogPass)
async def from_logpass_to_Ordername(message: types.Message, state: FSMContext):
    await state.update_data(LogPass=message.text)
    await message.answer('Очень хорошо. Теперь отправь мне <b>имя товара</b>',
                         reply_markup=Resetting)
    await RegisterOrder.OrderName.set()


@dp.message_handler(state=RegisterOrder.OrderName)
async def from_OrderName_to_HolderName(message: types.Message, state: FSMContext):
    await state.update_data(OrderName=message.text)
    await message.answer('Теперь отправь мне <b>ФИО</b> владельца аккаунта',
                         reply_markup=Resetting)
    await RegisterOrder.HolderName.set()


@dp.message_handler(state=RegisterOrder.HolderName)
async def from_HolderName_to_Address(message: types.Message, state: FSMContext):
    await state.update_data(HolderName=message.text)

    await message.answer('Очень хорошо. Теперь я жду от тебя <b>адрес</b>',
                         reply_markup=Resetting)
    await RegisterOrder.Address.set()


@dp.message_handler(state=RegisterOrder.Address)
async def from_Address_to_Price(message: types.Message, state: FSMContext):
    await state.update_data(Address=message.text)
    await message.answer('И последнее. <b>Отправь цену товара</b>',
                         reply_markup=Resetting)
    await RegisterOrder.Price.set()


@dp.message_handler(state=RegisterOrder.Price)
async def finish_fsm(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.reset_state(with_data=False)
    text = 'Пост был успешно заполнен. Что будем делать с ним?'
    await message.answer(text, reply_markup=Send_Look)

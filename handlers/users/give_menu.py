from math import ceil

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from data.config import ADM_LIST
from keyboard.default import Menu
from loader import dp
from states.order import Calculator


@dp.message_handler(Command('menu'))
async def give_main_menu(message: types.Message):
    await message.answer('Меню', reply_markup=Menu)


@dp.message_handler(Command('calculator'))
async def adm_calculator(message: types.Message):
    await message.answer('<b>Введите текущую сумму и я посчитаю ваш чистый доход</b>'
                         '\n\n <code>1. Вычту 25% за услуги обнала'
                         '\n2. Отниму 50%</code>')

    await Calculator.Adm_amount.set()


@dp.message_handler(state=Calculator.Adm_amount, user_id=ADM_LIST)
async def adm_math_amount(message: types.Message, state: FSMContext):
    amount = message.text

    if amount.isdigit():
        amount = int(amount)
        result = (amount - ceil(amount * 25 / 100)) / 2
        await message.answer(f'Ваш чистый доход составляет: <b>{result}$</b>')
        await state.finish()
    else:
        await message.reply('Введите сумму (только цифры)')
        await Calculator.Adm_amount.set()


@dp.message_handler(Text(contains='Калькулятор'))
async def calculator(message: types.Message):
    await message.answer('<b>Введите текущую сумму и я посчитаю ваш чистый доход</b>'
                         '\n\n <code>1. Вычту 35% за услуги обнала'
                         '\n2. Отниму 50%</code>')

    await Calculator.first()


@dp.message_handler(state=Calculator.Amount, user_id=ADM_LIST)
async def math_amount(message: types.Message, state: FSMContext):
    amount = message.text

    if amount.isdigit():
        amount = int(amount)
        result = (amount - ceil(amount * 35 / 100)) / 2
        await message.answer(f'Ваш чистый доход составляет: <b>{result}$</b>')
        await state.finish()
    else:
        await message.reply('Введите сумму (только цифры)')
        await Calculator.first()

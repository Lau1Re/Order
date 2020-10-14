from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterOrder(StatesGroup):
    NAME = State()
    LogPass = State()
    OrderName = State()
    HolderName = State()
    Address = State()
    Photo = State()
    Price = State()

class Calculator(StatesGroup):
    Amount = State()
    Adm_amount = State()

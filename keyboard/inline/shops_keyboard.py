from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboard.inline.callback_datas import shop_callback

shopkeyboard = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 1',
                                                callback_data='1'),

                                            InlineKeyboardButton(
                                                text='Шоп 2', callback_data='2')
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 3',
                                                callback_data="3"),

                                            InlineKeyboardButton(
                                                text='Шоп 4', callback_data="4")
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 5',
                                                callback_data='5'),

                                            InlineKeyboardButton(
                                                text='Шоп 6', callback_data='6')
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 7',
                                                callback_data="7"),

                                            InlineKeyboardButton(
                                                text='Шоп 8', callback_data="8")
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 9',
                                                callback_data="9"),

                                            InlineKeyboardButton(
                                                text='Шоп 10', callback_data="10")
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 11',
                                                callback_data="11"),

                                            InlineKeyboardButton(
                                                text='Шоп 12', callback_data="12")
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Шоп 13',
                                                callback_data="13")

                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text='Назад', callback_data='cancel')
                                        ]

                                    ])

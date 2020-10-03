from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Resetting = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Начать заново',
                                                              callback_data='reset'),
                                         InlineKeyboardButton(text='Отмена',
                                                              callback_data='cancel')
                                     ]
                                 ])

Cancel = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='Отмена',
                                                           callback_data='cancel')
                                  ]
                              ])



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Send_Look = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Запостить в канал',
                                                              callback_data='send')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Посмотреть пост',
                                                              callback_data='look')
                                     ],
                                     [
                                         InlineKeyboardButton(text='Отменить',
                                                              callback_data='cancel')
                                     ],
                                 ])
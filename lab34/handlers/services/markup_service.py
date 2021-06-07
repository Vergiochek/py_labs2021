import telebot
from text_literals.reply_keyboard_buttons import *


def set_reply_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(ADD_CITY_BUTTON, REMOVE_CITY_BUTTON)
    markup.row(ADD_ALERT_BUTTON, STOP_ALERT_BUTTON)
    markup.row(GET_WEATHER_BUTTON)
    return markup


def set_inline_markup(arr, attr, flag, add=''):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for item in arr:
        data = getattr(item, attr)
        try:
            param = getattr(item, add)
        except AttributeError:
            param = ''
        button = telebot.types.InlineKeyboardButton(text=f'{data} {param}',
                                                    callback_data=f'{flag}{data} {param}')
        markup.add(button)
    return markup

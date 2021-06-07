from app import bot
from handlers.services.database_service import register_user
from text_literals.authorization_messages import *
import re
from handlers.services.markup_service import set_reply_markup
from text_literals.callback_prefixes import AUTHORIZE
from text_literals.reply_keyboard_buttons import GET_USERS, BAN_USERS, UNBAN_USERS


@bot.callback_query_handler(func=lambda call: call.data == AUTHORIZE)
def authorize(callback):
    bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
                                  message_id=callback.message.message_id, reply_markup=None)
    bot.send_message(callback.message.chat.id, PASSWORD_MESSAGE)
    bot.register_next_step_handler(callback.message, register)


def register(message):
    password = message.json['text']
    chat_id = message.chat.id
    if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,15}$', password):
        user_id = message.from_user.id
        user_name = message.chat.username
        register_user(user_id, user_name, password)
        markup = set_reply_markup()
        if user_name == ADMIN[1:]:
            markup.add(GET_USERS)
            markup.row(BAN_USERS, UNBAN_USERS)
        bot.send_message(chat_id, SUCCESS_REGISTRATION_MESSAGE, reply_markup=markup)
    else:
        bot.send_message(chat_id, INVALID_PASSWORD_MESSAGE)

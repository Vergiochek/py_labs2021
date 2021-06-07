import telebot.types

from models import User
from text_literals.command_messages import *
from text_literals.commands import *
from .authorization_handlers import *
from .services.database_service import user_is_banned


@bot.message_handler(commands=[START_COMMAND])
def start_command_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user = User.query.get(user_id)
    if user is None:
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        button = telebot.types.InlineKeyboardButton(text=AUTHORIZE, callback_data=AUTHORIZE)
        markup.add(button)
        text = START_MESSAGE
        if message.chat.username is None:
            text += f'\n\n{NO_USERNAME_MESSAGE}'
        bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)
    else:
        if not user_is_banned(chat_id, user_id):
            bot.send_message(chat_id=chat_id, text=AUTHORIZED_ENTER_MESSAGE)


@bot.message_handler(commands=[HELP_COMMAND])
def help_command_handler(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)

from app import bot
from handlers.services.database_service import get_users_by_attr, change_ban_status
from handlers.services.deletion_service import delete_by_callback
from handlers.services.markup_service import set_inline_markup
from models import User
from text_literals.admin_messages import *
from text_literals.callback_prefixes import BAN, UNBAN


@bot.callback_query_handler(func=lambda call: call.data.startswith(BAN))
def ban(callback):
    manipulate(callback, 3, -1, True, False, BAN, BAN_USER_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data.startswith(UNBAN))
def unban(callback):
    manipulate(callback, 5, -1, False, True, UNBAN, UNBAN_USER_MESSAGE)


def manipulate(callback, start, end, status, is_banned, flag, message):
    user_name = callback.data[start: end]
    change_ban_status(user_name, status)
    users = get_users_by_attr(User.is_banned, is_banned)
    markup = set_inline_markup(users, 'user_name', flag)
    delete_by_callback(callback, users, user_name, markup, message)

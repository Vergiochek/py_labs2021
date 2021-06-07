from text_literals.callback_prefixes import *
from text_literals.reply_keyboard_buttons import *
from text_literals.authorization_messages import *
from .services.database_service import *
from .services.alert_service import get_alert_cities
from .services.admin_service import *


@bot.message_handler()
def text_message_handler(message):
    user = User.query.get(message.from_user.id)
    chat_id = message.chat.id
    txt = message.text
    if user is None:
        bot.send_message(chat_id, UNAUTHORIZED_USER_MESSAGE)
    elif not user.is_banned:
        cities = get_cities(user.user_id)
        if txt == ADD_CITY_BUTTON:
            bot.send_message(chat_id, SET_CITY_MESSAGE)
            bot.register_next_step_handler(message, register_city)
        elif txt == GET_WEATHER_BUTTON or txt == REMOVE_CITY_BUTTON:
            if len(cities) == 0:
                bot.send_message(chat_id, NO_CITIES_MESSAGE)
            else:
                val = GET_WEATHER if txt == GET_WEATHER_BUTTON else REMOVE_CITY
                markup = set_inline_markup(cities, 'city_name', val)
                bot.send_message(chat_id=chat_id, text=USER_CITIES_MESSAGE, reply_markup=markup)
        elif txt == ADD_ALERT_BUTTON:
            if len(cities) == 0:
                bot.send_message(chat_id, NO_CITIES_MESSAGE)
            else:
                markup = set_inline_markup(cities, 'city_name', ADD_ALERT)
                bot.send_message(chat_id=chat_id, text=USER_CITIES_MESSAGE, reply_markup=markup)
        elif txt == STOP_ALERT_BUTTON:
            alert_cities = get_alert_cities()
            if len(alert_cities) == 0:
                bot.send_message(chat_id, NO_ALERTS_MESSAGE)
            else:
                markup = set_inline_markup(alert_cities, 'city_name', STOP_ALERT, 'time')
                bot.send_message(chat_id=chat_id, text=USER_CITIES_MESSAGE, reply_markup=markup)
        else:
            user_name = message.chat.username
            if user_name == ADMIN[1:]:
                users = get_users_by_attr()
                if txt == GET_USERS:
                    text = "Bot users:\n"
                    for i in range(len(users)):
                        text += f'{i + 1}. {users[i].user_name}\n'
                    bot.send_message(chat_id, text)
                elif txt == BAN_USERS or txt == UNBAN_USERS:
                    val = False if txt == BAN_USERS else True
                    users = get_users_by_attr(User.is_banned, val)
                    no_text = ALL_BANNED_USERS if txt == BAN_USERS else ALL_UNBANNED_MESSAGE
                    if len(users) == 0:
                        bot.send_message(chat_id, no_text)
                    else:
                        flag = BAN if txt == BAN_USERS else UNBAN
                        markup = set_inline_markup(users, 'user_name', flag)
                        bot.send_message(chat_id=chat_id, text=USER_MESSAGE, reply_markup=markup)
                else:
                    bot.send_message(chat_id, UNKNOWN_MESSAGE)
            else:
                bot.send_message(chat_id, UNKNOWN_MESSAGE)
    else:
        bot.send_message(chat_id, USER_BANNED_MESSAGE)

import re
from threading import Thread
from time import sleep

import schedule

from app import bot
from handlers.services.deletion_service import delete_by_callback
from handlers.services.markup_service import set_inline_markup
from handlers.services.weather_service import send_weather
from models import City
from text_literals.callback_prefixes import ADD_ALERT, STOP_ALERT
from text_literals.main_functions_messages import *
from .database_service import user_is_banned


def get_alert_cities():
    cities = list()
    for job in schedule.get_jobs():
        city = City(job.job_func.args[1])
        city.time = job.at_time.strftime('%H:%M')
        cities.append(city)
    return cities


@bot.callback_query_handler(func=lambda call: call.data.startswith(ADD_ALERT))
def set_alert_city(callback):
    message = callback.message
    user_id = callback.from_user.id
    if user_is_banned(message.chat.id, user_id):
        return
    city = callback.data[9:-1]
    bot.send_message(message.chat.id, SET_ALERT_TIME_MESSAGE)
    bot.register_next_step_handler(message, set_alert_time, city)


def set_alert_time(message, city):
    time = message.text
    chat_id = message.chat.id
    if not re.match('^(([0,1][0-9])|(2[0-3])):[0-5][0-9]$', time):
        bot.send_message(chat_id, INVALID_TIME_MESSAGE)
    else:
        for job in schedule.get_jobs():
            if time == job.at_time.strftime('%H:%M') and city == job.job_func.args[1]:
                bot.send_message(chat_id, ALERT_EXISTS_MESSAGE)
                return
        schedule.every().day.at(time).do(send_weather, chat_id, city).tag(f'{city} {time}')
        if len(schedule.get_jobs()) == 1:
            Thread(target=schedule_check).start()
        bot.send_message(chat_id, f'{ALERT_PERIOD} {time} {ALERT_MESSAGE} {city}')


def schedule_check():
    while True:
        sleep(10)
        schedule.run_pending()


@bot.callback_query_handler(func=lambda call: call.data.startswith(STOP_ALERT))
def delete_alert(callback):
    user_id = callback.from_user.id
    if user_is_banned(callback.message.chat.id, user_id):
        return
    text = callback.data[10:]
    job = schedule.get_jobs(callback.data[10:])
    schedule.jobs.remove(job[0])
    cities = get_alert_cities()
    markup = set_inline_markup(cities, 'city_name', STOP_ALERT, 'time')
    delete_by_callback(callback, cities, text, markup, ALERT_DELETED_MESSAGE)

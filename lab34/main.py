from app import telebot
from flask import request
from handlers.commands_handlers import *
from handlers.text_messages_handler import *


@app.route('/', methods=['POST'])
def process():
    if request.headers.get('content_type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        app.logger.info(json_string)
        try:
            chat_id = request.json['message']['chat']['id']
        except KeyError:
            chat_id = request.json['callback_query']['from']['id']
        if not json_string.__contains__('text'):
            bot.send_message(chat_id, UNKNOWN_MESSAGE)
            return 'ok'
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok'
    else:
        return 'error'


if __name__ == '__main__':
    app.run()

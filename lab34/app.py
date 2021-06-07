import telebot
import logging
import threading
import pyowm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration.configurator import Configurator

app = Flask(__name__)

configuration = Configurator.get_configuration('/home/Daniil/Desktop/py_labs2021/lab34/configuration/config.json')
app.config['SQLALCHEMY_DATABASE_URI'] = configuration['connection_string']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

log_config = configuration['logger']
logger = logging.getLogger(__name__)
logging.basicConfig(filename=log_config['file'], level=log_config['level'], format=log_config['format'])

db = SQLAlchemy(app)

bot = telebot.AsyncTeleBot(configuration['token'])
bot.set_webhook(configuration['webhook'])

owm = pyowm.OWM(configuration['api_key'])

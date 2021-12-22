import datetime
import pytz

from file_token import token

import telebot
from telebot import types

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup()
    button = ['/time']
    keyboard.add(*button)
    bot.send_message(message.chat.id,
                     'Hi! Write the command \'/time\' to find out the time in the city you want.',
                     reply_markup=keyboard)


@bot.message_handler(commands=['time'])
def time_command(message):
    keyboard = types.ReplyKeyboardMarkup()
    buttons = ['Moscow', 'Prague', 'Paris', 'London', 'Rome', 'New York', 'Tokyo', 'Shanghai', 'Dubai']
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Choose the city where you want to find out the time.', reply_markup=keyboard)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Moscow":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Europe/Moscow')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Prague":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Europe/Prague')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Paris":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Europe/Paris')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "London":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Europe/London')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Rome":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Europe/Rome')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "New York":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('America/New_York')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Tokyo":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Asia/Tokyo')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Shanghai":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Asia/Shanghai')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)
    if message.text == "Dubai":
        keyboard = types.ReplyKeyboardRemove()
        time = pytz.timezone('Asia/Dubai')
        time = datetime.datetime.now(time).time()
        bot.send_message(message.chat.id, time.strftime('%H:%M:%S'), reply_markup=keyboard)


bot.polling()

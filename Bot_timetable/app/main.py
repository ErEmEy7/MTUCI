import telebot
from telebot import types

import datetime
from prettytable import PrettyTable

import psycopg2

from KEYS import token, db_password

conn = psycopg2.connect(database="timetable_db",
                        user="postgres",
                        password=db_password,
                        host="localhost",
                        port="7900")

cursor = conn.cursor()

bot = telebot.TeleBot(token)

date = datetime.datetime.now()
dt = datetime.date(date.year, date.month, date.day)
wk = dt.isocalendar()[1]
week = ''

if (wk % 2) == 0:
    week = 'нижняя'
else:
    week = 'верхняя'

both_week = 'обе'

sql_this_week = "SELECT day, timetable.time, timetable.subject, full_name FROM timetable.timetable JOIN \
                 timetable.teachers ON timetable.subject = teachers.subject JOIN timetable.literally_timetable ON \
                 timetable.time = literally_timetable.time WHERE week=%s or week=%s \
                 ORDER BY timetable.id"

sql_next_week = "SELECT day, timetable.time, timetable.subject, full_name FROM timetable.timetable JOIN \
                 timetable.teachers ON timetable.subject = teachers.subject JOIN timetable.literally_timetable \
                 ON timetable.time = literally_timetable.time WHERE week!=%s or week=%s\
                 ORDER BY timetable.id"


@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = types.ReplyKeyboardMarkup()
    button = ['Расписание на неделю', 'Расписание на день']
    keyboard.add(*button)
    bot.send_message(message.chat.id,
                     'Здравствуйте, выберетие интересующую вас функцию',
                     reply_markup=keyboard)


@bot.message_handler(content_types='text')
def select(message):
    if message.text == "Расписание на неделю" or message.text == 'Расписание на день':
        message_reply(message)
    if message.text == "Расписание на нынешнюю неделю" or message.text == "Расписание на следующую неделю":
        message_reply_week(message)
    if message.text == "Понедельник" or message.text == "Вторник" or message.text == "Среда" or \
            message.text == "Четверг" or message.text == "Пятница":
        message_reply_day(message)
    if message.text != "Расписание на неделю" and message.text != 'Расписание на день' \
            and message.text != "Расписание на нынешнюю неделю" and message.text != "Расписание на следующую неделю" \
            and message.text != "Понедельник" and message.text != "Вторник" and message.text != "Среда" \
            and message.text != "Четверг" and message.text != "Пятница":
        bot.send_message(message.chat.id,
                         'Извините, я Вас не понял')


def message_reply(message):
    if message.text == "Расписание на неделю":
        keyboard = types.ReplyKeyboardMarkup()
        button = ['Расписание на нынешнюю неделю', 'Расписание на следующую неделю']
        keyboard.add(*button)
        bot.send_message(message.chat.id,
                         'Хорошо, выберите интересующую Вас неделю',
                         reply_markup=keyboard)
    if message.text == 'Расписание на день':
        keyboard = types.ReplyKeyboardMarkup()
        button = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
        keyboard.add(*button)
        bot.send_message(message.chat.id,
                         'Хорошо, выберите интересующий Вас день недели',
                         reply_markup=keyboard)


def message_reply_week(message):
    records = ''
    keyboard = types.ReplyKeyboardRemove()
    if message.text == "Расписание на нынешнюю неделю":
        cursor.execute(sql_this_week, (week, both_week,))
        records = list(cursor.fetchall())
    if message.text == "Расписание на следующую неделю":
        cursor.execute(sql_next_week, (week, both_week,))
        records = list(cursor.fetchall())
    table = PrettyTable()
    table.field_names = ["Время", "Предмет", "Преподаватель"]
    j = 0
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    for i in range(5):
        table.add_row(['', '', ''])
        table.add_row([days[i], '', ''])
        table.add_row(['', '', ''])
        while j < len(records) and records[j][0] == days[i]:
            table.add_row([records[j][1], records[j][2], records[j][3]])
            j += 1
    bot.send_message(message.chat.id,
                     f'<pre>{table}</pre>',
                     parse_mode='HTML',
                     reply_markup=keyboard)


def message_reply_day(message):
    if message.text == 'Понедельник' or message.text == 'Вторник' or message.text == 'Среда' or \
            message.text == 'Четверг' or message.text == 'Пятница':
        keyboard = types.ReplyKeyboardRemove()
        cursor.execute("SELECT timetable.time, timetable.subject, full_name FROM timetable.timetable JOIN "
                       "timetable.teachers ON timetable.subject = teachers.subject JOIN timetable.literally_timetable "
                       "ON timetable.time = literally_timetable.time WHERE day=%s and (week=%s or week=%s) "
                       "ORDER BY literally_timetable.id", (message.text, week, 'обе',))
        records = list(cursor.fetchall())
        table = PrettyTable()
        table.field_names = ["Время", "Предмет", "Преподаватель"]
        for i in range(len(records)):
            table.add_row([records[i][0], records[i][1], records[i][2]])
        bot.send_message(message.chat.id, f'<pre>{table}</pre>', parse_mode='HTML', reply_markup=keyboard)


bot.polling()

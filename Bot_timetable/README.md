# Telegram_timetable_bot lab 6
Task: Create a bot for telegram schedules using the **telebot** library and link a database to it.
The bot should be able to determine the number of the school week and be able to issue a schedule both for the whole week and for a specific day.

The bot's message output is designed using the **PrettyTable** library.

In the file `console.txt` it is prescribed to fill in the database for using the bot.

Libraries used: telebot, datetime, psycopg2, prettytable.

##
To use my code you need to add `KEYS.py` file in `app`. This file should contain the following code:
```python
token = ''
db_password = ''
```
You get a token when creating a bot via BotFather and password when create a database

# Bot_timezoner lab 5
Task: Make a simple telegram bot using the **telebot** library.
The bot must be able to respond to the following commands: `/start` and `/time` and have multiple responses to a specific text

This bot is able to determine the time in some cities
For each city in the telegram there is a separate button, when pressed, the bot gives the exact time in the selected city

Libraries used: telebot, datetime, pytz

##
To use my code you need to add `file_token.py` file in `app`. This file should contain the following code:
```python
token = ''
```
You get a token when creating a bot via BotFather

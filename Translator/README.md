# Translator lab 2
Task: Make a website with a translator function and text-to-voice synthesis.

There is one text entry form on the site.
Two buttons: **Translate text** for translation and **Convert text to speech** for synthesis.
Translation and synthesis is carried out using Microsoft Azure.

Libraries used: flask

##
To use my code you need to add `key.py` file in `app`. This file should contain the following code:
```python
subscription_key = ''
location = ''
```
You should get the subscription key and location from Azure. The key looks like long string of letters and numbers, location can be like `global`.

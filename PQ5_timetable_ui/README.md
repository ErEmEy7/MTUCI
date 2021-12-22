# PQ5_timetable_ui lab 7
Task: Create a timetable application using the PQ5 library and link a database to it.

The application should have 3 tabs: timetable, subjects and teachers

It should be possible to edit the database from the application using the buttons `delete`, `join` (for each row) and `update`, `insert` for the window.

Libraries used: sys, PyQt5, psycopg2, datetime

To use my code you need to add `KEYS.py` file in `app`. This file should contain the following code:
```python
db_password = ''
```
You get a password when create a database

# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app

user = {'username': ' honey <UwU> '}
posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    },
    {
        'author': {'username': 'Василий'},
        'body': 'Привет!!'
    }
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/dict', methods=['post'])
def dict():
    nickname = str(request.form.get("nickname"))
    message = str(request.form.get("message"))

    posts.append({
        'author': {'username': nickname},
        'body': message
    })

    return render_template('index.html', title='Home', user=user, posts=posts)
# commit for prikol

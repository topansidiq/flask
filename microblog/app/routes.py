from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Topan Sidiq"}
    posts = [
        {
            'author': {'username': "Topan"},
            'body': 'Beautiful day in Padang!'
        },
        {
            'author': {'username': "Salsa"},
            'body': 'Nice to meet you!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
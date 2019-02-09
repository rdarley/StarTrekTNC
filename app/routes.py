from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', welcome_msg='Welcome to Star Trek: The Next Conversation')

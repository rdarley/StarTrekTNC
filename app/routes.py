from flask import render_template
from app import app
from app.forms import ContactForm


@app.route('/')
@app.route('/index')
def index():
    welcome_msg = 'Welcome to Star Trek: The Next Conversation'
    return render_template('index.html', title='Home', welcome_msg=welcome_msg)


@app.route('/contact')
def contact():
    return render_template('contact.html',
                           title='Contact Us',
                           form=ContactForm())

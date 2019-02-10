from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ContactForm


@app.route('/')
@app.route('/index')
def index():
    welcome_msg = 'Welcome to Star Trek: The Next Conversation'
    return render_template('index.html', title='Home', welcome_msg=welcome_msg)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Hail sent from {form.first_name.data} {form.last_name.data}')
        return redirect(url_for('index'))
    return render_template('contact.html',
                           title='Contact Us',
                           form=form)

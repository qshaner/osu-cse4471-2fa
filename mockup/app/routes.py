from flask import render_template, session, url_for, flash, redirect, request, session
from app import app
from app.forms import LoginForm
from functools import wraps

import duo_web
import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        if form.password.data == '1234' and form.username.data == 'Miguel':
            session['logged_in'] = True
            return index()
        else:
            flash('Wrong Password!')
            return render_template('login.html', title="signin3", form=form)

    return render_template('login.html', title="signin2", form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    if not session.get('logged_in'):
        form = LoginForm()
        return render_template('login.html', title="Sign in", form=form)
    else:
        user = {'username': 'Miguel', 'password':'1234'}
        posts = [
            {'author': {'username':'John'},
            'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
            }
        ]
        return render_template('index.html',title='Home', user=user, posts=posts)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))

from flask import render_template, flash, redirect, url_for, request
from xplore import app, db, bcrypt
from xplore.forms import RegistrationForm, LoginForm, UpdateAccountForm, PickGenre
from xplore.models import User
from flask_login import login_user, current_user, logout_user, login_required
from xplore.crawler import scraping

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@login_required
@app.route('/dashboard')
def web():
    Gdict = scraping.scrape()
    return render_template('web.html',dict = Gdict,title = 'web')

#User_Registration

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('front'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


#User_Login and Redirect to Login

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('front'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('front'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

"""
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
"""

@app.route("/front")
def front():
    return render_template('front.html', title='Front')


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('account.html', title='Account', form=form)

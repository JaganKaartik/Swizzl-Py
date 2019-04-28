#Import Statements

from flask import render_template, flash, redirect, url_for, request
from xplore import app, db, bcrypt
from xplore.forms import RegistrationForm, LoginForm, UpdateAccountForm
from xplore.models import User
from flask_login import login_user, current_user, logout_user, login_required
from xplore.crawler import scraping


#HomePage or the Root File

@app.route("/")
@app.route("/home")
def home():
    return render_template('pref.html')

#Login Required for the User Choosing Preferences


@login_required
@app.route('/pref')
def prefform():
   return render_template('pref.html')

#View All Feeds

@login_required
@app.route('/feedboard',methods = ['POST', 'GET'])
def feedboard():
    if request.method == 'POST':
        genre = request.form['Genre']
        website = request.form['Website']
    else:
        return redirect(url_for('home'))
    if not request.form['Genre']:
        flash('Please enter Genre')
        return redirect(url_for('home'))
    if(website == 'NY'):
        Gdict = scraping.nyScrape(genre)
    elif(website == 'GL'):
        Gdict = scraping.glScrape(genre)
    elif(website == 'GA'):
        Gdict = scraping.guaScrape(genre)
    else:
        flash('Please enter correct abbrevation')
        return redirect(url_for('home'))
    print(Gdict)
    if Gdict == "Empty":
        flash('No news in the genre, please re-enter genre','danger')
        return redirect (url_for('home'))

    return render_template('feeds.html',dict = Gdict,title = 'feed')

#User_Registration and Redirect to Log in page

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
    return render_template('register.html', title='Register', form = form)


#User_Login and Redirect to Home Page

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('front'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form = form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home'))


@app.route("/feeds")
@login_required
def feeds():
    return render_template('feeds.html', title = 'feed')

"""
@app.route("/front")
def front():
    return render_template('front.html', title='front')
"""

""" User Profile Management """

#Updating account Information

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
    return render_template('account.html', title='Account', form = form)

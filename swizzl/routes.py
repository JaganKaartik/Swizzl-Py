# Import Statements

from flask import render_template, flash, redirect, url_for, request
from swizzl import app, db, bcrypt
from swizzl.forms import RegistrationForm, LoginForm, UpdateAccountForm
from swizzl.models import User, ViewPosts
from flask_login import login_user, current_user, logout_user, login_required
from flask_admin.contrib.sqla import ModelView
from celery import Celery
from swizzl.services import newsfetch as snf


"""
    TESTING BACKEND 
"""
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0' 

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/feeds")
def feeds():
    fetchFeeds.delay()
    return render_template('home.html')

@celery.task()
def fetchFeeds():
    FeedDict = snf.YahooFetch()
    limit = len(FeedDict['title'])
        

    for i in range(0,limit):
        post = ViewPosts(title = FeedDict['title'][i], link = FeedDict['link'][i],linkdata = FeedDict['linktext'][i],tbscore = FeedDict['tbScore'][i],vaderscorePos = FeedDict['vaderScore'][i]['pos'],vaderscoreNeut = FeedDict['vaderScore'][i]['neu'],vaderscoreNeg = FeedDict['vaderScore'][i]['neg'],vaderscoreComp = FeedDict['vaderScore'][i]['compound'],prof = FeedDict['prof'][i],pubDate = FeedDict['pubdate'][i])
        
        db.session.add(post)
        try:
            db.session.commit()
        except:
            db.session.rollback()

"""
    Home Page of Document
    UI: Updated
    Backend: Updated
"""
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


"""
    View All Posts from the Database
    UI: Needs Work
    Backend: Needs Work
"""
@app.route("/viewpost")
@login_required
def viewpost():
    result = ViewPosts.query.all()
    return render_template('viewpost.html',post = result,title = 'viewpost')


"""
    User Registration
    -> Redirects to Log in page
    Explicitly Adding Admin and Users
    UI: Updated
    Backend: Updated
"""
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if(form.username.data == 'Admin'):
            user = User(username=form.username.data, password=hashed_password, roles='Admin')
        else:
            user = User(username=form.username.data, password=hashed_password, roles='User') 
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form = form)


"""
    User Login
    -> Redirects to Home Page (UI: Logged in view)
    UI: Updated
    Backend: Updated
"""

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form = form)

"""
    User Logout
    -> Redirects to Home Page (UI: Logged out view)
    UI: Updated
    Backend: Updated
"""

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home'))


""" 
    User Profile Management 
    Updating Account Information
"""

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



""" 
    Admin Management 
    Creating the Admin Model View

"""

@login_required
@app.route("/admin ")
def admin():
    return render_template('admin.html', title='admin')

class MyModelView(ModelView):
    def is_accessible(self):
        if User.query.filter(current_user.username == 'Admin').first():
            return True
        else:
            return False

            def inaccessible_callback(self,name,**kwargs):
                return redirect(url_for('login'))





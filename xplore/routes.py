#Import Statements

from flask import render_template, flash, redirect, url_for, request
from xplore import app, db, bcrypt
from xplore.forms import RegistrationForm, LoginForm, UpdateAccountForm
from xplore.models import User, Posts
from flask_login import login_user, current_user, logout_user, login_required
from xplore.crawler import scraping
from flask_admin.contrib.sqla import ModelView



#HomePage or the Root File

@app.route("/")
@app.route("/home")
@login_required
def home():
    return render_template('home.html')



#Login Required for the User Choosing Preferences



@login_required
@app.route('/pref')
def prefform():
   return render_template('pref.html')



#View All Feeds (Fix Limit Issues)



@login_required
@app.route('/feedboard',methods = ['POST', 'GET'])
def feedboard():
    if request.method == 'POST':
        genre = request.form['Genre']
        website = request.form['Website']
    else:
        return redirect(url_for('home'))
    if not request.form['Genre']:
        flash('Please enter Genre','danger')
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
    if Gdict == "Empty":
        flash('No news in the genre, please re-enter genre','danger')
        return redirect (url_for('home'))

    limit = len(Gdict['title'])
    
    for i in range(0,limit-1):
        post = Posts(Genre = genre,title = Gdict['title'][i],link = Gdict['link'][i],pubDate = Gdict['pubdate'][i],content = Gdict['description'][i])
        db.session.add(post)
        db.session.commit()
    
    
    return render_template('feeds.html',dict = Gdict,x=limit, title = 'feed')





@app.route("/viewpost")
@login_required
def viewpost():
    result = Posts.query.all()
    return render_template('viewpost.html',post = result,title = 'viewpost')

#User_Registration and Redirect to Log in page


#Explicitly Adding Admin and Users


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


#User_Login and Redirect to Home Page



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


""" User Profile Management """


#Updating Account Information


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


""" Admin Management """



#Creating the Admin Model View


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

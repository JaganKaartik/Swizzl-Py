from flask import render_template, flash, redirect, url_for
from xplore import app
from xplore.forms import RegistrationForm, LoginForm
from xplore.models import User, News

"""
@app.route("/")
def demo():
    return render_template('front_page.html',posts=posts)
"""

#User_Registration

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


#User_Login

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('front_page'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger!')
    return render_template('login.html', title='Login', form=form)

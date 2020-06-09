from urllib import request
from flask import render_template, url_for, flash
from . import auth
from flask_login import login_user, login_required, logout_user
from .forms import RegForm,LoginForm
from ..models import User
from .. import db

from werkzeug.utils import redirect

#User Login
@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('auth/login.html', loginform = form)

#User Logiut
@auth.route('/logout')
 @login_required
    def logout():
        logout_user()
        return redirect(url_for("main.index"))

#User Signup
@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', r_form = form)

from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f'Success creating your account. You are now logged in as: {user_to_create.username}',
            category='success')
        return redirect(url_for('market_page'))  # name of the def for the page
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating the user: {err_msg}',
                  category="danger")
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_connection(
                attempted_password=form.password.data):
            attempted_user.authenticated = True
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',
                  category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password do not match.', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out.", category='info')
    return redirect(url_for("home_page"))


# @app.route('/about')
# def about():
#     return f'<h1>test</h1>'

# @app.route('/about/<username>')
# def custAbout(username):
#     return f'<h1>Hello {username}</h1>'
from flask import Blueprint, render_template, redirect, flash, request, current_app
from .forms import LoginForm, SignUpForm, PasswordChangeForm
from .models import UserMongo
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

auth = Blueprint ('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:

            # Check if email already exists
            existing_user = current_app.db.customers.find_one({"email": email})

            if existing_user:
                flash('Account Not Created!!, Email already exists')
            else:
                new_customer = {
                    "email": email,
                    "username": username,
                    "password": generate_password_hash(password2)
                }

                try:
                    current_app.db.customers.insert_one(new_customer)
                    flash('Account Created Successfully, You can now Login')
                    return redirect('/login')
                except Exception as e:
                    print(e)
                    flash('Something went wrong!')

            # Clear form
            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''

    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        #  MongoDB query
        customer = current_app.db.customers.find_one({"email": email})

        if customer:
            # Check hashed password
            if check_password_hash(customer['password'], password):

                # Wrap MongoDB user for Flask-Login
                user = UserMongo(customer)

                login_user(user)
                return redirect('/')
            else:
                flash('Incorrect Email or Password')
        else:
            flash('Account does not exist please Sign Up')

    return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')


@auth.route('/profile/<int:customer_id>')
@login_required
def profile(customer_id):
    customer = Customer.query.get(customer_id)
    return render_template('profile.html', customer=customer)
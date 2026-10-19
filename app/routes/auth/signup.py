"""Sign-up route (/signup) of the auth blueprint."""

from app.forms import SignUp
from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash
from database import create_user, get_user_by_email
from . import auth

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Show the sign-up form; on valid submit, create the user with a hashed password."""

    form = SignUp()

    if request.method == 'GET':
        # Prefill from ?email=..., set by the redirect in signin()
        form.email.data = request.args.get('email', '')

    if form.validate_on_submit():

        email = form.email.data
        user = get_user_by_email(email)

        # Check-then-insert can race under concurrent requests;
        # the real guarantee must be a UNIQUE constraint on users.email.
        if user:
            flash('Email already registered.', 'error')
            return redirect(url_for('auth.signin'))
            
        else:
            password_hash = generate_password_hash(form.password.data)

            create_user(
                email=email,
                password_hash=password_hash,
                name=form.name.data
            )

            flash('User successfully created!', 'success')
            return redirect(url_for('auth.signin'))

    return render_template('auth/signup.html', form=form)

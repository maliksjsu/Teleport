from chef_browser import app, db
from flask import render_template, redirect, session, request, url_for, flash
from user.form import RegisterForm, LoginForm
from user.models import User
import bcrypt


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    error = None

    if form.validate_on_submit():

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(user)
        db.session.flush()

        if user.id:
            flash("User Created")
            db.session.commit()

        else:
            db.session.rollback()
            error = "Error registering User"

        return redirect('/success')

    return render_template('user/register.html', form=form, error=error)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if session.get('username'):
        username = session.get('username')
        flash('You are already logged in as %s' % username)
        return redirect(url_for('index'))

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()

        if user:

            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = form.username.data
                session['is_author'] = user.is_author

                if 'next' in session:

                    next = session.get('next')
                    session.pop('next')

                    return redirect(next)

                else:

                    return redirect(url_for('index'))
            else:
                error = 'Incorrect Password'
        else:
            error = "Incorrect Username"

    return render_template('user/login.html', form=form, error=error)

@app.route('/index')
def index():
    return render_template('user/index.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))



@app.route('/success')
def success():
    form = RegisterForm()
    flash(form.fullname.data)
    return "Author registered!"


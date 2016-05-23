from functools import wraps
from flask import session, request, redirect, url_for, abort


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#f is the function
#session.get username mean user is logged in
#if not then return to login and append the user current page and after login return it
#to him

def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('is_author') is None:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

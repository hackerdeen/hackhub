from functools import wraps
from flask import session, redirect, abort
from member import Member

def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/hub/login")
    func.func_name = f.func_name
    return func

def admin_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        user = Member(session["username"])
        if user.is_admin():
            return f(*args, **kwargs)
        else:
            return abort(403)
    func.func_name = f.func_name
    return func

        

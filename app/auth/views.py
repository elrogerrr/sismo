from . import auth
from app.forms import LoginForm
from flask import render_template

@auth.route('/login', methods=["GET","POST"])
def login():
    context={
        "login_form":LoginForm()
    }
    return render_template("login.html", **context)
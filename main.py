from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm 

app = create_app()

items=["item1","item2","item3","item4","item5","item6","item7"]

@app.cli.command()
def test():
    tests=unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)

@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session["user_ip"] = user_ip_information
    return response

@app.route('/show_information_address', methods= ["GET","POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username=session.get("username")
    login_form = LoginForm()
    context={
        "user_ip":user_ip,
        "items":items,
        "login_form":login_form,
        "username":username
    }
    if login_form.validate_on_submit():
        username=login_form.username.data
        session["username"] = username
        flash("nombre registrado y correcto")
        return redirect(url_for("index"))
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(host='127.0.0.5', port=8888, debug=True)
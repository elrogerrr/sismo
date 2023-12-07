from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"]='clavesegura=)(/&%$#"!"#$%&/()=0987654321234567890)'

items=["item1","item2","item3","item4","item5","item6","item7"]

class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar contraseña")

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
        return make_response(redirect("/index"))
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(host='127.0.0.5', port=8888, debug=True)
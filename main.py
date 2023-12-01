from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

items=["item1","item2","item3","item4","item5","item6","item7"]

@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip_information",user_ip_information)
    return response

@app.route('/show_information_address')
def show_information():
    user_ip = request.cookies.get("user_ip_information")
    context={
        "user_ip":user_ip,
        "items":items
    }
    return render_template("index.html", **context)

app.run(host='127.0.0.5', port=8888, debug=True)
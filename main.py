from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundirijillo"

app.run(host='0.0.0.0', port=8888)
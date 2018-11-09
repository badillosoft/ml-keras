from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Docker Python :D"

app.run(host="0.0.0.0")
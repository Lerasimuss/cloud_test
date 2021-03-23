from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def index():
    return "Привет от Ким Чен Ына"


if __name__ == '__main__':
    app.run()
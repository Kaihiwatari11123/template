from flask import Flask, render_template
from threading import Thread
import random

app = Flask('')


@app.route("/")
def main():
    return render_template("index.html")


def run():
    app.run(host="0.0.0.0", port=random.randint(5000,8080))


def keep_alive():
    server = Thread(target=run)
    server.start()
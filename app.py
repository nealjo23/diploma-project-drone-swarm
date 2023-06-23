"""
John Neal 20003366
Diploma Advanced Programming
NM TAFE
Semester 1 2023
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    links = {"video": "http://127.0.0.1:5000/video"}
    return render_template("index.html", links=links)


if __name__ == '__main__':
    app.run(port=8000)

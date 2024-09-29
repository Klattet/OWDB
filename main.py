from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.html")

@app.route("/search")
def search(query: str = None):
    return render_template("search.html")

@app.route("/heroes")
def heroes():
    return render_template("heroes.html")
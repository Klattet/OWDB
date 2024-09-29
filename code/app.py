from flask import Flask, render_template

app = Flask(__name__, template_folder = "html")

@app.route("/")
def root():
    return render_template("default.html")
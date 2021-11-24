from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "homepage"

@app.route("/about")
def about():
    return "about page"

@app.route("/admin")
def admin():
    return "admin page"

@app.route("/secret")
def secret():
    return "secret page"


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
import sys
from flask import Flask, render_template, Response, request,redirect

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secret"
IS_LOGIN = False

# --- STATIC PAGES --- #

@app.route("/")
def homepage():
    page_name = "Welcome to homapage!"
    return render_template("index.html", **locals())

@app.route("/about")
def about():
    return "about page"

@app.route("/admin")
def admin():
    return "admin page"

@app.route("/secret")
def secret():
    return "secret page"

# --- LOGIN --- # 

def login_required(func):
    def wrapper(*args, **kwargs):
        print(IS_LOGIN, file = sys.stderr)
        if not IS_LOGIN:
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper

@app.route("/profile")
@login_required
def profile():
    return "profile page"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            global IS_LOGIN
            IS_LOGIN = True
            return redirect("/profile")
        return redirect("/login")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return "HELLO WORLD"

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "GET" and "username" not in request.form and "password" not in request.form:
        message = "You haven't logged in. Complete the fields above."
    elif request.method == "POST" and "username" in request.form and "password" in request.form:
        pairs = {"admin": "admin", "hello": "hello", "andy": "andy"}
        if request.form["username"] in pairs and request.form["password"] == pairs[request.form["username"]]:
            message = "You have successfully logged in!"
        else:
            message = "The username/password could not be found. Please try again."
    else:
        message = "Invalid request. Please try again."

    return render_template("login.html", message=message)

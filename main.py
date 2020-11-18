from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return "HELLO WORLD"

def authenticate(username, password):
    dummy = {"admin": "admin", "hello": "hello", "andy": "andy"}
    message = ""
    if username and password:
        if username in dummy and password == dummy[username]:
            message = "You have successfully logged in!"
        else:
            message = "The username/password could not be found. Please try again."
    else:
        message = "Some fields are missing. Please try again."

    return message

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "GET":
        message = "You haven't logged in. Complete the fields above."
    elif request.method == "POST" and "username" in request.form and "password" in request.form:
       message = authenticate(request.form["username"], request.form["password"])
    else:
        message = "Invalid request. Please try again."

    return render_template("login.html", message=message)

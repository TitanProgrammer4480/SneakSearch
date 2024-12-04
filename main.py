from enum import unique
from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from functions.google import g_search
from functions.duck import duck_search
#from functions.brave import brave_search



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        term = request.form["term"]
        g_box = request.form.get('google', "off")
        d_box = request.form.get('duckduckgo', "off")
        b_box = request.form.get('brave', "off")
        g_result = g_search(term, 10, "us")
        duck_result = duck_search(term, 10, "wt-wt")
        #brave_result = brave_search(term)
        brave_result = {}
        all_results = [{
            "search": "Google",
            "status": g_box,
            "results": g_result
        }, {
            "search": "DuckDuckGo",
            "status": d_box,
            "results": duck_result
        }, {
            "search": "Brave",
            "status": b_box,
            "results": brave_result
        }]
        return render_template("home.html",
                               web_res=all_results,
                               term=term,
                               g_box=g_box)
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form["name"])
        if request.form["name"] == "admin" and request.form[
                "password"] == "admin":
            session["username"] = request.form["name"]
            return redirect(url_for("dashboard"))
        print(hash(request.form["name"].encode()))
        print(request.form["password"])
        print(hash(request.form["password"].encode()))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User(username=hash(request.form["username"].encode()), email=hash(request.form["email"].encode()), password=hash(request.form["password"].encode()))
        db.session.add(user)
        db.session.commit()
        session["username"] = request.form["username"]
        return redirect(url_for("dashboard"))
    return render_template("signup.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if "username" in session:
        print(session["username"])
        print(User.query.all())
        session_user = User.query.filter_by(username=session["username"]).all()
        return render_template("dashboard.html", user=session_user)
    return "you are not logged in"


@app.route("/logout", methods=["GET"])
def logout():
    session.pop('username', None)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

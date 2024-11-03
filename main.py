from flask import Flask, render_template, request

from functions.google import g_search

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        term = request.form["term"]
        result = g_search(term, 10, "us")
        return render_template("home.html", web_res=result)
    return render_template("home.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

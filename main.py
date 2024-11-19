from flask import Flask, render_template, request

from functions.google import g_search
from functions.duck import duck_search
from functions.brave import brave_search

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        term = request.form["term"]
        g_box = request.form.get('google', "off")
        d_box = request.form.get('duckduckgo', "off")
        b_box = request.form.get('brave', "off")
        g_result = g_search(term, 10, "us")
        duck_result = duck_search(term, 10, "wt-wt")
        brave_result = brave_search(term)
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
        return render_template("home.html", web_res=all_results, term=term)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request

from functions.google import g_search
from functions.duck import duck_search

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        term = request.form["term"]
        g_result = g_search(term, 10, "us")
        duck_result = duck_search(term, 10, "wt-wt")
        all_results = []
        all_results.append(
            {
                "search": "Google",
                "results": g_result
            }
        )
        all_results.append(
            {
                "search": "DuckDuckGo",
                "results": duck_result
            }
        )
        return render_template("home.html", web_res=all_results, term=term)
    return render_template("home.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

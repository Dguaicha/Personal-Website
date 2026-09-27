from flask import Flask, render_template
from content.portfolio import PORTFOLIO

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", portfolio=PORTFOLIO)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

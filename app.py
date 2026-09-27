<<<<<<< Updated upstream
from flask import Flask, abort, jsonify, render_template
from database import load_jobs_from_db, load_job_from_db
=======
from flask import Flask, render_template
>>>>>>> Stashed changes
from content.portfolio import PORTFOLIO

app = Flask(__name__)


@app.route("/")
<<<<<<< Updated upstream
def hello_world():
    jobs = load_jobs_from_db()
    return render_template(
        "home.html",
        jobs=jobs,
        portfolio=PORTFOLIO,
    )


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if job is None:
        abort(404)
    return render_template("job.html", job=job)
=======
def home():
    return render_template("home.html", portfolio=PORTFOLIO)
>>>>>>> Stashed changes


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

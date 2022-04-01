from flask import Flask, render_template

from DataController import DataController

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/referrals")
def present_referrals():
    data_controller = DataController()
    jobs_list = data_controller.get_list_of_jobs_from_google_sheets()
    jobs = data_controller.create_job_model_list(jobs_list)
    return render_template('referrals.html', jobs=jobs)

if __name__ == '__main__':
    app.run()



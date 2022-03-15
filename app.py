import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///students.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        # Access form data
        ID = request.form.get("ID")
        quizz_1 = request.form.get("quizz_1")
        midterm_test = request.form.get("midterm_test")
        quizz_2 = request.form.get("quizz_2")
        exam = request.form.get("exam")
        total_score = int(quizz_1) + int(midterm_test) + int(quizz_2) + int(exam)

        # Update data into database
        db.execute("UPDATE students SET quizz_1 = ?, midterm_test = ?, quizz_2 = ?, exam = ?, total_score = ? WHERE id = ?", quizz_1, midterm_test, quizz_2, exam, total_score, ID);

        # Go back to homepage
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        # Query for all students
        students = db.execute("SELECT * FROM students ORDER BY total_score DESC")

        # Query for all score results
        score_result = db.execute("SELECT AVG(total_score) AS average, MAX(total_score) AS maximum, MIN(total_score) AS minimum FROM students")

        # Render students page
        return render_template("index.html", students=students, score_result=score_result)

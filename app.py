from os import listdir
from os.path import isfile, join

from flask import Flask, redirect, render_template, session, url_for

from lib import (
    ComparisonMemory,
    ComparisonMemoryElement,
    NoComparisonAvailableException,
)
from sorts.merge_insertion_sort import merge_insertion_sort

app = Flask(__name__)
# Change the secret key if you use this for anything serious.
app.secret_key = b'&dw2HLe%ISEJQ[\uo}Jwh^`-L@9m?".`iJg8\%8.'

IMAGEPATH = "static/images"


@app.route("/")
def index():
    if "comparisons" in session:
        memory = ComparisonMemory(session["comparisons"])
    else:
        memory = ComparisonMemory([])
        session["comparisons"] = []
        session["comparison_count"] = 0
    images = [
        ComparisonMemoryElement(f, memory)
        for f in listdir(IMAGEPATH)
        if isfile(join(IMAGEPATH, f))
    ]
    try:
        # Throws if there are missing comparisons
        images = merge_insertion_sort(images)
        # No missing comparisons, show result page
        ascending = [i.value for i in images]
        descending = ascending[::-1]
        return render_template(
            "result.html",
            images=descending,
            comparison_count=session.get("comparison_count", 0),
        )
    except NoComparisonAvailableException as e:
        # There was a missing comparison, show selection page
        session["current_comparison"] = (e.lhs, e.rhs)
        return render_template(
            "compare.html",
            left_image=e.lhs,
            right_image=e.rhs,
            comparison_count=session.get("comparison_count", 0),
        )


@app.route("/left")
def left():
    """Left is better than right"""
    if "comparisons" in session:
        lhs, rhs = session["current_comparison"]
        session["comparisons"].append((rhs, lhs))
        session["comparison_count"] += 1
        session.modified = True
    return redirect(url_for("index"))


@app.route("/right")
def right():
    """Right is better than left"""
    if "comparisons" in session:
        lhs, rhs = session["current_comparison"]
        session["comparisons"].append((lhs, rhs))
        session["comparison_count"] += 1
        session.modified = True
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
DATA = Path(__file__).parent / "keam_2025_cutoffs.csv"
df = pd.read_csv(DATA)
df["closing_rank"] = pd.to_numeric(df["closing_rank"], errors="coerce")
df = df.dropna(subset=["closing_rank"])


@app.get("/")
def home():
    return render_template(
        "index.html",
        courses=["All engineering courses"] + sorted(df.course.unique()),
        categories=sorted(df.category.unique()),
        results=None,
        form={"rank": "10000", "category": "SM", "course": "All engineering courses", "college": "", "near": False},
    )


@app.post("/")
def predict():
    form = {
        "rank": request.form.get("rank", "").strip(),
        "category": request.form.get("category", "SM"),
        "course": request.form.get("course", "All engineering courses"),
        "college": request.form.get("college", "").strip(),
        "near": request.form.get("near") == "on",
    }
    try:
        rank = int(form["rank"])
        if rank < 1:
            raise ValueError
    except ValueError:
        return render_template("index.html", courses=["All engineering courses"] + sorted(df.course.unique()), categories=sorted(df.category.unique()), results=[], error="Enter a valid rank greater than zero.", form=form)

    view = df.copy()
    if form["course"] != "All engineering courses":
        view = view[view.course == form["course"]]
    if form["college"]:
        view = view[view.college_name.str.contains(form["college"], case=False, na=False)]
    view = view[view.category == form["category"]].copy()
    view["status"] = view.closing_rank.apply(
        lambda cutoff: "Within 2025 cutoff" if rank <= cutoff else
        ("Close to cutoff" if form["near"] and rank <= cutoff * 1.1 else "Beyond 2025 cutoff")
    )
    results = view[view.status != "Beyond 2025 cutoff"].sort_values(["course", "closing_rank"]).to_dict("records")
    return render_template("index.html", courses=["All engineering courses"] + sorted(df.course.unique()), categories=sorted(df.category.unique()), results=results, form=form)


@app.get("/download")
def download():
    return send_file(DATA, as_attachment=True, download_name="keam_2025_cutoffs.csv", mimetype="text/csv")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from ai_model.analyze import analyze_article

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        score, sources = analyze_article(url)
        result = {"score": score, "sources": sources}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

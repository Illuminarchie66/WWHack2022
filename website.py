from flask import Flask
from flask import Flask, render_template     
from flask import Flask, flash, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/record", methods=["GET", "POST"])
def record():
    file = None
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url) # we need a resubmission, go back
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url) # we need a resubmission, go back

    return render_template("record.html", audio=file)

if __name__ == "__main__":
    app.run()
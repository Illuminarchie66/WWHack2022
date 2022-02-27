from flask import Flask
from flask import Flask, render_template     
from flask import Flask, flash, request, redirect, url_for
import transcriber as transcriber
import QuoteToMovie as quoter
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/record", methods=["GET", "POST"])
def record():
    file = None
    quote="You need to submit a quote first!"
    time="Can't be a time for a quote that doesn't exist :("
    film="Need a quote first!"
    array=[]
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url) # we need a resubmission, go back
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url) # we need a resubmission, go back
        else:
            quote = transcriber.transcribeFile(file)
            array = quoter.QuoteToMovie(quote)
            if len(array)==0:
                film = "Couldn't find a match :("
                time = "D:"
            else: 
                film = array[0][0]
                time = array[0][1]

    return render_template("record.html", quote=quote, film=film, allFilms=array, time=time)

if __name__ == "__main__":
    app.run()
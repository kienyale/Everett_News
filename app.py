from flask import Flask, render_template, request
from scrape import scrape_city_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/city", methods=["POST"])
def city():
    location = request.form["location"]
    data = scrape_city_data(location)
    if data:
        return render_template("city.html", **data)
    else:
        return render_template("error.html", message="City not found.")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/transparency")
def transparency():
    return render_template("transparency.html")

if __name__ == "__main__":
    app.run(debug=True)

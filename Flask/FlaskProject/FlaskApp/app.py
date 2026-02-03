from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    #return "<h1> Hello HOME PAGE ni88as</h1>"

@app.route("/about")
def aboutPage():
    return render_template("about.html")
    #return "<h2>THIS IS AN ABOUT PAGE</h2>"

@app.route("/dashboard/<name>")
def dashboard(name):
    items = ["apple", "orange", "mango", "pear"]
    return render_template("dashboard.html", username=name, data=items)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


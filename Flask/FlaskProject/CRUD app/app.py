from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, instance_relative_config=True)

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.instance_path, "employee.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Model
class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    employee = Employee(name="Denji", email="denji@gmail.com")
    db.session.add(employee)
    db.session.commit()

    employees = Employee.query.all()
    return render_template("index.html", employees=employees)


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import database
import object
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
database.connect()
app.config['UPLOAD_PATH'] = 'static/images'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

@app.route("/")
def homePage():
    headline = "HOME PAGE"
    return render_template("index.html", headline=headline)

@app.route("/view")
def view():
    headline = "VIEW COLLECTION"
    cards = database.viewCards()
    return render_template("view.html", headline=headline, cards=cards)

@app.route("/add")
def add():
    headline = "ADD CARD"
    return render_template("add.html", headline=headline)

@app.route("/added", methods=["POST"])
def added():
    image = request.files['image']
    name = request.form.get("name")
    position = request.form.get("position")
    team = request.form.get("team")
    card = object.Card(image.filename, name, position, team)
    database.addCard(card)
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return render_template("added.html", name=name)

@app.route("/delete")
def delete():
    headline = "DELETE CARD"
    return render_template("delete.html", headline=headline)

@app.route("/removed", methods=["POST"])
def removed():
    name = request.form.get("name")
    database.deleteCard(name)
    return render_template("removed.html", name=name)





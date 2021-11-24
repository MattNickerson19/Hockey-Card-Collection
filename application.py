from flask import Flask, render_template, request, session
import sqlite3
import object
from contextlib import closing
import database

app = Flask(__name__)
database.connect()


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

@app.route("/delete")
def delete():
    headline = "DELETE CARD"
    return render_template("delete.html", headline=headline)





# import random
from faker import Faker
from flask import render_template

# from app import db
from app.main import bp
from app.main.models import Adress


fake = Faker("ru-RU")


@bp.route("/")
def index():
    data = Adress.query.all()
    return render_template("main/index.html", title="index", data=data)

# import random
from faker import Faker
from flask import render_template, request

from app import db
from app.main import bp
from app.main.models import Adress, Resident


fake = Faker("ru-RU")


@bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 20
    data = Adress.query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    pages = data.iter_pages(
        left_edge=2, left_current=2, right_current=5, right_edge=2
    )
    return render_template(
        "main/index.html", title="index", data=data, pages=pages
    )

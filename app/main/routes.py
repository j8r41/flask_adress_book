# import random
from faker import Faker
from flask import render_template, request

from app import db
from app.main import bp
from app.main.models import Adress, Resident
from sqlalchemy import or_

fake = Faker("ru-RU")


@bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 20
    q = request.args.get("search", "")
    data = (
        Adress.query.join(Resident, Resident.id == Adress.id)
        .filter(
            or_(
                Adress.country.like(f"%{q}%"),
                Adress.subject.like(f"%{q}%"),
                Adress.city.like(f"%{q}%"),
                Adress.index.like(f"%{q}%"),
                Adress.street.like(f"%{q}%"),
                Adress.number_building.like(f"%{q}%"),
                Adress.number_flat.like(f"%{q}%"),
                Resident.second_name.like(f"%{q}%"),
                Resident.first_name.like(f"%{q}%"),
                Resident.middle_name.like(f"%{q}%"),
            )
        )
        .paginate(page=page, per_page=per_page, error_out=False)
    )
    pages = data.iter_pages(
        left_edge=2, left_current=2, right_current=5, right_edge=2
    )
    return render_template(
        "main/index.html", title="index", data=data, pages=pages
    )

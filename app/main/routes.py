# import random
# from faker import Faker
from flask import flash, redirect, render_template, request, url_for
from flask_babel import _
from sqlalchemy import or_

from app import db
from app.main import bp
from app.main.forms import CreateAdressForm
from app.main.models import Adress, Resident

# fake = Faker("ru-RU")


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


@bp.route("/create_address", methods=["GET", "POST"])
def create_address():
    form = CreateAdressForm()
    if form.validate_on_submit():
        address = Adress(
            country=form.country.data,
            subject=form.subject.data,
            city=form.city.data,
            index=form.index.data,
            street=form.street.data,
            number_building=form.number_building.data,
            number_flat=form.number_flat.data,
            residents=form.residents.data,
        )
        db.session.add(address)
        db.session.commit()
        flash(_("Успешно! Адрес создан."))
        return redirect(url_for("main.index"))
    return render_template(
        "main/create_address.html",
        title=_("Добавить адрес"),
        form=form,
    )

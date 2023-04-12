from app.main import bp
from flask import render_template
from app.main.models import Adress


@bp.route("/")
def index():
    data = Adress.query.all()
    return render_template("main/index.html", title="index", data=data)

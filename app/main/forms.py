from flask_babel import _
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired

from app.main.models import Resident


class AdressForm(FlaskForm):
    country = StringField(_l("Страна"), validators=[DataRequired()])
    subject = StringField(_l("Регион"), validators=[DataRequired()])
    city = StringField(_l("Город"), validators=[DataRequired()])
    index = IntegerField(_l("Индекс"), validators=[DataRequired()])
    street = StringField(_l("Улица"), validators=[DataRequired()])
    number_building = IntegerField(_l("№ здания"), validators=[DataRequired()])
    number_flat = IntegerField(_l("№ квартиры"), validators=[DataRequired()])
    residents = QuerySelectMultipleField(
        "Житель", query_factory=lambda: Resident.query
    )
    submit = SubmitField(_l("Отправить"))


class ResidentForm(FlaskForm):
    second_name = StringField(_l("Фамилия"), validators=[DataRequired()])
    first_name = StringField(_l("Имя"), validators=[DataRequired()])
    middle_name = StringField(_l("Отчество"))
    submit = SubmitField(_l("Отправить"))
    

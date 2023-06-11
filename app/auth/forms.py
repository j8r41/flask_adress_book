# The MIT License (MIT)
# Copyright (c) 2017 Miguel Grinberg

from flask_babel import _
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from app.auth.models import User


class LoginForm(FlaskForm):
    username = StringField(_l("Логин"), validators=[DataRequired()])
    password = PasswordField(_l("Пароль"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Запомнить"))
    submit = SubmitField(_l("Вход"))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Логин"), validators=[DataRequired()])
    password = PasswordField(_l("Пароль"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Повторите пароль"), validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(_l("Регистрация"))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_("Логин занят. Используйте другой."))

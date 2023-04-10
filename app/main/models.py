from app import db

adressobject_resident = db.Table(
    "adressobject_resident",
    db.Column("adressobject_id", db.Integer, db.ForeignKey("adressobject.id")),
    db.Column("resident_id", db.Integer, db.ForeignKey("resident.id")),
)


class AdressObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64), nullable=False)
    subject = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(64), nullable=False)
    number_building = db.Column(db.Integer, nullable=False)
    number_flat = db.Column(db.Integer, nullable=False)
    residents = db.relationship(
        "Resident",
        secondary=adressobject_resident,
        backref=db.backref("addresses", lazy="dynamic"),
    )


class Resident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    second_name = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=True)
    addresses = db.relationship(
        "AdressObject",
        secondary=adressobject_resident,
        backref=db.backref("residents", lazy="dynamic"),
    )

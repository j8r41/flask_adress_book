import random

from faker import Faker
from flask_sqlalchemy import SQLAlchemy

from app.main.models import Adress

fake = Faker("ru-RU")
db = SQLAlchemy()


if __name__ == "__main__":
    for _ in range(10):
        country = "Россия"
        subject = "Test subject"
        city = fake.city()
        index = fake.postcode()
        street = fake.street_name()
        number_building = fake.building_number()
        number_flat = random.randint(1, 100)
        ad_object = Adress(
            country=country,
            subject=subject,
            city=city,
            index=index,
            street=street,
            number_building=number_building,
            number_flat=number_flat,
        )
        db.session.add(ad_object)
        db.session.commit()

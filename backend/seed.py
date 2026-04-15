from app import app
from models import db, User, Workout
from faker import Faker
import random

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="testuser")
    user.set_password("password")

    db.session.add(user)
    db.session.commit()

    for _ in range(10):
        workout = Workout(
            exercise=fake.word(),
            duration=random.randint(10, 60),
            calories=random.randint(50, 500),
            user_id=user.id
        )
        db.session.add(workout)

    db.session.commit()
    print("Seeded!")
from flask import Blueprint, request, session
from models import db, Workout
from schemas import workout_schema, workouts_schema

workouts_bp = Blueprint("workouts", __name__, url_prefix="/workouts")


def authorized():
    return "user_id" in session


# GET (paginated)
@workouts_bp.route("", methods=["GET"])
def get_workouts():
    if not authorized():
        return {"error": "Unauthorized"}, 401

    user_id = session["user_id"]

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    pagination = Workout.query.filter_by(user_id=user_id)\
        .paginate(page=page, per_page=per_page, error_out=False)

    return {
        "data": workouts_schema.dump(pagination.items),
        "page": page,
        "total_pages": pagination.pages
    }


# CREATE
@workouts_bp.route("", methods=["POST"])
def create_workout():
    if not authorized():
        return {"error": "Unauthorized"}, 401

    data = request.get_json()

    workout = Workout(
        exercise=data["exercise"],
        duration=data.get("duration"),
        calories=data.get("calories"),
        user_id=session["user_id"]
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


# UPDATE
@workouts_bp.route("/<int:id>", methods=["PATCH"])
def update_workout(id):
    if not authorized():
        return {"error": "Unauthorized"}, 401

    workout = Workout.query.get_or_404(id)

    if workout.user_id != session["user_id"]:
        return {"error": "Forbidden"}, 403

    data = request.get_json()

    workout.exercise = data.get("exercise", workout.exercise)
    workout.duration = data.get("duration", workout.duration)
    workout.calories = data.get("calories", workout.calories)

    db.session.commit()

    return workout_schema.dump(workout)


# DELETE
@workouts_bp.route("/<int:id>", methods=["DELETE"])
def delete_workout(id):
    if not authorized():
        return {"error": "Unauthorized"}, 401

    workout = Workout.query.get_or_404(id)

    if workout.user_id != session["user_id"]:
        return {"error": "Forbidden"}, 403

    db.session.delete(workout)
    db.session.commit()

    return {}, 204
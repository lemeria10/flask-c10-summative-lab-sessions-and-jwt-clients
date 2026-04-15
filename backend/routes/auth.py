from flask import Blueprint, request, session, jsonify
from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if User.query.filter_by(username=data["username"]).first():
        return {"error": "Username already exists"}, 422

    user = User(username=data["username"])
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id

    return {"id": user.id, "username": user.username}, 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if user and user.check_password(data["password"]):
        session["user_id"] = user.id
        return {"id": user.id, "username": user.username}

    return {"error": "Invalid credentials"}, 401


@auth_bp.route("/logout", methods=["DELETE"])
def logout():
    session.clear()
    return {}, 204


@auth_bp.route("/check_session", methods=["GET"])
def check_session():
    user_id = session.get("user_id")

    if not user_id:
        return {"error": "Unauthorized"}, 401

    user = User.query.get(user_id)
    return {"id": user.id, "username": user.username}
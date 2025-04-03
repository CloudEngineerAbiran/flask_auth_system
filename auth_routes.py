from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User

auth_routes = Blueprint("auth_routes", __name__)

# ✅ User Registration Route
@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    hashed_password = generate_password_hash(data["password"])
    new_user = User(username=data["username"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# ✅ User Login Route
@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if user and check_password_hash(user.password, data["password"]):
        access_token = create_access_token(identity=user.username)
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Invalid username or password"}), 401

# ✅ Protected Route (Requires Authentication)
@auth_routes.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}! This is a protected route."}), 200


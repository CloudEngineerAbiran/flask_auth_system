from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    jwt = JWTManager(app)

    from auth_routes import auth_routes
    app.register_blueprint(auth_routes)

    with app.app_context():
        db.create_all()

    # ✅ Add a default home route to prevent 404 error
    @app.route("/")
    def home():
        return "Welcome to the Flask Authentication System!", 200

    return app

if __name__ == "__main__":
    app = create_app()
    print("🚀 Flask Auth System is running on http://0.0.0.0:5000")
    app.run(host="0.0.0.0", debug=True)


from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Increased length for hashed passwords
    role = db.Column(db.String(50), default="user")  # Can be 'admin' or 'user'
    mfa_enabled = db.Column(db.Boolean, default=False)  # Multi-Factor Authentication flag

    def __repr__(self):
        return f"<User {self.username}>"


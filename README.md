# Flask Authentication System

## Project Overview
The Flask Authentication System is a lightweight authentication service built using Flask. It provides user registration, login with JWT authentication, and role-based access control.

## Folder Structure
```
flask_auth_system/
│── app.py
│── config.py
│── requirements.txt
│── models.py
│── auth_routes.py
│── instance/
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/flask_auth_system.git
cd flask_auth_system
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

## Configuration
Modify `config.py` to update settings:
```python
import os

class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt_secret_key"
```

## API Endpoints

### 1. Register a User
**Endpoint:** `POST /register`
**Request Body:**
```json
{
  "username": "user1",
  "email": "user1@example.com",
  "password": "securepassword"
}
```

### 2. Login User
**Endpoint:** `POST /login`
**Request Body:**
```json
{
  "username": "user1",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "access_token": "JWT_TOKEN"
}
```

### 3. Protected Route
**Endpoint:** `GET /protected`
**Headers:**
```sh
Authorization: Bearer JWT_TOKEN
```

## Models
```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), default="user")
    mfa_enabled = db.Column(db.Boolean, default=False)
```

## How to Push to GitHub

### 1. Initialize Git and Add Files
```sh
git init
git add .
git commit -m "Initial commit"
```

### 2. Create GitHub Repository
- Go to [GitHub](https://github.com/)
- Create a new repository named `flask_auth_system`
- Copy the repository URL

### 3. Push to GitHub
```sh
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

## Conclusion
This Flask Authentication System provides a simple user authentication mechanism with JWT. It can be extended with additional features such as OAuth authentication, MFA, and database migrations.

## How It Works
1. A user registers using the `/register` endpoint.
2. The user logs in via the `/login` endpoint and receives a JWT token.
3. The token is used to access protected routes like `/protected`.
4. Role-based access control ensures users can only access allowed features.

This system is useful for any web application requiring authentication and can be expanded for additional security measures.

Enjoy coding! 🚀



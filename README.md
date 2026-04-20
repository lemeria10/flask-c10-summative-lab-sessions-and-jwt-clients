📘 Flask Sessions & JWT Authentication Lab

This project demonstrates how to build a secure Flask backend API that supports both:

🔐 Session-based authentication
🪪 JWT (JSON Web Token) authentication

It is designed to integrate with a frontend client and provides a full authentication flow including login, logout, and protected routes.

🚀 Features
User registration and login
Session-based authentication using Flask sessions
Token-based authentication using JWT
Protected routes (require authentication)
Logout functionality (session + JWT)
RESTful API design
Ready for frontend integration
🛠️ Tech Stack
Python 3
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Bcrypt
Flask-RESTful
Marshmallow
JWT (JSON Web Tokens)

👉 JWT is a secure, compact way to transmit user identity data between client and server

📁 Project Structure
server/
│
├── app.py              # App entry point
├── config.py           # Configuration settings
├── models.py           # Database models
├── schemas.py      
├── routes/
│   ├── auth.py         # Authentication routes
│   └── workouts.py    # Protected resources
├── migrations/         # Database migrations
└── seed.py             # Seed data
⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/lemeria10/flask-c10-summative-lab-sessions-and-jwt-clients.git
cd flask-c10-summative-lab-sessions-and-jwt-clients
2. Install Dependencies

Using pipenv:

pipenv install
pipenv shell

Or pip:

pip install -r requirements.txt
3. Set Environment Variables

Create a .env file:

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
4. Initialize Database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Seed Database
python seed.py
6. Run Server
flask run

Server runs at:

http://127.0.0.1:5000
🔑 Authentication Flow
✅ Session-Based Auth
Login stores user in session
Session cookie sent automatically
Server verifies session on each request
✅ JWT-Based Auth
Login returns a token
Client stores token (localStorage/cookies)
Token sent in headers:
Authorization: Bearer <token>
Server verifies token for protected routes

👉 JWT is stateless, meaning the server doesn’t store session data

📡 API Endpoints
🔐 Auth Routes
Method	Endpoint	Description
POST	/signup	Register user
POST	/login	Login user
DELETE	/logout	Logout user
GET	/check_session	Check session
📦 Protected Routes
Method	Endpoint	Description
GET	/resource	Protected resource data
🧪 Testing

Use:

Postman
Thunder Client
curl

Example:

curl http://127.0.0.1:5000/check_session
🧠 Learning Objectives
Understand session vs JWT authentication
Build secure Flask APIs
Protect routes with authentication
Integrate backend with frontend clients
Manage user authentication state
⚖️ Sessions vs JWT
Feature	Sessions	JWT
Storage	Server-side	Client-side
Scalability	Limited	High
Stateless	❌ No	✅ Yes
Security	Cookie-based	Token-based
📌 Notes
Sessions are easier for browser-based apps
JWT is better for APIs and mobile apps
Always secure secrets in .env
Use HTTPS in production
👤 Author

Nick Lemeria

📜 License

This project is for educational purposes.

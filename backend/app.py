from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from models import db, bcrypt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

# CRITICAL for session auth with React frontend
CORS(app, supports_credentials=True)
@app.route("/")
def home():
    return {"message": "API is running"}
# Register routes
from routes.auth import auth_bp
from routes.workouts import workouts_bp

app.register_blueprint(auth_bp)
app.register_blueprint(workouts_bp)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
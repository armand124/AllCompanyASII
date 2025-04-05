from flask import Flask
from routes.post_routes import posts_routes
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(posts_routes)

    app.config.from_object(Config)
    db.init_app(app)

    return app
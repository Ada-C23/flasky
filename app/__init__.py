from flask import Flask
from flask_cors import CORS
from .db import db, migrate
from .routes.cat_routes import bp as cats_bp
from .routes.caretaker_routes import bp as caretakers_bp
from .models import cat, caretaker
import os

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cats_bp)
    app.register_blueprint(caretakers_bp)

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.logging import create_logger
import logging
from app.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up logging
    LOG = create_logger(app)
    LOG.setLevel(logging.INFO)

    # Import and register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
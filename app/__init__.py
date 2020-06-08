from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    # Create app configurations
    app.config.from_object(Config)

    # Registering blueprints
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint,url_prefix = '/authenticate')
    app.register_blueprint(main_blueprint)

    db.init_app(app)

    return app

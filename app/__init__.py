from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.load_view = 'auth.login'

app = Flask(__name__)


def create_app():
    # Create app configurations
    app.config.from_object(Config)

    # Registering blueprints
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint,url_prefix = '/authenticate')
    app.register_blueprint(main_blueprint)

    # Initialise Flask Extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    return app

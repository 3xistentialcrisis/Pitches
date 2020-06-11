from flask import Flask
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet,configure_uploads

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.load_view = 'auth.login'
photos = UploadSet('photos', IMAGES)

app = Flask(__name__)


def create_app(config_name):
    # Create app configurations
    app.config.from_object(config_options[config_name])

    # Registering blueprints
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(authentication_blueprint,url_prefix = '/authenticate')
    app.register_blueprint(main_blueprint)

    # Initialise Flask Extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    configure_uploads(app, photos)
    mail.init_app(app)

    return app

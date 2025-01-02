from flask import Flask
from flask_login import LoginManager
from .config import Config

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .chat import bp as chat_bp
    app.register_blueprint(chat_bp)

    return app
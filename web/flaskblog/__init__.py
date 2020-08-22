from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

from flask_mail import Mail
from flaskblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
mail.init_app(app)


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker="redis://redis:6379/0",
        backend="redis://redis:6379/1",
        include=["flaskblog.users.utils"],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery_app = make_celery(app)


def create_app():
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1344dfa0b97b2fdbf50f85d7'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .dbmodels import setgame, User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.join_page'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

def create_database(app):
    if not path.exists('/golf/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


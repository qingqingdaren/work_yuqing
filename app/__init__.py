from flask import Flask
from flask_sqlalchemy import SQLAlchemy,Pagination

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@127.0.0.1:3306/cucnews'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


    db.init_app(app)
    from .news import news as news_blueprint
    app.register_blueprint(news_blueprint)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy,Pagination

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhaoqing:123456@rm-2zeevewh0670zu318.mysql.rds.aliyuncs.com:3306/cucnews'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhaoqing:123456@localhost:3306/cucnews'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


    db.init_app(app)
    from .manwei import news as news_blueprint
    app.register_blueprint(news_blueprint)

    return app

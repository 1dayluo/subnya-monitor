from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from celery import Celery
from .config import read_config, init_db
from .controller.api import api


def create_app():
    app = Flask(__name__)
    config_json = read_config()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://{}'.format(config_json['sqlite']['db_1'])
    
    # 注册路由
    app.register_blueprint(api)
    app.secret_key = b'_5#y2L"F4a@@Q8z\n\xec]/'
    celery = Celery(app.name, broker='redis://localhost:6379/1', backend='redis://localhost:6379/2')
    init_db(app)
    CORS(app)
    # db = SQLAlchemy(app)
    return app


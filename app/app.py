from flask import Flask
import os
from flask_cors import CORS
from app.celery import Celery
from .config import read_config
from .models import db
from .controller.api import api
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env() #environment variables are then accessible throughout the application 
    config_json = read_config()
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(config_json['sqlite']['db_1'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # 注册路由
    app.register_blueprint(api)
    app.secret_key = os.getenv('APP_SECRET')
    CORS(app)
    # celery = make_celery(app)
    return app


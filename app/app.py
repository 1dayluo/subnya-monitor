from flask import Flask
import os
from flask_cors import CORS
from app.celery import celery_init_app
from .config import read_config
from .models import db
from .controller.api import api
from dotenv import load_dotenv



load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env() #environment variables are then accessible throughout the application 
    custom_config = read_config()
    app.config.update(custom_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(custom_config['sqlite']['db_1'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['broker_connection_retry_on_startup'] = True
    app.config['task_file'] = 'monitor.txt'
    app.config['DEBUG'] = True
    app.config['broker_connection_retry_on_startup'] = True
    db.init_app(app)
    app.config.from_mapping(
    CELERY=dict(
        broker_url=custom_config.get('celery_broker'),
        result_backend=custom_config.get('celery_backend'),
        task_ignore_result=True,
    ),
    )
    celery_init_app(app)
    # 注册路由
    app.register_blueprint(api)
    app.secret_key = os.getenv('APP_SECRET')
    CORS(app)
    # celery = make_celery(app)
    return app


# celery.py
from app.celery import Celery
from flask import Flask
from app.config import read_config

def make_celery(app: Flask) -> Celery:
    # 从 Flask 应用配置读取 Celery 配置
    config = read_config()  # 如果你是从配置文件中读取配置
    broker_url = config.get('celery_broker')
    backend_url = config.get('celery_backend')
    
    # 实例化 Celery
    celery = Celery(
        app.import_name,
        broker=broker_url,
        backend=backend_url
    )
    
    # 更新 Celery 的配置
    celery.conf.update(app.config)
    
    # 让 Celery 任务运行在 Flask 应用上下文中
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    
    return celery


# celery.py
from celery import Celery, Task
from flask import Flask,current_app
from app.config import read_config

# def make_celery(app: Flask) -> Celery:
#     # 从 Flask 应用配置读取 Celery 配置
#     config = read_config()  # 如果你是从配置文件中读取配置
#     broker_url = config.get('celery_broker')
#     backend_url = config.get('celery_backend')
#     # print(broker_url)
#     # 实例化 Celery
#     celery = Celery(
#         app.import_name,
#         broker=broker_url,
#         # backend=backend_url
#     )
#     celery_app = Celery(app.name, task_cls=FlaskTask, )
#     celery_app.config_from_object(app.config["CELERY"])
#     # 更新 Celery 的配置
#     celery.conf.update(app.config)
#     celery.set_default()
#     # print(celery.conf)
#     # 让 Celery 任务运行在 Flask 应用上下文中
#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)
#     app.extensions["celery"] = celery
#     celery.Task = ContextTask
#     return celery


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
from app.app import create_app
from app.celery import celery_init_app
from gunicorn.app import wsgiapp

app = create_app()


celery_app = app.extensions['celery']

if __name__ == '__main__':
    wsgiapp.run()
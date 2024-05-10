from app.app import create_app
from app.celery import make_celery

app = create_app()
celery = make_celery(app)

if __name__ == '__main__':
    app.run()
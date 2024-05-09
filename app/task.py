import sqlite3
from celery import Celery

@Celery.task
def get_db_connection(db_name):
    """
        获取db链接
    """
    db = sqlite3.connect(db_name)
    conn = db.cursor()# This is optional: it allows accessing columns by name
    return conn
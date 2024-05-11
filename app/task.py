import sqlite3
import os
from flask import current_app, jsonify
from celery import shared_task



@shared_task(ignore_result=False) 
def get_added_list() -> dict :
    # print(celery.conf)
    task_file = current_app.config.get('monitor').get('dir')[0]
    results = []
    if os.path.exists(task_file):
        with open(task_file+'/'+current_app.config.get('task_file'), 'r+') as f:
            results = [i.strip('\n') for i in f.readlines()]
    return {"message":"ok","domains": results}


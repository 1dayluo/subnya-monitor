import sqlite3
import os
from flask import current_app, jsonify
from celery import shared_task
from .models import Domains
import datetime


@shared_task(ignore_result=False) 
def get_added_list() -> dict :
    # print(celery.conf)
    task_file = current_app.config.get('monitor').get('dir')[0]
    results = []
    db_data = {}
    task = []
    subdomain,datetimes = [],[]
    if os.path.exists(task_file):
        with open(task_file+'/'+current_app.config.get('task_file'), 'r+') as f:
             task = [i.strip('\n') for i in f.readlines()]
    # print(results)
    domains_info = list(Domains.query.filter(Domains.domain.in_(task)))
    for domain in domains_info:
        subdomain =(domain.subdomain, domain.updatetime.strftime("%m/%d/%Y, %H:%M:%S"))
        datetimes.append(domain.updatetime)
        db_data[domain.domain] = {
            'detail': subdomain 
        }
    for domain in task:
        if domain not in db_data.keys():
            results.append({'status': 'off', 
                            'domain': domain, 
                            'subdomain_num': 0,
                            'last': ''})
        else:
            results.append({'status': 'on', 'domain': domain,
                             'subdomain_num': len(db_data[domain].get('detail')),
                             'last':max(datetimes, key=lambda x: x)})
    return {"message":"ok","domains": results}



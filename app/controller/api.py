from flask import Blueprint, request, jsonify, current_app
from ..models import Domains
from collections import defaultdict
from ..task import get_added_list
import datetime
import os

# 待重写

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/read_config')
def read_config():
    if current_app.config.get('DEFAULT_PATH'):
        if os.path.exists(current_app.config.get('DEFAULT_PATH')):
            return jsonify({
                'config_path': current_app.config.get('DEFAULT_PATH'),
                'read_path': current_app.config.get('monitor').get('settings').get('outdir') + 'monitor.txt',
                'subnya_log': current_app.config.get('monitor').get('settings').get('logdir')
                })
        else:
            return jsonify({})
    else:
        return jsonify({})
    # domains = Domains.query.all()
    # print(domains[0].domain)
@api.route('/set-config-path', methods=['POST'])
def set_config_path():
    path = request.get_json['path']
    current_app.config.update(read_config(path))
    return jsonify({
            'config_path': current_app.config.get('DEFAULT_PATH'),
            'read_path': current_app.config.get('monitor')('settings')('outdir') + 'monitor.txt',
            'subnya_log': current_app.config.get('monitor')('settings')('logdir')
            })

@api.route('/get_dbmonitored')
def get_dbmonitor_list():
    domains = Domains.query.all()
    results = defaultdict(dict)
    for domain in domains:
        
        subdomain_info = {}
        # if not results.get('domain.domain'):
        #     results[domain.domain]  = {}
        subdomain_info[domain.subdomain] = {
            'updatetime' : domain.updatetime,
            'checkedtime': domain.checkedtime,
            'ifon' : domain.ifon,
            'status' : domain.status 
        }
            
   
        results[domain.domain].update(subdomain_info)

    return jsonify({"message":"ok","domains": results})

@api.route('/get_monitored')
def get_tasks():
    get_added_list()
    result =  get_added_list.delay()
    return result.get()





@api.route('/api/run_today_status')
def get_today():
    """
        今日是否跑过脚本
    """
    global output_dir
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    if today in os.listdir(output_dir):
        return jsonify({"messgae":"ok", "result": True})
    else:
        return jsonify({"messgae":"ok", "result": False})
    


@api.route('/api/add_monitor', methods=['POST'])
def add_monitor():
    """
        增加监控
    """
    domain = request.get_json()['domain']
    with open(os.path.join(config_json['monitor']['dir'][0],'monitor.txt'), 'r+') as f:
        source_domains = [i.strip('\n') for i in f.readlines()]
    print(source_domains)
    if domain not in source_domains:
        with open(os.path.join(config_json['monitor']['dir'][0],'monitor.txt'), 'a+') as f2:
            f2.writelines(domain+"\n")
    # os.system('subnya -r')
        return jsonify({"messgae":"ok", "result": True})
    return jsonify({"messgae":"ok", "result": False})


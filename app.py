from flask import Flask, redirect, url_for, render_template, \
    request, jsonify, flash, session, Response
from celery import Celery
import os
import pathlib
import datetime
import sqlite3
import json
from flask_cors import CORSa
import yaml
import datetime, time
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 初始化配置
config_json = read_config()
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite://{config_json['sqlite']['db_1']}'
db.init_app(app)
# CORS设置
CORS(app)
# Celery
celery = Celery(app.name, broker='redis://localhost:6379/1', backend='redis://localhost:6379/2')
app.secret_key = b'_5#y2L"F4a@@Q8z\n\xec]/'
base_config_path = str(pathlib.Path.home())+'/.config/subnya'
log_file = base_config_path + '/log/monitor_run.log'
output_dir = ''
sql_path = ''
target_dir = ''

def read_config():
    """
     读取subnya的配置文件
    """
    
    os.environ['DEFAULT_PATH']=base_config_path+'/'+'config.yml'
    if os.path.exists(os.environ['DEFAULT_PATH']):
        with open(os.environ['DEFAULT_PATH'], 'r') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        print(result['monitor']['dir'][0])
        result['monitor']['settings']['outdir'] = output_dir =  base_config_path+result['monitor']['settings']['outdir'][1:] if result['monitor']['settings']['outdir'][0] == '.' else result['monitor']['settings']['outdir']
        result['sqlite']['db_1'] = sql_path =   base_config_path+result['sqlite']['db_1'][1:] if result['sqlite']['db_1'][0] == "." else result['sqlite']['db_1']
        result['monitor']['settings']['logdir'] = log_file = base_config_path+result['monitor']['settings']['logdir'][1:] if result['monitor']['settings']['logdir'][0] == '.' else result['monitor']['settings']['logdir']
        result['monitor']['dir'][0] = target_dir =   base_config_path+result['monitor']['dir'][0][1:] if result['monitor']['dir'][0][0] == '.'  else result['monitor']['dir'][0]

        return result
        # return json.dumps(result)
        # return result['monitor']['dir'][0]
    else:
        return


@celery.task
def get_db_connection():
    """
        获取db链接
    """
    db = sqlite3.connect(config_json['sqlite']['db_1'])
    conn = db.cursor()# This is optional: it allows accessing columns by name
    return conn

@app.route('/api/read_config')
def read_config():
    """
     读取subnya的配置文件
    """
    return config_json

@app.route('/api/set-config-path', methods=['POST'])
def set_config():
    """
      设置subnya的配置路径
    """
    data = request.json  # 获取 JSON 数据
    print(data)
    default_path = data.get('path')
    if default_path.split('.')[-1]== 'yml':
        os.environ['DEFAULT_PATH'] = default_path
        if os.path.exists(os.environ['DEFAULT_PATH']):
            return jsonify({"message": "Config path updated", "path": default_path}), 200
        else:
            return jsonify({"error": "No path specified"}), 400

    else:
        return jsonify({"error": "No path specified"}), 400


@app.route('/api/get_monitored')
def get_monitor_list():
    results = []
    if os.path.exists(os.path.join(config_json['monitor']['dir'][0],'monitor.txt')):
        with open(os.path.join(config_json['monitor']['dir'][0],'monitor.txt'), 'r+') as f:
            results = [i.strip('\n') for i in f.readlines()]
    return jsonify({"message":"ok","domains": results})

@app.route('/api/get_dbmonitored')
def get_dbmonitor_list():
    conn = get_db_connection()
    results = [ result[0] for result in  conn.execute('SELECT DISTINCT domain FROM domains')]
    return jsonify({"message":"ok","domains": results})

@app.route('/api/run_today_status')
def get_today():
    """
        今日是否跑过脚本
    """
    global output_dir
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    if today in os.listdir(output_dir):
        return jsonify({"messgae":"ok", "result": true})
    else:
        return jsonify({"messgae":"ok", "result": false})
    


@app.route('/api/add_monitor', methods=['POST'])
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


@app.route('/')
def home():
    global conn
    if len(output_dir) == 0 or len(sql_path) == 0:
        flash('Path not exists!please set base path ')
        return redirect(url_for('setenv'))    
    else:
        if os.path.exists(output_dir) and os.path.exists(sql_path):
            # read log file
            all_files = os.listdir(output_dir)
            conn = get_db_connection.delay()
            results = [ result[0] for result in  conn.result.execute('SELECT DISTINCT domain FROM domains')]
            return render_template('home.html', log_files=all_files, monitored=results)
        else:
            flash('Please set correct path!')
            return redirect(url_for('setenv'))
    return render_template('home.html')

@app.route('/setting', methods=['GET','POST'])
def setenv():
    global output_dir, sql_path, base_config_path
    if request.method == 'POST':
        output_dir = request.form['output_dir']
        sql_path = request.form['sql_path']
        return redirect(url_for('home'))
    
    return render_template('setting.html', output_dir=base_config_path+'/output', \
                           sql_path=base_config_path+'/db/monitor.db')



@app.route('/outfile/<filename>')
def outfile(filename=''):
    global output_dir
    with open(output_dir + '/' + filename, 'r') as f:
         content = f.read()
    return render_template('show_text.html', text_content=content)

@app.route('/logs')
def log():
    with open(log_file, 'r') as f:
        content = f.read()

    return render_template('show_text.html', text_content=content)

@app.route('/today')
def today():
    global conn, cursor
    today = datetime.date.today()
    conn = get_db_connection()
    conn.execute('SELECT * FROM added_domains WHERE date(updatetime) = ?', (today, ))
    rows = conn.fetchall()
    domain_info = {}
    for row in rows:
        if not domain_info.get(row[0]):
            domain_info[row[0]] = {}
        conn.execute('SELECT IFON, STATUS FROM domains WHERE subdomain = ?', (row[1],))
        sub_row = conn.fetchone()
        domain_info[row[0]][row[1]] = {
            'IFON': sub_row[0],
            'STATUS': sub_row[1]
        }
    

    # return json.dumps(domain_info)
    return render_template('today_task.html', domains=domain_info )


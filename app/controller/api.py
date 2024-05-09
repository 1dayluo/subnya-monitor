from flask import Blueprint
import os

# 待重写

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def read_config():
    """
     读取subnya的配置文件
    """
    return 'ok'

@api.route('/set-config-path', methods=['POST'])
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


@api.route('/get_monitored')
def get_monitor_list():
    results = []
    if os.path.exists(os.path.join(config_json['monitor']['dir'][0],'monitor.txt')):
        with open(os.path.join(config_json['monitor']['dir'][0],'monitor.txt'), 'r+') as f:
            results = [i.strip('\n') for i in f.readlines()]
    return jsonify({"message":"ok","domains": results})

@api.route('/api/get_dbmonitored')
def get_dbmonitor_list():
    conn = get_db_connection()
    results = [ result[0] for result in  conn.execute('SELECT DISTINCT domain FROM domains')]
    return jsonify({"message":"ok","domains": results})

@api.route('/api/run_today_status')
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


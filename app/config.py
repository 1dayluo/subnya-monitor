from flask_sqlalchemy import SQLAlchemy
import yaml 
import json
import pathlib
import os


base_config_path = str(pathlib.Path.home())+'/.config/subnya'
log_file = base_config_path + '/log/monitor_run.log'
output_dir = ''
sql_path = ''
target_dir = ''
base_config_path = str(pathlib.Path.home())+'/.config/subnya'


def read_config():
    """
     读取subnya的配置文件
    """
    
    os.environ['DEFAULT_PATH']=base_config_path+'/'+'config.yml'
    if os.path.exists(os.environ['DEFAULT_PATH']):
        with open(os.environ['DEFAULT_PATH'], 'r') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        result['monitor']['settings']['outdir'] = output_dir =  base_config_path+result['monitor']['settings']['outdir'][1:] if result['monitor']['settings']['outdir'][0] == '.' else result['monitor']['settings']['outdir']
        result['sqlite']['db_1'] = sql_path =   base_config_path+result['sqlite']['db_1'][1:] if result['sqlite']['db_1'][0] == "." else result['sqlite']['db_1']
        result['monitor']['settings']['logdir'] = log_file = base_config_path+result['monitor']['settings']['logdir'][1:] if result['monitor']['settings']['logdir'][0] == '.' else result['monitor']['settings']['logdir']
        result['monitor']['dir'][0] = target_dir =   base_config_path+result['monitor']['dir'][0][1:] if result['monitor']['dir'][0][0] == '.'  else result['monitor']['dir'][0]
        result['celery_broker'] = 'redis://localhost:6379/1'
        result['celery_backend'] =  'redis://localhost:6379/2'
        return result
        # return json.dumps(result)
        # return result['monitor']['dir'][0]
    else:
        return


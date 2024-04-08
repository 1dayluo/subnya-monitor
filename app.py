from flask import Flask, redirect, url_for, render_template, \
    request, flash, session, Response
import os
import pathlib
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4a@@Q8z\n\xec]/'
base_config_path = str(pathlib.Path.home())+'/.config/subnya'
log_file = base_config_path + '/log/monitor_run.log'
output_dir = ''
sql_path = ''

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
            db = sqlite3.connect(sql_path)
            conn = db.cursor()
            results = [ result[0] for result in  conn.execute('SELECT DISTINCT domain FROM domains')]
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
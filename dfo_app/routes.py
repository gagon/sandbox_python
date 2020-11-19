from dfo_app import app
from flask import render_template
from flask_socketio import SocketIO, send, emit,disconnect
import numpy as np
import json
from dfo_app.utils import utils
import pandas as pd
import datetime
import os


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # for js files not being cached
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

dirname=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

@app.route('/')
@app.route('/index')
def index():
    page_active={"setup":"active"}

    session=utils.get_session_json()

    return render_template('index.html',page_active=page_active,session=session)


@app.route('/integrated_plot')
def integrated_plot_page():
    page_active={"integrated_plot":"active"}
    return render_template('integrated_plot.html',page_active=page_active)


@app.route('/integrated_plot_plot1')
def integrated_plot_page1():
    page_active={"integrated_plot":"active"}

    session=utils.get_session_json()

    # session["dts_data"]=np.random.rand(1000,2000).tolist()
    session["dts_data"]=pd.read_csv(r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\out.csv").values.tolist()


    orig_date=datetime.datetime(2017,1,1)
    timestamps=[
        datetime.datetime.strftime(orig_date+datetime.timedelta(minutes=t),"%Y-%m-%d %H:%M:%S") for t in range(len(session["dts_data"][0]))
    ]
    session["dts_timestamps"]=timestamps

    # print(session["dts_timestamps_count"])

    return render_template('integrated_plot_plot1.html',page_active=page_active,session=session)


@app.route('/integrated_plot_plot2')
def integrated_plot_page2():
    page_active={"integrated_plot":"active"}

    session=utils.get_session_json()

    # session["dts_data"]=np.random.rand(1000,2000).tolist()
    session["dts_data"]=pd.read_csv(r"C:\Users\B.Zhumabayev\Desktop\gecko\data_WellA\raw_DTS\out.csv").values.tolist()


    orig_date=datetime.datetime(2017,1,1)
    timestamps=[
        datetime.datetime.strftime(orig_date+datetime.timedelta(minutes=t),"%Y-%m-%d %H:%M:%S") for t in range(len(session["dts_data"][0]))
    ]
    session["dts_timestamps"]=timestamps

    # print(session["dts_timestamps_count"])

    return render_template('integrated_plot_plot2.html',page_active=page_active,session=session)


@app.route('/config_plot')
def config_plot():
    page_active={"integrated_plot":"active"}
    page_setup={"dashboad_num":5,"plot_num":6}
    json_fullpath=os.path.join(dirname,r"dfo_app\temp\config_plot.json")
    config_plot = json.load(open(json_fullpath))
    return render_template('config_plot.html',page_active=page_active,page_setup=page_setup,config_plot=config_plot)

@app.route('/calibration')
def calibration_page():
    page_active={"calibration":"active"}
    return render_template('calibration.html',page_active=page_active)


@app.route('/processing')
def processing_page():
    page_active={"processing":"active"}
    return render_template('processing.html',page_active=page_active)



@socketio.on('save_session')
def save_session(session):
    utils.save_session_json(session)
    emit("saved")
    return "None"

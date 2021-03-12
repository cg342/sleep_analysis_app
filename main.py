#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory
import subprocess
import time
import flask
# import test
import run
import glob
import os, shutil
from flask_uploads import UploadSet, configure_uploads, DATA
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = flask.Flask(__name__)

app.config['UPLOADED_CSVS_DEST'] = 'uploads'
csvs = UploadSet('csvs', DATA)
configure_uploads(app, csvs)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # clean contents of uploads/ folder before each session
        cleanUploadFolder()
        clearLogfile()
        uploaded_files = request.files.getlist('data[]')
        for f in uploaded_files:
            csvs.save(f)
        inputpath = "uploads/"
        messagelist = run.start(inputpath)
        path = messagelist[0]

        if not path:

            #printerr = []
            with open('_pre.log_') as f:
                content = f.readlines()
            printerr = [x.strip() for x in content] 
            rmlog() # remove log file before session ends
            return flask.render_template("outputmsg.html", msglist = printerr)
        
        res = "" # path for output file to download
        try:
            csv_files = glob.glob(path+"*.csv")
            for f in csv_files:
                if 'unfilled' not in f:
                    res = os.path.join(os.path.dirname(app.instance_path), f)

            return flask.send_file(res, as_attachment=True)
        except Exception as e:

            return flask.render_template("outputmsg.html", msglist = messagelist[1:])

    return render_template('index.html')

def cleanUploadFolder():
        fp = os.path.join(os.path.dirname(app.instance_path), "uploads/")
        
        for file in os.listdir(fp):
            if file != '.gitignore': # disregard the gitignore file, commit and push the empty folder uploads/
                f_del = (os.path.join(fp, file)) 

                try:
                    if os.path.isfile(f_del):
                        os.unlink(f_del)
                    elif os.path.isdir(f_del): 
                        shutil.rmtree(f_del)
                except Exception as e:
                    print(e)
# create an empty log file
def clearLogfile():
    
    filename = "_pre.log_"
    filepath = os.path.join(os.path.dirname(app.instance_path), filename)
    with open(filepath, 'w') as f:
        pass
# remove the log file if exist
def rmlog():
    filepath = os.path.join(os.path.dirname(app.instance_path), "_pre.log_")
    if os.path.exists(filepath):
        print("here")
        os.remove(filepath)

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

if __name__=='__main__':
    app.run(debug=True)
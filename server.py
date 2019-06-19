#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory
# from weather import query_api
import subprocess
import time
import flask
import test
import run
import glob
import os, shutil
from flask_uploads import UploadSet, configure_uploads, DATA


app = flask.Flask(__name__)



app.config['UPLOADED_CSVS_DEST'] = 'uploads'
csvs = UploadSet('csvs', DATA)
configure_uploads(app, csvs)
'''
@app.route('/')
def my_form():
    return render_template('my-form.html')
'''
@app.route('/', methods=['GET', 'POST'])
def my_form_post():

    if request.method == 'POST':
        # clean contents of uploads/ folder before each session
        cleanUploadFolder()

        uploaded_files = request.files.getlist('data[]')
        for f in uploaded_files:
            csvs.save(f)
        inputpath = "uploads/"
        messagelist = run.start(inputpath)
        path = messagelist[0]

        if not path:
            return flask.render_template("outputmsg.html", msglist = messagelist)
        res = ""
    
        try:
            csv_files = glob.glob(path+"*.csv")
            for f in csv_files:
                if 'unfilled' not in f:
                    res = os.path.join(os.path.dirname(app.instance_path), f)

            return flask.send_file(res, as_attachment=True)
        except Exception as e:
            return flask.render_template("outputmsg.html", msglist = messagelist)

        
    return render_template('my-form.html')

def cleanUploadFolder():
        fp = os.path.join(os.path.dirname(app.instance_path), "uploads/")
        
        for file in os.listdir(fp):
            print file
            f_del = (os.path.join(fp, file))
            try:
                if os.path.isfile(f_del):
                    os.unlink(f_del)
                elif os.path.isdir(f_del): 
                    shutil.rmtree(f_del)
            except Exception as e:
                print(e)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
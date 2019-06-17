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
import os
from flask.ext.uploads import UploadSet, configure_uploads, DATA


app = flask.Flask(__name__)

csvs = UploadSet('datafile', DATA)

app.config['UPLOADED_FILES_DEST'] = 'uploads/'
configure_uploads(app, csvs)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
   

    inputpath = flask.request.form['text']
    if inputpath[-1] != '/':
        inputpath += '/'
    messagelist = run.start(inputpath)

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

    # return flask.render_template("outputmsg.html", msglist = messagelist )



if __name__=='__main__':
    app.run(debug=True)
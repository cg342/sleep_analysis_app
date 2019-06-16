#!/usr/bin/env python
from pprint import pprint as pp
# from flask import Flask, flash, redirect, render_template, request, url_for
# from weather import query_api
import subprocess
import time
import flask
import test
import run
import glob
import os

app = flask.Flask(__name__)

# @app.route('/')
# def index():
#     # def inner():
#     #     yield 'hello!'
#     # def some_function():
#     #     text = request.form.get('inputpath')
#     #     flash(test)
#     # text = flask.request.form.get('inputpath')
#     return flask.Response(test.ind(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately

# # def my_form():
# #     return flask.render_template('my-form.html')

# @app.route('/', methods=['POST'])
# def show():
#     return flask.Response(test.show(), mimetype='text/html')

# def my_form_post():
#     input = flask.request.form['input']
#     processed_text = text.upper()
#     return processed_text



# @app.route('/result')
# def showresult():
#     return flask.Response(test.show_result())

@app.route('/')
def my_form():
    return flask.render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    inputpath = flask.request.form['text']
    if inputpath[-1] != '/':
        inputpath += '/'
    messagelist = run.start(inputpath)
    path = messagelist[0]
   
    if not path:
        return flask.render_template("outputmsg.html", msglist = messagelist)
    res = ""

    '''
    csv_files = glob.glob(path+"*.csv")
    for f in csv_files:
        if 'unfilled' not in f:
            res = os.path.join(os.path.dirname(app.instance_path), f)
    print "res: " + res
    return flask.send_file(res, as_attachment=True)
    '''    
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
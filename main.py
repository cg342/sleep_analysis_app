#!/usr/bin/env python
from pprint import pprint as pp
# from flask import Flask, flash, redirect, render_template, request, url_for
# from weather import query_api
import subprocess
import time
import flask
import test

app = flask.Flask(__name__)

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template(
#         'weather.html',
#         data=[{'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},
#         {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
#         {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'}, 
#         {'name':'Quebec'}])

@app.route('/')
def index():
    # def inner():
    #     yield 'hello!'
    # def some_function():
    #     text = request.form.get('inputpath')
    #     flash(test)
    # text = flask.request.form.get('inputpath')
    return flask.Response(test.ind(), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately


@app.route('/', methods=['POST'])
def show():
    return flask.Response(test.show(), mimetype='text/html')



# @app.route("/result" , methods=['GET', 'POST'])
# def result():
#     data = []
#     error = None
#     select = request.form.get('comp_select')
#     resp = query_api(select)
#     pp(resp)
#     if resp:
#        data.append(resp)
#     if len(data) != 2:
#         error = 'Bad Response from Weather API'
#     return render_template(
#         'result.html',
#         data=data,
#         error=error)

if __name__=='__main__':
    app.run(debug=True)
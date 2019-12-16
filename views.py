from flask import Flask, url_for, render_template, request
from livereload import Server

import utils
from query_db import exec_query

# app is a Flask object
app = Flask('app')

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/user_data')
def user_data():
    return utils.user_data_module()


@app.route('/average_params')
def average_params():
    return utils.average_params_module()


@app.route('/all_customers')
def all_customers():
    result = exec_query(f'SELECT * FROM customers WHERE Country =\'{request.args["Country"]}\';')
    return str(result)


@app.route('/astros')
def astros():
    return utils.astros_module()


@app.route('/req_list')
def req_list():
    return utils.req_module()


if __name__ == "__main__":
    app.run()


server.serve()

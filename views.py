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
    return utils.user_data_method()


@app.route('/average_params')
def average_params():
    return utils.average_params_method()


@app.route('/astros')
def astros():
    return utils.astros_method()


@app.route('/gen')
def gen():
    count = request.args["count"]
    return utils.gen_method(count)


@app.route('/req_list')
def req_list():
    return utils.req_method()


@app.route('/all_customers')
def all_customers():
    query_string = f"""
                        SELECT *
                        FROM customers
                        WHERE Country =\'{request.args["Country"]}\';
                    """
    result = exec_query(query_string)
    return str(result)


@app.route('/state_city')
def state_city():
    query_string = f"""
                        SELECT *
                        FROM customers
                        WHERE City=\'{request.args.get("city", "Null")}\'
                        AND State=\'{request.args.get("state", "Null")}\';
                    """
    if not request.args.get("state", ""):
        query_string = f"""
                        SELECT *
                        FROM customers
                        WHERE City=\'{request.args.get("city", "Null")}\'
                    """
    result = exec_query(query_string)
    return str(result)


if __name__ == "__main__":
    app.run()


server.serve()

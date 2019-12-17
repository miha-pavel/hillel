from flask import Flask, url_for, render_template, request
from livereload import Server

import utils
import sql_query_strings
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
    result = utils.gen_method(count)
    response = f"""
                <h1>The task of generation random letters</h1>
                <h2>The task is</h2>
                <p>Вью функция должна принимать параметр который
                регулирует количество символов</p>
                <p>My result is the {count} random letters:</p>
                 {result}
            """
    return response


@app.route('/req_list')
def req_list():
    return utils.req_method()


@app.route('/all_customers')
def all_customers():
    return str(exec_query(sql_query_strings.all_customers_qs(request.args["Country"])))


@app.route('/state_city')
def state_city():
    city = request.args.get("city", '')
    state = request.args.get("state", '')
    response_header = """
                        <h1>The task of City, State filter</h1>
                        <h2>The task is</h2> 
                        <p>Вью функция должна фильтровать таблицу
                        кастомерс по Штату И Городу</p>
                        
                    """
    customer_city_state = f"""
                    <p>The list of customers which live in the {city} state {state} is:</p>
                """
    if not state:
        customer_city_state = f"""
                                <p>The list of customers which
                                live in the {city} is:</p>
                            """
    result = exec_query(sql_query_strings.state_city_qs(city, state))
    response = response_header+customer_city_state+str(result)
    return response


@app.route('/unique_name')
def unique_name():
    result = exec_query(sql_query_strings.unique_name_qs())[0][0]
    response = f"""
                <h1>The task about unique name count</h1>
                <h2>The task is</h2>
                <p>Вью функция должна выводить количество уникальных имен
                (FirstName) из таблицы кастомерс</p>
                <p>My result is the count of the unique names equals: {result}</p>
            """
    return response


@app.route('/profit')
def profit():
    result = exec_query(sql_query_strings.profit_qs())[0][0]
    response = f"""
                    <h1>The task of the common profit </h1>
                    <h2>The task is</h2>
                    <p>Вывести общую прибыль из колонки invoice_items ((UnitPrice * Quantity) + ...)</p>
                    <p>My result is common profit equals: {result}</p>
                """
    return response


if __name__ == "__main__":
    app.run()


server.serve()

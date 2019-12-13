from flask import Flask
# from random import string
from faker import Faker
from livereload import Server

# app is a Flask object
app = Flask('app')

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True
server = Server(app.wsgi_app)


fake = Faker()


@app.route('/')
def home_page():
    return 'This Site is hometask '


if __name__ == "__main__":
    # port=5001 можно изменить порт запуска Фласка
    app.run()


server.serve()

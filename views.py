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


# @app.route('/gen')
# def gen():
#     return ''.join(
#         random.choice(string.ascii_uppercase) for i in range(10)
#     )


@app.route('/user_data')
def user_data():
    style_string = "style='border: 1px solid black;'"
    users_table = """<h1>List 100 random Users</h1>
    <table style="border: 1px solid black;">
    <tr>
        <th {style}>User Id</th>
        <th {style}>User name</th>
        <th {style}>User Email</th>
    </tr>
    {users_data}
    </table>"""
    users_data = ''
    for i in range(100):
        fake_profile = fake.simple_profile(sex=None)
        users_data = users_data + """<tr>
                                        <td {style}>{user_id}</td>
                                        <td {style}>{user_name}</td>
                                        <td {style}>{user_email}</td>
                                    </tr>""".format(
                                    user_id=i+1,
                                    user_name=fake_profile.get("name"),
                                    user_email=fake_profile.get("mail"),
                                    style=style_string
                                    )
    return users_table.format(users_data=users_data,
                            style=style_string)


if __name__ == "__main__":
    app.run()


server.serve()
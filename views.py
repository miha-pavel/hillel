from flask import Flask
# from random import string
from faker import Faker
from livereload import Server
import pandas as pd

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


style_string = "style='border: 1px solid black;'"
@app.route('/user_data')
def user_data():
    users_table = """<h1>List 100 random Users</h1>
    <table {style}>
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


@app.route('/average_params')
def average_params():
    df = pd.read_csv('hw.csv', sep=',')
    header_list = df.columns.tolist()
    header_list.pop(0)
    height = "Height"
    weight = "Weight"
    average_param = ""
    average_table = """
                        <h1>Average Data</h1>
                        <table {style}>
                            {average_param}
                        </table>
                    """
    for column_name in header_list:
        if height in column_name:
            average_param = average_param + """
                <tr>
                    <td {style}>{height} (Cm)</td>
                    <td {style}>{height_data}</td>
                </tr>
            """.format(height=height,
            height_data=round(df[column_name].mean()*2.54, 2),
            style=style_string)
        else:
            average_param = average_param + """
                <tr>
                    <td {style}>{weight} (Kg)</td>
                    <td {style}>{weight_data}</td>
                </tr>
            """.format(weight=weight,
            weight_data=round(df[column_name].mean()*0.453592, 2),
            style=style_string)
    return average_table.format(average_param=average_param, style=style_string)


if __name__ == "__main__":
    app.run()


server.serve()

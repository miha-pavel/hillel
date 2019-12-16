from flask import Flask, url_for, render_template
from faker import Faker
from livereload import Server
import pandas as pd
import requests

# app is a Flask object
app = Flask('app')

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True
server = Server(app.wsgi_app)


fake = Faker()


@app.route('/')
def home_page():
    return render_template('index.html')


style_string = "style='border: 1px solid black;'"
@app.route('/user_data')
def user_data():
    """Function generate 100 random users and create html template

        Parameters:

        Returns:
        str: The html template which includes table with 100 random users
    """
    users_table = """
        <h1>List 100 random Users</h1>
        <table {style}>
        <tr>
            <th {style}>User id</th>
            <th {style}>User name</th>
            <th {style}>User email</th>
        </tr>
        {users_data}
        </table>
        <a href="/">Back</a>"""
    users_data = ''
    for i in range(100):
        fake_profile = fake.simple_profile(sex=None)
        users_data += """<tr>
                        <td {style}>{user_id}</td>
                        <td {style}>{user_name}</td>
                        <td {style}>{user_email}</td>
                    </tr>""".format(
                    user_id=i+1,
                    user_name=fake_profile.get("name"),
                    user_email=fake_profile.get("mail"),
                    style=style_string
                    )
    return users_table.format(users_data=users_data, style=style_string)


@app.route('/average_params')
def average_params():
    """Function read *.csv file and finds the average value each column

    Parameters:

    Returns:
    str: The html template which includes table average height and weight data
    """
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
            <a href="/">Back</a>
        """
    for column_name in header_list:
        if height in column_name:
            average_param += """
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


@app.route('/astros')
def astros():
    """Function make a request to the URL and create html templates with astronaut list

    Parameters:

    Returns:
    str: The html template which includes astronaut list
    """
    url = 'http://api.open-notify.org/astros.json'
    responseJSON = requests.get(url).json()
    astros = """
        <h1>List astronauts</h1>
        <h2>There are {astronauts_count} astronauts in orbit</h2>
        <ul>
            {astronauts_list}
        </ul>
        <a href="/">Back</a>
        """
    astronauts_list = ''
    for astronaut in responseJSON.get('people'):
        astronauts_list += "<li>{astronaut_name}</li>".format(
                            astronaut_name=astronaut.get("name"),
                            )
    return astros.format(astronauts_list=astronauts_list,
                        astronauts_count=responseJSON.get('number'))


@app.route('/requir_list')
def requir_list():
    """Function read requirements.txt file and create html template
    with list packages which were used in the project

    Parameters:

    Returns:
    str: The html template which includes list packages
    """
    file_data = open("requirements.txt", "r")
    requirements_list = """
        <h1>List requirements</h1>
        <p>In my Flask project I used next library:</p>
        <ul>
            {requir_list_item}
        </ul>
        <a href="/">Back</a>
        """
    requir_list_item = ''
    for line in file_data:
        requir_list_item += "<li>{line}</li>".format(line=line)
    return requirements_list.format(requir_list_item=requir_list_item)


if __name__ == "__main__":
    app.run()


server.serve()

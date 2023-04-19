import flask
import requests
import csv

from faker import Faker

app = flask.Flask(__name__)


@app.route('/requirements/')                                          # /requirements/
def requirements_list():
    file_txt = open('requirements.txt', 'r')
    reqirements = file_txt.read()
    return flask.render_template('requirements.html', file=reqirements)


@app.route('/')                                                         # /users/generate
def index():
    return flask.render_template('generate.html')


@app.route('/users/generate')
def generate_fullnames():
    num_fullnames = int(flask.request.args['numberFullnames'])
    amount = int(flask.request.args['numberFullnames'])
    fake = Faker()

    list_names = []
    for i in range(amount):
        i = [fake.name(), fake.email()]
        list_names += i

    return flask.render_template('fullnames-and-emails.html', fullnamesandemails=list_names)


@app.errorhandler(404)
def not_found(error):
    return 'File Not Found', 404


@app.route('/mean/')                                                    # /mean/
def mean():
    file = open("hw.csv", "r")
    data = list(csv.DictReader(file, delimiter=","))
    file.close()

    height = [float(row[' "Height(Inches)"']) for row in data]
    weight = [float(row[' "Weight(Pounds)"']) for row in data]

    height_mean = round((sum(height)/len(height))*2.54, 3)
    weight_mean = round((sum(weight) / len(weight))*0.45359237, 3)

    return flask.render_template('mean.html', height_mean=height_mean, weight_mean=weight_mean)


@app.route('/space/')                                                  # /space/
def api_view():
    response = requests.get('http://api.open-notify.org/astros.json')
    number = response.json()

    return flask.render_template('api.html', number=number['number'])


if __name__ == '__main__':
    app.run(debug=True)
import beeline
beeline.init(
    # Get this via https://ui.honeycomb.io/account after signing up for Honeycomb
    writekey='1252c1ce92b00ad574131fa6e873366d',
    # The name of your app is a good choice to start with
    dataset='cheems-app',
    service_name='cheems-app',
    # debug=True, # defaults to False. if True, data doesn't get sent to Honeycomb
)


from flask import Flask, jsonify
from random import seed
from random import randint
import os
from flask import render_template, redirect, url_for


seed(1)
app = Flask(__name__)


def load_from_file(filename):
    output = []
    with open(filename) as my_file:
        for line in my_file:
            output.append(line.strip())
    return output


def load_from_dir(directory):
    output = []
    for filename in os.listdir(directory):
        with open(directory + "/" + filename) as file:
            output.append(file.read())
    return output


def get_random_array_element(array):
    return array[randint(0, len(array)-1)]


soad = load_from_file("lyrics/soad")
cheems = load_from_dir("ascii/cheems")


@app.route('/')
def index():
    return render_template(
        'index.html',
        cheems=get_random_array_element(cheems),
        soad=get_random_array_element(soad)
    )



@app.route('/api/<version>/soad')
def soad_api(version):
    if version == "v1":
        return jsonify({"line": "%s" % get_random_array_element(soad)})
    if version == "v2":
        return jsonify(["%s" % get_random_array_element(soad)])
    return redirect(url_for('index'))



@app.route('/api/<version>/cheems')
def cheems_api(version):
    if version == "v1":
        return "%s" % get_random_array_element(cheems)
    if version == "v2":
        return jsonify({"ascii": "%s" % get_random_array_element(cheems)})
    if version == "v3":
        return jsonify(["%s" % get_random_array_element(cheems)])
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
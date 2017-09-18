from flask import render_template, request, url_for, redirect, jsonify
from app import app
from app.forms import ImageSetForm
import os
import subprocess
import socket

import pymysql
import pymysql.cursors

import sqlite3

app.secret_key = 's3cr3t'


@app.route('/displayoutputstatus')
def displayoutputstatus():
    result = displayoutputstatus()
    return jsonify(result)


@app.route('/', methods=['POST', 'GET'])
def index():
    activeSet = "Not Here"
    version = '0.1'
    current_image = "NONE"
    selectedSet = "No Set Selected Yet"
    #   form = ImageSetForm()
    imageset_form = ImageSetForm()

    imgchange_status = displayoutputstatus()


'''if request.method == 'POST':
   print("We got a POST request")
   current_image = request.form['current_image']
   print("We got the current image set: " + current_image)
   print("This is the value for out1: " + request.form['out1'])
   out1 = request.form['out1']
   out2 = request.form['out2']
   out3 = request.form['out3']
   out4 = request.form['out4']
   out5 = request.form['out5']
   out6 = request.form['out6']
   out7 = request.form['out7']
   out8 = request.form['out8']'''

# Coll
if request.method == 'POST':

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Password1',
                                 db='PieFace',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    sql = "SELECT * FROM PieFace.new_table;"
    cursor.execute(sql)

    result = cursor.fetchone()

    selectedSet = result["test"]

    print("Request Form Fields= " + str(request.form) + "\n")
    print("Active = " + str(request.form['active']) + "\n")
    print("Select = " + str(request.form['select']) + "\n")

    print("activate button was pressed" + imageset_form.activate.data)
    print("select button was pressed" + imageset_form.select.data)
    if imageset_form.validate():
        print("activate button was pressed : {value}".format(value=imageset_form.activate.data))
        print("select button was pressed : {value}".format(value=imageset_form.select.data))

    if imageset_form.activate.data == True:
        activeSet = request.form['imageSet']

    elif imageset_form.select.data == True:
        selectedSet = request.form['imageSet']

if current_image != "NONE":
    print("Changing the current image to: " + current_image)
    # this works: c = subprocess.call(['/home/pi/display.sh', current_image])
    c = subprocess.Popen(['/home/pi/display.sh', current_image], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Right after I ran the command" + current_image)
    return render_template('index.html',
                           title='PieFace',
                           hdmichange_status=hdmichange_status,
                           imgchange_status=displayoutputstatus())

hdmichange_status = "out1: " + out1
try:
    hdmichange_status = gethdmi()
except:
    print("Error getting hdmi status!")

print(hdmichange_status)

return render_template('index.html',
                       imageset_form=imageset_form,
                       title='PieFace',
                       active=activeSet.upper(),
                       version=1.0,
                       selected=selectedSet,
                       hdmichange_status=hdmichange_status,
                       imgchange_status=displayoutputstatus())

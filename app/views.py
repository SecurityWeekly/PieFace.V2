from flask import render_template, request, url_for, redirect, jsonify
from app import app
from app.forms import ImageSetForm
import os
import subprocess
import socket
import telnetlib

import sqlite3

app.secret_key = 's3cr3t'


def gethdmi():
    #
    # These are the codes and the responses
    #
    # R8001	:  Read INPUT Link States
    # R8002	:  Read OUTPUT Link States
    # R8003	:  Read INPUT HDCP States
    # R8004	:  Read OUTPUT HDCP States
    # R8006	:  Read OUTPUT Channel Set States
    # R8007	:  Read OUTPUT ON/OFF States
    # R8008	:  Read External Audio Output Enable States
    # R8009	:  Read INPUT EDID Set States
    # R8010[x1]	:  Read INPUT x1 EDID Data
    # R8011[x1]	:  Read OUTPUT x1 EDID Data
    # R8012	:  Read Network States
    # R8017	:  Read Cascading Mode Enable/Disable

    read_code = {'input_link_states': ">@ R8001\r", \
                 'output_link_states': ">@ R8002\r", \
                 'input_hdcp_states': ">@ R8003\r", \
                 'output_hdcp_states': ">@ R8004\r", \
                 'output_channel_states': ">@ R8006\r", \
                 'output_onoff_states': ">@ R8007\r", \
                 'system_status': ">@ RSTA\r", \
                 'network_states': ">@ R8012\r"}

    HOST = '172.16.1.35'
    TCP_PORT = 23
    BUFFER_SIZE = 32767

    # Telnet to the HDMI router
    tn = telnetlib.Telnet(HOST)
    print("Read HDMI Input Link States by sending: " + read_code['input_link_states'])
    # Write the command to read the input link states
    #   tn.write(read_code['input_link_states'])
    # What input is going to which output?
    tn.write(read_code['output_channel_states'])
    # Read data until there is a new line
    data = tn.read_until('\n\r', 1)
    #   print("We got: " + data)
    #   tn.write(read_code['system_status'])
    #   data=tn.read_until('\n\r',2)
    #   print("We got: " + data)
    tn.close()
    return data


def displayoutputstatus():
    f = open('/home/wpaquin/Desktop/pieface/app/display.output', 'r')
    file_contents = f.read()
    return file_contents
    f.close()


# @app.route('/displayoutputstatus')
# def displayoutputstatus():
#    #result = displayoutputstatus()
#    result = "Hi Mark!"
#    return jsonify(result)

@app.route('/', methods=['POST', 'GET'])
def index():
    version = '0.1'
    current_image = "NONE"
    out1 = ""
    out2 = ""
    out3 = ""
    out4 = ""
    out5 = ""
    out6 = ""
    out7 = ""
    out8 = ""
    hdmichange_status = "None"
    activeSet = "Not Here"

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

    if request.method == 'POST':

        print("Request Form Fields= " + str(request.form) + "\n")
        # print("Active = " + str(request.form['active']) + "\n")
        # print("Select = " + str(request.form['select']) + "\n")

        #       print "activate button was pressed" + imageset_form.activate.data
        #       print "select button was pressed" + imageset_form.select.data
        #       if imageset_form.validate():
        print("activate button was pressed : {value}".format(value=imageset_form.activate.data))
        print("select button was pressed : {value}".format(value=imageset_form.select.data))

        if imageset_form.activate.data == True:
            activeSet = request.form['imageSet']

        elif imageset_form.select.data == True:
            selectedSet = request.form['imageSet']

    '''if current_image != "NONE":
       print("Changing the current image to: " + current_image)
       # this works: c = subprocess.call(['/home/pi/display.sh', current_image])
       c = subprocess.Popen(['/home/pi/display.sh', current_image],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       print("Right after I ran the command" + current_image)
       return render_template('index.html',
                               title='PieFace',
                               hdmichange_status=hdmichange_status,
                               imgchange_status=displayoutputstatus())'''

    # hdmichange_status = "out1: " + out1
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

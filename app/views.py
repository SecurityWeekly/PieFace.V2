from flask import render_template, request, url_for, redirect, jsonify
from app import app
from app.forms import ImageSetForm
from app import hdmi_controller
from app import database_handler
import subprocess

# declare new hdmi_controller instance

hdmi_controller = hdmi_controller.hdmi_controller()
database_handler = database_handler.database_handler()

app.secret_key = 's3cr3t'


@app.route('/displayoutputstatus')
def potato():
    print("Displaying output status")


@app.route('/', methods=['POST', 'GET'])
def index():
    activeSet = "Not Here"
    version = '0.1'
    current_image = "NONE"
    selectedSet = "No Set Selected Yet"
    form = ImageSetForm()
    imageset_form = ImageSetForm()

    imgchange_status = hdmi_controller.display_output_status

    # Coll
    if request.method == 'POST':

        selectedSet = database_handler.select_all()

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
        return render_template('index.html', title='PieFace', hdmichange_status=hdmi_controller.get_hdmi_status,
                               imgchange_status=hdmi_controller.display_output_status())

    # hdmichange_status = "out1: " + hdmi_controller.output1
    try:
        hdmichange_status = hdmi_controller.get_hdmi_status()
    except:
        print("Error getting hdmi status!")

        return render_template('index.html',
                               imageset_form=imageset_form,
                               title='PieFace',
                               active=activeSet.upper(),
                               version=1.0,
                               selected=selectedSet,
                               hdmichange_status=hdmi_controller.get_hdmi_status,
                               imgchange_status=hdmi_controller.display_output_status())



    print(hdmichange_status)

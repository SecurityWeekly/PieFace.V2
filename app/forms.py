from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from database_handler import db_functions, sessionmaker

# init hdmi_controller class
class ImageSetForm(Form):
    db = db_functions()


    '''imageSet = SelectField('ImageSet',
                           choices=[('psw', 'PSW'), ('esw', 'ESW'), ('ssw', 'SSW'), ('hnn', 'HNN'), ('sg', 'SG'),
                                    ('sgshorts', 'SGSHORTS'), ('sgnews', 'SGNEWS'), ('static', 'STATIC')])'''
    select = SubmitField("Select Image Set")
    activate = SubmitField("Activate Image Set")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")

    ResW = TextField("resWidth")
    ResH = TextField("resHeight")
    PauseTime = TextField("Pause Time in Seconds")
    isDefault = BooleanField("Default Image Set:")
    imageType = RadioField("Type", choices=[('image', 'Image'), ('video', 'Video')])

    # hdmi controller class to be used here to get inputs/outputs
    # set selected item for dropdowns with something like hdmi_controller.outputs['output1']

    output1 = SelectField('Output1',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output2 = SelectField('Output2',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output3 = SelectField('Output3',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output4 = SelectField('Output4',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output5 = SelectField('Output5',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output6 = SelectField('Output6',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output7 = SelectField('Output7',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    output8 = SelectField('Output8',
                          choices=[('', ''), ('input1', 'Input 1'), ('input2', 'Input 2')])
    switch = SubmitField("Submit Output")

    
    
    imageSet = QuerySelectField(query_factory=db.enabled_categories, allow_blank=True, get_label="Name")

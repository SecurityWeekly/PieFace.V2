from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, BooleanField


class ImageSetForm(Form):
    imageSet = SelectField('ImageSet',
                           choices=[('psw', 'PSW'), ('esw', 'ESW'), ('ssw', 'SSW'), ('hnn', 'HNN'), ('sg', 'SG'),
                                    ('sgshorts', 'SGSHORTS'), ('sgnews', 'SGNEWS'), ('static', 'STATIC')])
    select = SubmitField("Select Image Set")
    activate = SubmitField("Activate Image Set")

    resWidth = TextField("resWidth")
    resHeight = TextField("resHeight")
    pauseTime = TextField("Pause Time in Seconds")
    isDefault = BooleanField("Default Image Set:")
    imageType = RadioField("Type", choices=[('image', 'Image'), ('video', 'Video')])

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

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

    # Hashtag

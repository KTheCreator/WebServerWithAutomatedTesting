from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
#Handles the generation of the input form
class inputForm(FlaskForm):
    #Creates the string field for the user's input
    username = StringField('UserName')
    #Creates the submit button for the form
    submit = SubmitField('Submit Name')

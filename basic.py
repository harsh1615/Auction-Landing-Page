from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import Flaskform
from wtforms import (StringField,BooleanField,DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField)
from wtfforms.validators import DataRequired

app = Flask(__name__)

app.config['secret_key]= 'mykey'

class InfoForm(FlaskForm):

breed = StringField('whats your name',validotor=[DataRequired()])
mood = SelectField('choice what u r in for:',choices=[('buy','buyer','sell','seller')])

feedback = TextAreaField()
submit = SubmitField('submit)

@app.route('/',methods=['GET','POST'])
def index

form = InfoForm()
if form.validate_on_submit():
session['breed'] = form.breed.data 
session['mood'] = form.mood.data 
session['feedback'] = form.feedback.data 

return redirect(url_for('thankyou'))

return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou()
return render_template('thankyou.html')
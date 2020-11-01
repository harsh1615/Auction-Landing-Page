import os
from flask import Flask
from flask_sqlalchmey import SQLAlechemy

basedir = os.path(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLAlechemy_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLAlechemy_TRACK_MODIFICATIONS] = False 

db = SQLAlechemy(app)


class auction(db.Model):

__tablename__ = 'auctions'

#manual table#

id = db.Column(db.Integer,primary_key=True)
name = db.Column(db.text)
age = db.Column(db.integer)

def __init__(self,name,age):
self.name=name
self.age=age

def __repr__(self)
return f"Puppy{self.name} is {self.age} years old"
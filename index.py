import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.cofig['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Items(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	image = db.Column(db.Text)
	base_price = db.Column(db.Integer)

	def __init__(self, name, image, base_price):
		self.name = name
		self.image = image
		self.base_price = base_price

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/creation')
def creation():
	return render_template('creation.html')

@app.route('/product/<id>')
def product(id):
	return render_template('item.html')

@app.route('/wishlist')
def wishlist():
	return render_template('watchlist.html')

@app.route('/product/<id>')
def product(id):
    return render_template('item.html')


if __name__ == '__main__':
    app.run()
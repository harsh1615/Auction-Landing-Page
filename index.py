import os
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from werkzeug.security import generate_password_hash, check_password_hash


# bcrypt = Bcrypt()
# password = "supersecretpassword"
# hashed_password = bcrypt.generate_password_hash(password=password)

app = Flask(__name__)
# app.config["SECRET_KEY"] = "mysecretkey"
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# Migrate(app, db)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
# class Items(db.Model):
# 	__tablename__ = 'products'
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.Text)
# 	image = db.Column(db.Text)
# 	base_price = db.Column(db.Integer)

# 	def __init__(self, name, image, base_price):
# 		self.name = name
# 		self.image = image
# 		self.base_price = base_price

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/creation')
def creation():
	return render_template('creation.html')

@app.route('/wishlist')
def wishlist():
	return render_template('watchlist.html')


@app.route('/product/<id>')
def product(id):
	return render_template('item.html')

if __name__ == '__main__':
    app.run(debug=True)

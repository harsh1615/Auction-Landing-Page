from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run()
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' %name


@app.route('/contact')
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
	return "Hello World! This is Flask Tutorial!"

@app.route('/test')
def test():
	return render_template('post.html')

@app.route('/post'), 

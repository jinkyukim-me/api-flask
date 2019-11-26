from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
	return "Hello World! This is Flask Tutorial!"

@app.route('/test')
def test():
	return render_template('post.html')

@app.route('/post', methods=['post'])
def post():
	value = request.form['test']
	return render_template('default.html')

if __name__ == "__main__":
	app.run(debug=True)
 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Home'

@app.route('/test', methods=['GET','POST'])
def test():
	if request.method == 'GET':
		return render_template('post.html')
	elif request.method == 'POST':
		value = request.form['test']
		return render_template('default.html')

if __name__ == '__main__':
	app.run(debug=True)


from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

def make_bold(funct):
	def wrapper():
		return f'<b>{funct()}</b>'
	return wrapper

def make_emphasis(funct):
	def wrapper():
		return f'<em>{funct()}</em>'
	return wrapper

def make_underlined(funct):
	def wrapper():
		return f'<u>{funct()}</u>'
	return wrapper

@app.route("/")
def hello_world():
	return '<h1 style="text-align: center">Hello world!</h1>'\
			'<p>This is a paragraph.<p>'\
			'<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWRxMnVteTJqdHY5Y2M4a2VhOXp4N3FjZWMxczRkYnl3MnZiank2ZiZlcD12MV9naWZzX3RyZW5kaW5nJnRpZD04NjVhMmM3ODk1ZmZjNzhiZjE5NzU0YjgwODI1YTk5MGMyOWJlN2U0MmYxMzc5OGM4NmQ5MDhkMzBhMTIyYTU1JmN0PWcmYXA9MA/i4YVzT5V66gZgdYgCR/giphy.gif">'


@app.route('/bye')
@make_bold
@make_emphasis
def bye():
	return "Bye!"











app.run(debug=True)
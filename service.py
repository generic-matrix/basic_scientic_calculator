from flask import Flask
from flask import request
from math import *
import base64
app = Flask(__name__)

#Check if the expression is valid
def eval_expression(expression):
	#check of paranthesis balance
	if(expression.count("(")==expression.count(")")):
		return True
	else:
		return False	
	

@app.errorhandler(500)
def internal_error(error):
	return "Error"
	
@app.route('/eval')
def calculator():
	expression=base64.b64decode(request.args.get('expression')).decode("utf-8") 
	if(eval_expression(expression)):
		res=eval(expression)
		return str(res)
	else:
		return "Invalid Expression"
	
@app.route('/')
def index_page():
	file=open("index.html", "r")
	data =file.read()
	file.close()
	return data
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
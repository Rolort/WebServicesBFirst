import logs
from flask import jsonify
from flask import flash, request
from app import app
import json

#Handling Errors
def catalog_error(arg):
	return {
		2003: database_error(),
		0: request_error(7)
	}.get(arg, error_general())

@app.errorhandler(500)
def error_general(error=None):
	response = {
		'status': 500,
		'message': 'Internal Server Error'
	}
	resp = jsonify(response)
	resp.status_code = 500
	logs.logReq(str(response), str(resp.status_code), "error_general")
	return resp

@app.errorhandler(403)
def user_notfound(error=None):
	response = {
		'status': 403,
		'message': 'User not exist'
	}
	resp = jsonify(response)
	resp.status_code = 403
	logs.logReq(str(response), str(resp.status_code), "user_notfound")
	return resp

def pin_notfound(error=None):
	response = {
		'status': 403,
		'message': 'Pin error'
	}
	resp = jsonify(response)
	resp.status_code = 403
	logs.logReq(str(response), str(resp.status_code), "Pin error")
	return resp

#Error con base de datos
@app.errorhandler(503)
def database_error(error=None):
	response = {
		'status': 503,
		'message': 'Sorry we have problems with connections'
	}
	resp = jsonify(response)
	resp.status_code = 503
	logs.logReq(str(response), str(resp.status_code), "database_error")
	return resp

@app.errorhandler(400)
def request_error(x):
	a = 'Error'
	a = {
		1: 'User Error',
		2: 'Password Error',
		3: 'Method Error',
		4: 'Bad Request',
		5: 'PhoneNumber Error',
		6: 'PIN Error',
		7: 'Missing Information',
		8: 'User is already register',
		9: 'Error in Register',
		10: 'Duplicated Name',
		11: 'Error in category'
	}.get(x, 'Unknown Error')
	response = {
		'status': 400,
		'message': a
	}
	resp = jsonify(response)
	resp.status_code = 400
	logs.logReq(str(response), str(resp.status_code), "request_error")
	return resp

def user_exist():
	response = {
		'status_code': 200,
		'message': 'User exist'
	}
	resp = jsonify(response)
	resp.status_code = 200
	logs.logReq(str(response), str(resp.status_code), "user_exist")
	return resp

def signUp_response(step, pin):
	if step:
		message = 'SignUp Exist'
	else:
		message = 'SignUp not Exist'
	signUp = {
	    'pin': pin,
		'step': step,
		'response': {
			'status_code': 200,
			'message': message
		}
	}
	resp = jsonify(signUp)
	resp.status_code = 200
	logs.logReq(str(signUp), str(resp.status_code), "signUp_response")
	return resp

def pinSuccess_response():
	response = {
		'status_code': 200,
		'message': 'Validated Pin'
	}
	resp = jsonify(response)
	resp.status_code = 200
	logs.logReq(str(response), str(resp.status_code), "Pin Validated")
	return resp

def userSuccess_response():
	response = {
		'status_code': 200,
		'message': 'Registered User'
	}
	resp = jsonify(response)
	resp.status_code = 200
	logs.logReq(str(response), str(resp.status_code), "User Success")
	return resp

def hostSuccess_response():
	response = {
		'status_code': 200,
		'message': 'Registered Host'
	}
	resp = jsonify(response)
	resp.status_code = 200
	logs.logReq(str(response), str(resp.status_code), "Host Success")
	return resp

def UserAddress_response():
	response = {
		'status_code': 200,
		'message': 'Registered Address in User'
	}
	resp = jsonify(response)
	resp.status_code = 200
	logs.logReq(str(response), str(resp.status_code), "User Address Success")
	return resp

def categories_response(array_categ):
	categories = {
		'categories': array_categ,
		'response': {
			'status_code': 200,
			'message': 'Success'
		}
	}
	resp = jsonify(categories)
	print(resp)
	resp.status_code = 200
	logs.logReq(str(categories), str(resp.status_code), "Categories")
	return resp

def locations_response(array_location):
	search = {
		'stores': array_location,
		'response': {
			'status_code': 200,
			'message': 'Success'
		}
	}
	resp = jsonify(search)
	print(resp)
	resp.status_code = 200
	logs.logReq(str(search), str(resp.status_code), "Search")
	return resp



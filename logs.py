import pymysql
import json
import db_config
from datetime import datetime

request = "";
device = "";
ip = "";

def logReq(response, code, error):
	try:
		connection = db_config.getConnectionLogs()
		print("Connection Successful Logs :D!")
		now = datetime.now()
		sql = "INSERT INTO Request(Request, Response, Code, Error, ReqDaTime, Device, IP) VALUES(%s, %s, %s, %s, %s, %s, %s)"
		data = (request, response, code, error, now, device, ip)
		cursor = connection.cursor()
		cursor.execute(sql, data)
		connection.commit()
	except Exception as e:
		print(e)

def getRequest():
	print (request)
	print (device)
	print (ip)
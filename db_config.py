import MySQLdb

def getConnection():
	connection = MySQLdb.Connect(host="127.0.0.1", port=3306, user="aopina", passwd="12141618", db="LinesDB")
	return connection

def getConnectionLogs():
	connection = MySQLdb.Connect(host="127.0.0.1", port=3306, user="aopina", passwd="12141618", db="logs")
	return connection


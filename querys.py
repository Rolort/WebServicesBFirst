import pymysql
import json
from app import app
import db_config
import logs
import responses
import process
import model

def getPin(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM SignUp WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			pin = row[2]
			cursor.close()
			connection.close()
			return pin
		else:
			cursor.close()
			connection.close()
			return ""
	except Exception as e:
		print (e)
		return ""

def getDatePin(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM SignUp WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			date = row[4]
			cursor.close()
			connection.close()
			return date
		else:
			cursor.close()
			connection.close()
			return
	except Exception as e:
		print (e)
		return ""

def getStep(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM SignUp WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			step = int(row[3])
			cursor.close()
			connection.close()
			return step
		else:
			cursor.close()
			connection.close()
			return 0
	except Exception as e:
		print (e)
		return ""

def getCategories():
	try:
		array_categ = []
		connection = db_config.getConnection()
		connection.set_character_set('utf8')
		print("Connection Successful Categories!")
		sql = "SELECT * FROM Categories ORDER BY 'order'"
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		print(rows)
		cursor.close()
		connection.close()
		for row in rows:
			t = {'name':row[1], 'description':row[2], 'picture':row[3], 'active':row[4], 'order':row[5]}
			array_categ.append(t)

		return array_categ
	except Exception as e:
		print (e)
		return ""

def getKey(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM Users WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			idUser = int(row[0])
			cursor.close()
			connection.close()
			return idUser
		else:
			cursor.close()
			connection.close()
			return 0
	except Exception as e:
		print (e)
		return "Error database connection"

def getKeyStore(idUsers, name):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM Store WHERE idUsers = %s AND name = '%s'"%(idUsers, name)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			idStore = int(row[0])
			cursor.close()
			connection.close()
			return idUsers
		else:
			cursor.close()
			connection.close()
			return 0
	except Exception as e:
		print (e)
		cursor.close()
		connection.close()
		return 0

def getStoresByCategory(idCategories):
	try:
		array_categ = []
		connection = db_config.getConnection()
		connection.set_character_set('utf8')
		print("Connection Successful Categories!")
		sql = "SELECT * FROM Store INNER JOIN StoreAddress INNER JOIN StoreSchedules INNER JOIN  StoreTags \
		       on Store.idStore= StoreAddress.idStore AND Store.idStore= StoreSchedules.idStore AND \
		       Store.idStore= StoreTags.idStore WHERE Store.active = 1 AND StoreTags.idCategories = %d"%(idCategories)
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		print(rows)
		cursor.close()
		connection.close()
		for row in rows:
			t = {'id':row[0],
				 'name':row[1],
				 'description':row[2],
				 'email':row[3],
				 'contact_phone':row[4],
				 'extra_phone':row[5],
				 'website':row[6],
				 'idCategories':row[29],
				 'storeAddress':{
				 	'name':row[10],
				 	'lat':row[11],
				 	'lng':row[12],
				 	'street':row[13],
				 	'municipality':row[14],
				 	'state':row[15],
				 	'zip':row[16]
				 },
				 'StoreSchedules':{
				 	'monday':row[19],
				 	'tuesday':row[20],
				 	'wednesday':row[21],
				 	'thursday':row[22],
				 	'friday':row[23],
				 	'saturday':row[24],
				 	'sunday':row[25]
				 },
				 'distance':0
				}
			array_categ.append(t)

		return array_categ
	except Exception as e:
		print (e)
		return ""

def getStores(text):
	try:
		array_categ = []
		text = text + '%'
		connection = db_config.getConnection()
		connection.set_character_set('utf8')
		print("Connection Successful Stores!")
		sql = "SELECT * FROM Store INNER JOIN StoreAddress INNER JOIN StoreSchedules INNER JOIN  StoreTags \
		       on Store.idStore= StoreAddress.idStore AND Store.idStore= StoreSchedules.idStore AND \
		       Store.idStore= StoreTags.idStore WHERE Store.active = 1 AND (Store.name LIKE '%s' OR \
		       StoreAddress.name LIKE '%s' or StoreAddress.street like '%s')"%(text, text, text)
		print(sql)
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		print(rows)
		cursor.close()
		connection.close()
		array = model.createJsonStore(rows)
		return array
	except Exception as e:
		print (e)
		return ""

def updateStep(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful!")
		sql = "SELECT * FROM SignUp WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			row = cursor.fetchone()
			step = int(row[3])
			step = step + 1
			print (step)
			sql = "UPDATE SignUp SET step = %d WHERE phoneNumber = %s"%(step, phoneNumber)
			cursor = connection.cursor()
			cursor.execute(sql)
			connection.commit()
			cursor.close()
			connection.close()
		else:
			cursor.close()
			connection.close()
	except Exception as e:
		print (e)

def saveUser(user):
	try:
		connection = db_config.getConnection()
		print("Connection Successful User!")
		birth = process.strToDate(user.birthdate)
		sql = "INSERT INTO Users(name, lastName, birthdate, phoneNumber, email, isHost) VALUES ('%s', '%s', '%s', '%s', '%s', %d)"%(user.name, user.lastName, birth, user.phoneNumber, user.email, user.isHost)
		print (sql)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def saveLogin(user):
	try:
		idUser = getKey(user.phoneNumber)
		connection = db_config.getConnection()
		print("Connection Successful User!")
		sql = "INSERT INTO Login(userName, password, idUsers) VALUES(%s, %s, %d)" \
		      %(user.phoneNumber, user.password, idUser)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def saveStore(store, user):
	try:
		idUsers = getKey(user)
		connection = db_config.getConnection()
		print("Connection Successful Store!")
		sql = "INSERT INTO Store(name, description, email, contact_phone, extra_phone, website, active, idUsers) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" \
		      %(store.name, store.description, store.email, store.contact_phone, store.extra_phone, store.website, store.active, idUsers)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def saveAddress(address, idStore):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Store Address!")
		sql = "INSERT INTO StoreAddress(name, lat, lng, street, municipality, state, zip, idStore) VALUES('%s', %f, %f, '%s', '%s', '%s', '%s', %d)" \
		      %(address.name, address.lat, address.lng, address.street, address.municipality, address.state, address.zip, idStore)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def saveSchedule(schedule, idStore):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Store Schedule!")
		sql = "INSERT INTO StoreSchedules(monday, tuesday, wednesday, thursday, friday, saturday, sunday, idStore) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" \
		      %(schedule.monday, schedule.tuesday, schedule.wednesday, schedule.thursday, schedule.friday, schedule.saturday, schedule.sunday, idStore)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def saveUserAddress(userAddress, user):
	try:
		idUser = getKey(user)
		connection = db_config.getConnection()
		print("Connection Successful User Address!")
		sql = "INSERT INTO UserAddresses(name, lat, lng, street, number, suburb, municipality, state, zip, isSelected, idUsers) VALUES('%s', '%f', '%f', '%s', '%s', '%s', '%s', '%s', '%s', '%d', %d)" \
		      %(userAddress.name, userAddress.lat, userAddress.lng, userAddress.street, userAddress.number, userAddress.suburb, userAddress.municipality, userAddress.state, userAddress.codezip, userAddress.isSelected, idUser)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

#Revisar esta funcion
def saveTags(tags, idStore):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Tags!")
		sql = "INSERT INTO StoreTags(tags, idCategories, idStore) VALUES('%s', %d, %d)" \
		      %(tags.tags, tags.idCategories, idStore)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False


def isUser(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful User!")
		sql = "SELECT * FROM Users WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		if result:
			return True
			cursor.close()
			connection.close()
		else:
			cursor.close()
			connection.close()
			return False
	except Exception as e:
		print (e)
		return False

def isLogin(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Login!")
		sql = "SELECT * FROM Login WHERE phoneNumber = %s"%(phoneNumber)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		cursor.close()
		connection.close()
		if result:
			return True
		else:
			return False
	except Exception as e:
		print (e)
		return False

def isHost(name):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Host!")
		sql = "SELECT * FROM Store WHERE name = '%s'"%(name)
		print(sql)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		cursor.close()
		connection.close()
		if result:
			return True
		else:
			return False
	except Exception as e:
		print (e)
		return False

def isCategory(idCategory):
	try:
		connection = db_config.getConnection()
		print("Connection Successful Categories!")
		sql = "SELECT * FROM Categories WHERE idCategories = %d"%(idCategory)
		print(sql)
		cursor = connection.cursor()
		result = cursor.execute(sql)
		cursor.close()
		connection.close()
		if result:
			return True
		else:
			return False
	except Exception as e:
		print (e)
		return False

def userToHost(phoneNumber):
	try:
		connection = db_config.getConnection()
		print("Connection Successful User!")
		sql = "UPDATE Users SET isHost = %d WHERE phoneNumber = %s"%(1, phoneNumber)
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

def updateUserAddress(user):
	try:
		idUser = getKey(user)
		connection = db_config.getConnection()
		print("Connection Successful User Address!")
		sql = "UPDATE UserAddresses SET isSelected = %d WHERE idUsers = %d"%(0, idUser)
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.commit()
		cursor.close()
		connection.close()
		return True
	except Exception as e:
		print (e)
		return False

import random
import time
from datetime import datetime, date, time, timedelta
from math import cos, sqrt, radians, sin, atan2
from geopy.distance import geodesic

import querys
import model

def create_pin():
	pin = random.randint(999, 9999)
	return pin

def getDateTime():
	return datetime.now()

def strToDate(val):
	res = datetime.strptime(val, '%d-%m-%Y')
	return res

def getTimeExpiration():
	now = datetime.now()
	now_plus_10 = now + timedelta(minutes = 15)
	return now_plus_10

def verifyExpiration(dateExp):
	if datetime.now() < dateExp:
		return False
	else:
		return True

def validatePin(pin, phoneNumber):
	date = querys.getDatePin(phoneNumber)
	if verifyExpiration(date):
		return False
	else:
		pinValidate = querys.getPin(phoneNumber)
		if pin == pinValidate:
			return True
		else:
			return False

def saveHost(phoneNumber, store, address, schedule, tags):
	if querys.saveStore(store, phoneNumber):
		keyUser = querys.getKey(phoneNumber)
		keyStore = querys.getKeyStore(keyUser, store.name)
		if querys.saveAddress(address, keyStore) and querys.saveSchedule(schedule, keyStore) and querys.saveTags(tags, keyStore) and querys.userToHost(phoneNumber):
			return True
		else:
			return False
	else:
		return False

def saveUserAddress(userAddress, phoneNumber):
	if querys.updateUserAddress(phoneNumber) and querys.saveUserAddress(userAddress, phoneNumber):
		return True
	else:
		return False

def getDistance(lat1, lon1, lat2, lon2):
	pointA = (lat1, lon1)
	pointB = (lat2, lon2)
	print("here")
	print(pointA)
	print(pointB)
	distan = geodesic(pointA, pointB).km
	return distan

def closest(lat, lng, idCategories):
	data = querys.getStoresByCategory(idCategories)
	for row in data:
		row['distance'] = getDistance(lat,lng,row['storeAddress']['lat'],row['storeAddress']['lng'])
	stores = sorted(data, key=lambda k: k['distance'], reverse=False)
	return stores

def searchByText(text):
	return querys.getStores(text)
	



		



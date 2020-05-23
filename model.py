
class User(object):
	phoneNumber = ""
	name = ""
	lastName = ""
	birthdate = ""
	email = ""
	password = ""
	isHost = 0

	def __init__(self, phoneNumber, name, lastName, birthdate, email, isHost, password):
		self.phoneNumber = phoneNumber
		self.name = str(name)
		self.lastName = lastName
		self.birthdate = birthdate
		self.email = str(email)
		self.password = password
		self.isHost = isHost

	def validate_values(self):
		if not self.name or not self.lastName or not self.password or not self.email:
			return False
		else:
			return True

class Store(object):
	name = ""
	description = ""
	email = ""
	contact_phone = ""
	extra_phone = ""
	website = ""
	active = ""

	def __init__(self, name, description, email, contact_phone, extra_phone, website, active):
		self.name = name
		self.description = description
		self.email = email
		self.contact_phone = contact_phone
		self.extra_phone = extra_phone
		self.website = website
		self.active = active

	def validate_values(self):
		if not self.name or not self.description or not self.email or not self.contact_phone or not self.extra_phone or not self.active:
			print("store")
			return False
		else:
			return True

class StoreAddress(object):
	name = ""
	lat = 0
	lng = 0
	street = ""
	municipality = ""
	state = ""
	codezip =""
	country = ""

	def __init__(self, name, lat, lng, street, municipality, state, codezip, country):
		self.name = name
		self.lat = lat
		self.lng = lng
		self.street = street
		self.municipality = municipality
		self.state = state
		self.codezip = codezip
		self.country = country

	def validate_values(self):
		if not self.name or not self.lat or not self.lng or not self.street or not self.state or not self.country:
			return False
		else:
			return True

class StoreSchedule(object):
	monday = ""
	tuesday = ""
	wednesday = ""
	thursday = ""
	friday = ""
	saturday = ""
	sunday = ""

	def __init__(self, monday, tuesday, wednesday, thursday, friday, saturday, sunday):
		self.monday = monday
		self.tuesday = tuesday
		self.wednesday = wednesday
		self.thursday = thursday
		self.friday = friday
		self.saturday = saturday
		self.sunday = sunday

	def validate_values(self):
		if not self.monday or not self.tuesday or not self.wednesday or not self.thursday or not self.friday or not self.saturday or not self.sunday:
			return False
		else:
			return True

class StoreTags(object):
	tags = ""
	idCategories = ""

	def __init__(self, tags, idCategories):
		self.tags = tags
		self.idCategories = idCategories

	def validate_values(self):
		if not self.idCategories:
			return False
		else:
			return True

class StoreDistance(object):
	distance = 0
	storeJson = any

	def __init__(self, distance, storeJson):
		self.distance = distance
		self.storeJson = storeJson

class UserAddresses(object):
	name = ""
	lat = 0
	lng = 0
	street = ""
	number = ""
	suburb = ""
	municipality = ""
	state = ""
	codezip = ""
	isSelected = 1

	def validate_values(self):
		if not self.name or not self.lat or not self.lng or not self.street:
			return False
		else:
			return True

	def __init__(self, name, lat, lng, street, number, suburb, municipality, state, codezip, isSelected):
		self.name = name
		self.lat = lat
		self.lng = lng
		self.street = street
		self.number = number
		self.suburb = suburb
		self.municipality = municipality
		self.state = state
		self.codezip = codezip
		self.isSelected = isSelected


def getValuesFromStore(json):
	store = Store(json['name'], json['description'], json['email'], json['contact_phone'], json['extra_phone'], json['website'], 1)
	return store

def getValuesFromSchedule(addJson):
	schedule = StoreSchedule(addJson['schedule']['monday'], addJson['schedule']['tuesday'], addJson['schedule']['wednesday'], addJson['schedule']['thursday'], addJson['schedule']['friday'], addJson['schedule']['saturday'], addJson['schedule']['sunday'])
	return schedule

def getValuesFromAddress(addJson):
	storeAddress = StoreAddress(addJson['address']['name'], addJson['address']['lat'], addJson['address']['lng'], addJson['address']['street'], addJson['address']['municipality'], addJson['address']['state'], addJson['address']['codezip'], addJson['address']['country'])
	return storeAddress

def getValuesFromTags(addJson):
	storeTags = StoreTags(addJson['storeTags']['tags'], addJson['storeTags']['idCategories'])
	return storeTags

def getValuesFromUserAddress(addJson):
	userAddress = UserAddresses(addJson['name'], addJson['lat'], addJson['lng'], addJson['street'], addJson['number'], addJson['suburb'], addJson['municipality'], addJson['state'], addJson['codezip'], 1)
	return userAddress

def createJsonStore(rows):
	array_categ = []
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

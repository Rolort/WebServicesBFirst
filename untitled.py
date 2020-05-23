"""
  Web Services to get the stores by search
    ---
       tags:
         - UserAddress
       schemes:
         - http
       parameters:
         - in: header
           name: device
           type: string
           description: The OS of the device
           required: true
           example: iOS
         - in: header
           name: ip
           type: string
           description: The IP of the device
           required: true
           example: 127.0.0.1
         - in: header
           name: user
           type: string
           description: The phoneNumber of User (Must be registered)
           required: true
           example: 5543061607
           - in: path
           name: name
           type: string
           description: Name of Address
           required: true
           example: Casa
         - in: path
           name: lat
           type: float
           description: The latitude of User
           required: true
           example: 19.4111532
         - in: path
           name: lng
           type: float
           description: The longitude of User
           required: true
           example: -99.177838
         - in: path
           name: street
           type: string
           description: The street of Address
           required: false
           example: Privada San Carlos
         - in: path
           name: number
           type: int
           description: The number of Address
           required: false
           example: 1
         - in: path
           name: suburb
           type: string
           description: The suburb of Address
           required: false
           example: Condesa
         - in: path
           name: municipality
           type: string
           description: The municipality of Address
           required: false
           example: Venustiano Carranza
         - in: path
           name: state
           type: string
           description: The state of Address
           required: false
           example: Santa Cruz
         - in: path
           name: codezip
           type: string
           description: The codezip of Address
           required: false
           example: 01234
       produces:
         - application/json
       consumes:
         - application/json
       responses:
         200:
           description: Successful!
           
  """




#Method to Get Stores
@app.route('/addAddress', methods=['POST'])
def userAddress():
  try:
    jso = json.dumps(request.json)
    logs.request = str(request) + jso + str(request.headers)
    logs.device = request.headers.get('device')
    logs.ip = request.headers.get('ip')
    logs.getRequest()
    if not logs.device or not logs.ip:
      return responses.request_error(4)
    _phoneNumber = request.headers.get('user')
    _json = request.json
    userAddress = model.getValuesFromUserAddress(_json)
    
    if request.method == 'POST' and querys.isUser(_phoneNumber):
      if process.saveUserAddress(userAddress, phoneNumber):
        return responses.UserAddress_response()
      else:
        return responses.database_error()
    else:
      if request.method != 'GET':
        return responses.request_error(3)
      elif not querys.isUser(_phoneNumber):
        return responses.user_notfound()
      else:
        return responses.request_error(100)
  except Exception as e:
    print (e)
    print (e.args[0])
    if not e.args[0].isdigit():
      return responses.catalog_error(0)
    else:
      return responses.catalog_error(e.args[0])
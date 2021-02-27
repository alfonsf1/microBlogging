#USER SERVICE
@app.route("/createUser", methods=['POST'])
def createUser(username, email, password):
    #Registers a new user account. Returns true if username i

    pass 

@app.route("/checkPassword", methods=['GET'])
def checkPassword(username, password):
    #Returns true if the password parameter matches the password stored for the username.
    pass

@app.route("/addFollower", methods=['PUT'])
def addFollower(username, usernameToFollow):
    #Start following a new user.
    pass


@app.route("/removeFollower", methods=['PUT'])
def removeFollower(username, usernameToRemove):
    #Stop following a user.
    pass
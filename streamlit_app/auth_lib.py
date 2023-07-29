import db
import bcrypt

# When a user creates an account, collecting their data and inserting it into the User database

def createUser(username, email, password, profilePicture):
    try:
        password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
        resp = db.query('INSERT INTO User (username, email, password, profilePicture) VALUES(%s, %s, %s, %s)', (username, email, password, profilePicture), insert=True)
        return findUser(username)
    except Exception as e:
        print(e)
        return []


#Passing a username and finding the user in the User table, and returns the user if the username exists in the table
# Used to ensure a user attempting to login is an exisitng user

def findUser(username):
    try:
        resp = db.query(f"SELECT * FROM User WHERE username = %s", (username))[0] # since unique
        user = {
            'id': resp[0],
            'username': resp[1],
            'email': resp[2],
            'password': resp[3],
            'profilePicture': resp[4]
        }
        return user;
    except Exception as e:
        print(e)
        return []
    

# If the username has been found a user attempting to login must enter the password, the inputed password is then checked against the password
# saved in the User table to ensure the user has entered the correct password

def validatePassword(username, inputPassword):
    try:
        # find hashed password in db
        resp = db.query(f"SELECT password FROM User WHERE username = %s", (username))[0][0]
        bytes_formatted = (str(bytes(resp)).split("'")[1].split("'")[0]).encode('UTF-8')
        # if not(resp):
        #     return []
        if bcrypt.checkpw(inputPassword.encode('UTF-8'), bytes_formatted):
            return findUser(username)
    except Exception as e:
        print(e)
        return []
    return []



# If a user wants to update their password, they must first validate their password (enter their current password), then enter a new 
# password and the User table is updated  to have the updated password for the user

def updatePassword(username, inputPassword, newPassword):
    try:
        if(validatePassword(username, inputPassword)):
            resp = db.query(f"UPDATE User SET password = %s WHERE username = %s", (newPassword, username))
        return result[0]
    except Exception as e:
        print(e)
        return []
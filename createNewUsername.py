
global createdNames
createdNames = []

def exsitingUsers(name):
    if name in createdNames:
        return True
def unquieName(name,number=0):
    if exsitingUsers(name+str(number)):
        return unquieName(name, number+1)
    else:
        return name+str(number)

def createUsername():
    firstname = input("what is your first name?: ")[0]
    username = input("what is your lastname?: ")+firstname
    if exsitingUsers(username):
        user = unquieName(username)
    else:
        user = username
    createdNames.append(user)
    print(f"you got the username {user}")

while True:
    ask = input("do you want to continue?: ")
    if ask:
        break
    createUsername()

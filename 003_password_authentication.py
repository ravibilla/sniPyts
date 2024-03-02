import getpass

database = {"ravi.billa": "123456", "billa.ravi": "654321"}
username = input("Enter your username: ")

if username in database.keys():
    password = getpass.getpass("Enter your password: ")
    
    for user, pwd in database.items():
         if username == user:
                while password != database.get(user):
                    password = getpass.getpass("Incorrect password! \nEnter your password again: ")
                break
    print("User verfied !")
else:
    print("User doesn't exist!")
#This application serves as a login interface.
import getpass 
from pathlib import Path

ufilepath = Path("./user_info.txt")
users = {}
   
def writer(user,password):
    file = open(ufilepath, 'a')
    file.write(user + ',' + password+'\n')
    file.close


def reader(dict):
    file = open(ufilepath, 'r')
    for x in file:
        user, passwords = x.split(',')
        dict[user] = passwords

    
reader(users)
print(users)

index = input("\nRegister or log in? ").capitalize()
access = False



if index == "Register":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    writer(user,password)
    print("Registration Successful! Try to Log in.")
    
    

elif index == "Log in":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if (user in users.keys()) and (password in users.values()):
        print("Access granted, welcome!")
        
    else:
        print("\n\nUsername and password non existent or wrong\nYou need to register.\n")

else:
    print("\nWrong input, try again\n")
# This application serves as a login interface.
import getpass 

users = {}


def writer(username, passwords):
    with open("user_info.txt", 'a') as file:
        file.write(username + ',' + passwords+"\n")


def reader(dic):
    with open("user_info.txt", 'r') as file:
        for x in file:
            username, passwords = x.split(',')
            passwords = passwords.strip(' \n')
            dic[user] = passwords


reader(users)


index = input("\nRegister or log in? ").capitalize()

if index == "Register":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    writer(user, password)
    print("Registration Successful! Try to Log in.")

elif index == "Log in" or index == "Login":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if (user in users.keys()) and (password in users.values()):
        print("Access granted, welcome!")
        
    else:
        print("\n\nUsername and password non existent or wrong\nYou need to register.\n")

else:
    print("\nWrong input, try again\n")

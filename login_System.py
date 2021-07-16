#This application serves as a login interface.
import getpass 

users = {}
   
def writer(user,password):
    file = open("/user_info.txt", 'a')
    file.write(user + ',' + password+"\n")
    file.close()

def reader(dict):
    file = open("/user_info.txt", 'r')
    for x in file:
        user, passwords = x.split(',')
        passwords = passwords.strip(' \n')
        dict[user] = passwords
    file.close()

reader(users)

index = input("\nRegister or log in? ").capitalize()

if index == "Register":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    writer(user,password)
    print("Registration Successful! Try to Log in.")
    
elif (index == "Log in" or index == "Login"):
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if (user in users.keys()) and (password in users.values()):
        print("Access granted, welcome!")
        
    else:
        print("\n\nUsername and password non existent or wrong\nYou need to register.\n")

else:
    print("\nWrong input, try again\n")

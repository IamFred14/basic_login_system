#This application serves as a login interface.
import getpass 
from pathlib import Path 

ufilepath = Path("./users.txt")
pfilepath = Path("./passwords.txt")
users = set()
passwords = set()



def read_user(users):
    open_ufile = open(ufilepath, 'r')
    users = set(str(open_ufile))

def read_pass(passwords):
    open_pfile = open(pfilepath, 'r')
    passwords = set(str(open_pfile))

def write_users():
    close_ufile = open(ufilepath, 'w')
    for val in users:
        close_ufile.write(val)

def write_pass():
    close_pfile = open(pfilepath, 'w')
    for val in passwords:
        close_pfile.write(val) 
 
def get_user():
    uname = input("\nInput new Username: ")
    previous = len(users)
    users.add(uname)
    if previous < len(users):
        print("\nUsername accepted.")
    else:
        print("\nUsername already in use.")
    return 1    
            
def get_pass():
    passw = getpass.getpass("\nInput new Password:")
    passwords.add(passw)
    print("\nThank you for your time!\n")

def goto(line):
    global lineNumber
    lineNumber = line


read_user(users)
read_pass(passwords)

index = input("\nSign up or sign in? ")

if index == "Sign up" or index == "sign up":
    if get_user() == 1:
        goto(54)
    else:
        pass
    get_pass()
    write_users()
    write_pass()
    
else:
    access = False
    while access == False : 
        uname = input("Username: ")
        for x in users:
            if uname == x :
                print("Username accepted.")
            else:
                print("Username not on the list.")
                access = True

        if access == True :
            continue
        else:
            passw = getpass.getpass("Password: ")
            for x in passwords:
                if passw == x :
                    access = True
                    print("Access granted!")
                else:

                    access = False
                    print("Access denied. Try again...")


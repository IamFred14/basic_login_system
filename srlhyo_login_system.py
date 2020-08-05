#This application serves as a login interface.
import getpass
from pathlib import Path
import csv
ufilepath = Path("./users.csv")
pfilepath = Path("./passwords.csv")
users = []
passwords = []
def read_users_csv():
    open_users = open(ufilepath, newline='')
    csvfile = csv.reader(open_users)
    users = list(csvfile)
def read_password_csv():
    open_pass = open(pfilepath, newline='')
    csvfile1 = csv.reader(open_pass)
    passwords = list(csvfile1)
def write_users_csv():
    csvfile = open(ufilepath,'w')
    writer = csv.writer(csvfile)
    writer.writerow(users) 
def write_passwords_csv():
    csvfile1 = open(pfilepath,'w')
    writer = csv.writer(csvfile1)
    writer.writerow(passwords) 
def get_user():
    uname = input("Input new Username: ")
    for x in users:
        if uname == x: 
            print("Username already in use!")
            break    
    else:
        print("Username accepted!")
        users.append(uname)
def get_password():
    passw = getpass.getpass("Input new Password:")
    passwords.append(passw)
index = input("Sign up or sign in? ")
if index == "Sign up" or index == "sign up":
    get_user()
    get_password()
    write_users_csv()
    write_passwords_csv()
else:
    access = False
    read_users_csv()
    read_password_csv()
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

#This application serves as a login interface.
import getpass
from pathlib import Path
import csv

ufilepath = Path("./users.csv")
pfilepath = Path("./passwords.csv")
users = []
passwords = []

def readUserCSV():
    openUsers = open(ufilepath, newline='')
    csvfile = csv.reader(openUsers)
    users = list(csvfile)

def readPassCSV():
    openPass = open(pfilepath, newline='')
    csvfile1 = csv.reader(openPass)
    passwords = list(csvfile1)

def writeUsersCSV():
    csvfile = open(ufilepath,'w')
    writer = csv.writer(csvfile)
    for val in users:
        writer.writerow(val) 

def writePasswordCSV():
    csvfile1 = open(pfilepath,'w')
    writer = csv.writer(csvfile1)
    for val in passwords:
        writer.writerow(val.strip()) 
 
def get_User():
    uname = input("Input new Username: ")
    for x in users:
        if uname == x: 
            print("Username already in use!")
            exit    
        else:
            print("Username accepted!")
            users.append(uname)
            
def get_Pass():
    passw = getpass.getpass("Input new Password:")
    passwords.append(passw)

index = input("Sign up or sign in? ")

if index == "Sign up" or index == "sign up":
    get_User()
    get_Pass()
    writeUsersCSV()
    writePasswordCSV()
    
else:
    access = False
    readUserCSV()
    readPassCSV()
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


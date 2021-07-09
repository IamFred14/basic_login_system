#This application serves as a login interface.
import getpass 
from pathlib import Path 
import csv
import os

ufilepath = Path("./users.csv")
pfilepath = Path("./passwords.csv")
users = []
passwords = []


def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def read_user(users):
    open_users = open(ufilepath, newline='')
    csv_user = csv.reader(open_users)
    users = list(csv_user)

def read_pass(passwords):
    open_pass = open(pfilepath, newline='')
    csv_pass = csv.reader(open_pass)
    passwords = list(csv_pass)

def write_users():
    csvfile = open(ufilepath,'w')
    writer = csv.writer(csvfile)
    writer.writerow(users) 

def write_pass():
    csvfile = open(pfilepath,'w')
    writer = csv.writer(csvfile)
    writer.writerow(passwords) 
 
def get_user():
    while True:
        uname = input("\nInput new Username: ")
        if uname in users:
            print("\nUsername already in use!\n")
        else: 
            users.append(uname)
            print("\nUsername not in use!\n")
            break
            

            
def get_pass():
    passw = getpass.getpass("\nInput new Password:")
    passwords.append(passw)
    print("\nThank you for your time!\n")

def goto(line):
    global lineNumber
    lineNumber = line


read_user(users)
read_pass(passwords)
clear()

index = input("\nSign up or sign in? ")

global_access = False
while global_access == False:
 if index == "Sign up" or index == "sign up":
     get_user()
     get_pass()
     write_users()
     write_pass()
     global_access = True
    
 elif index == "Sign in" or index == "sign in":
     user_access = False
     while user_access == False: 
       uname = input("Username: ")
       if uname in users:
          print("\nUsername accepted!\n")
          user_access = True
      
       else:
          user_access = False
          print("\nUsername not on the list. Try again.\n")

     pass_access = False
     while pass_access == False:	  
            
        passw = getpass.getpass("Password: ")
        if passw in passwords:
          pass_access = True
          print("\nAccess granted!\nWelcome back!\n")
  	else:
	  pass_access = False
	  print("\nAccess denied. Try again...\n")
global_access = True
		
  else:
     print("\nOption not valid. Try again\n")
     global_access = False


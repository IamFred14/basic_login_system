#This application serves as a login interface.
import getpass 
from pathlib import Path

# make sure that you understand what each line is doing. For exemple:
# Is Path required for this situation? It may not...
ufilepath = Path("./user_info.txt") # anyway, it might be that Path ensures consistency across different operating systems.
# I don't know, but it's worth it to read about it and even play a bit with the code to see if you get different results
users = {}
   
def writer(user,password): # Why not "WITH OPEN??". Look up for that and se what is the difference. Open is not wrong but WITH OPEN might be even better!
    # have you thought about it?
    file = open(ufilepath, 'a')
    file.write(user + ',' + password+"\n")
    file.close()


def reader(dict):
    file = open(ufilepath, 'r')
    for x in file:
        user, passwords = x.split(',') # why user and passwords? can the same user store multiple passwords? If not, than password makes a lot more sense
        passwords = passwords.strip(' \n')
        dict[user] = passwords
    file.close()

    
reader(users)
print(users) # I know you know but make sure you don't print unneeded variables before pushing the code to Main.

index = input("\nRegister or log in? ").capitalize()

# too many empty spaces around here... 

if index == "Register":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    writer(user,password)
    print("Registration Successful! Try to Log in.")
    
# and here too...   In case of doubt, just quickly check out the PEP8 coding style guidelines. You don't need to read the all thing, only what it applies for 
# your case...    

elif (index == "Log in" or index == "Login"):
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if (user in users.keys()) and (password in users.values()):
        print("Access granted, welcome!")
        
    else:
        print("\n\nUsername and password non existent or wrong\nYou need to register.\n") # I would change the text slightly. The username or the password
        # can be right. That will give the user a bit more clue. You get me? EX: my username can be right, even though the password is wrong. Then I only have to
        # focus on the password.

else:
    print("\nWrong input, try again\n")

##### Well Done! I like most of it! This login system is way better than the first one. Super evolution! Keep up with the good work!
# SOME TIPS:
# Don't be afraid to spend some time readind documentation on any pythonm module you decide to use. You will learn what are the funcionalities given to you to
# make your life even esiers

# Also, try to have fun while coding. You'll be surprised how good you are! Don't take it seriously as that prevents you from learning properly. You know
# when you're playing a game and you try this and that to see what results you get, even if you die? And usually along the way you discover screts and so on?
# Exactly! With code is exactly the same. Don't limit yourself to video tutorials. Read 20%, 5% video and 75% playing with code; have fun.s
import random
import os.path

def generate(o, symbsbase):
    password = []
    ans = "ooo"
    ans2 = "ooo"
    passname = "/"
    while ans != "no" and ans != "yes":
        ans = str(input("Do you want to save your password to a text file? The password will not be ecnrypted so be careful where you move it/backup it.\nyes/no\n"))
    if ans == "yes":
        if os.path.isfile("Decrypted Password Storage.txt"):
            savepass = open("Decrypted Password Storage.txt", "a")
        else:
            savepass = open("Decrypted Password Storage.txt", "w+")
        while ans2 != "no" and ans2 != "yes":
            ans2 = str(input("Do you want to give the password a name?\nyes/no\n"))
        if ans2 == "yes":
            passname = str(input("How do you want to name your password?\n"))
            savepass.write ("\nName: " + passname + "\nPassword: ")
    print("\n-------------------------------------\nYour Password is: ", end= '') 
    for i in range (0, o):
        a = random.randint(0, len(symbsbase)-1)
        password.append(symbsbase[a]) 
    for i in range (0, len(password)):
        print(password[i], end ='')
        if ans == "yes":
            savepass.write(password[i])
    print ("\n-------------------------------------\n\n")
    if ans == "yes":
        savepass.write("\n")
        savepass.close()

def ask():
    o = 3
    numofsel = 0
    symbsbase = []
    symbslower = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbsupper = ['A', 'B' , 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbs = ['!', '#', '$', '&', '*', '(', ')', '-', '_', '=', '+']
    
    while o < 4:
        o = int(input("Give the length of your desired password:\n"))
    reps = 0 
    while numofsel == 0:
        if reps > 0:
            print("You should choose atleast something to include in your selection!\n")
        ans = "ooo"
        while ans.lower() != "no" and ans.lower() != "yes":
            ans = str(input("Do you want to include uppercase letters?\nyes/no\n"))
        if ans == "yes":
            numofsel += 1
            for i in range (0, len(symbsupper)):
                symbsbase.append(symbsupper[i])
        
        ans = "ooo"
        while ans.lower() != "no" and ans.lower() != "yes":
            ans = str(input("Do you want to include lowercase letters?\nyes/no\n"))
        if ans == "yes":
            numofsel += 1
            for i in range (0, len(symbslower)):
                symbsbase.append(symbslower[i])
        
        ans = "ooo"
        while ans.lower() != "no" and ans.lower() != "yes":
            ans = str(input("Do you want to include numbers?\nyes/no\n"))
        if ans == "yes":
            numofsel += 1
            for i in range (0, len(nums)):
                symbsbase.append(nums[i])
        
        ans = "ooo"
        while ans.lower() != "no" and ans.lower() != "yes":
            ans = str(input("Do you want to include symbols (!, #, $, %, &, *, ...)?\nyes/no\n"))
        if ans.lower() == "yes":
            numofsel += 1
            for i in range (0, len(symbs)):
                symbsbase.append(symbs[i])
        reps += 1
        
    generate(o, symbsbase)

print ("Hey! Welcome to our password generator, made by inf2021198 and inf2021221")
aend = "no"
while aend.lower() == "no" and aend.lower() != "yes":
    ask()
    aend = "ooo"
    while aend.lower() != "no" and aend.lower() != "yes":
        aend = str(input("Do you want to stop the process of password generation?\nyes/no\n"))






"""
--------------------------------------------------
Borrowed Code from: 

None

--------------------------------------------------

In development by inf2021221 & inf2021198 for our university project at IONIO 
University of Informatics

Link to the Github project:
    https://github.com/maxiikk/PasswordGenerator

Last edit made at 27/2/2022 18:14
"""

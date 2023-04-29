'''import re

#Sanket2020
unm=input("Enter Username:")

unm_pattern="^[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,unm)

if x: #true
    print("Username is valid!")
else:
    print("Error! Inavlid Username")'''

import re
import getpass

#sanket2020@gmail.com
Email = False
while Email == False :
    email=input("Enter an email:")

    email_ptrn="^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$"

    x=re.findall(email_ptrn,email)

    if x:
        print("Valid Email")
        Email = True
    else:
        print("Error! Inavlid Email")

x = False

while x == False :

    pas = getpass.getpass('Password :-')
    if re.findall('[A-Z]',pas) and re.findall('[a-z]',pas) and re.findall('[\W]',pas) and re.findall('[0-9]',pas) :

        print ("Please Enter to confirm password")
        x = True
    else :

        print ("please enter strong password")

y =False
if x == True :

    while y == False:
        pas1 = getpass.getpass('confirm Password :- ')

        if pas == pas1 :

            print ("Your password is saved")
            y = True
        else :

            print ("Please enter same passsword ")


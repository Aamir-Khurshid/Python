age = int(input("Enter your age: "))
print("Your age is: ",age)
if(age>18):                        # Condition true if will execute
    print("So,You can drive")
else:                              # Condition false else will execute
    print("So,You cannot drive")


# To check multiple condition we use elif
 
if(age == 0):                               
    print("YOU ARE BORN CONGO")
elif(age<=19):
    print("YOU ARE A TEENAGER")
elif(age<=28):
    print("YOU ARE IN MATURING PHASE")    
elif(age<=37):
    print("YOU ARE MATURE")
elif(age<=50):    
    print("YOU ARE GETTING OLDER")
else:
    print("YOU ARE OLD NOW ")


# Nested statements

if (age<=30):
    if(age>=19):
        print("You are not a teenager now")
    elif(age<=18):
        print("You are a teenager") 
           
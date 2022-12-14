# Used to find time 

import time
timenow = (time.strftime('%H:%M:%S'))
print(timenow)
timehour = int(time.strftime('%H'))
timemin = int(time.strftime('%M'))
timesec = int(time.strftime('%S'))

# Make a code capable of greeting Good Morning,Good Afternoon and Good Evening

if(timehour>5 and timehour<12  ):
    print("Good morning")
elif(timehour>=12 and timehour<6  ):
    print("Good afternoon") 
else:
    print("Good Evening")       
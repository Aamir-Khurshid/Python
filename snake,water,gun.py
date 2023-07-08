import random 
li = [-1,0,1]
computer = random.choice(li)
user = int(input("Enter : -1(snake), 0(water), 1(gun) : "))
comp = [computer,user]
win = [[0,-1],[-1,1],[1,0]]
draw = [[0,0],[-1,-1],[1,1]]
loose = [[0,1],[-1,0],[1,-1]]
for i in win :
    if(i==comp):
        print("The player win")
        print(f"The system choose {computer}")
for i in draw :
    if(i==comp):
        print("Draw")
        print(f"The system choose {computer}")
for i in loose :
    if(i==comp):
        print("The player loose")        
        print(f"The system choose {computer}")

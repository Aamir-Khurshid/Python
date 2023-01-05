# Create a KBC program

list = [
    ["Who discovered java?","Me","You","By Itself","Noone","a"],
    ["Who is the owner of apple?","You","Noone","Me","Unknown","c"],
    ["Who is the owner of flipkart?","You","Noone","Unknown","Me","d"],
    ["Who is the owner of amazon?","Me","Noone","You","Unknown","a"],
    ["Who is the owner of myntra?","You","Me","Noone","Unknown","b"],
    ["Who is the owner of yahoo?","You","Noone","Me","Unknown","c"],
    ["Who is the owner of c language?","You","Noone","Me","Unknown","c"],
    ["Who is the owner of python?","You","Noone","Me","Unknown","c"],
    ["Who is the owner of youtube?","You","Noone","Unknown","Me","d"],
    ["Who is the owner of gaana?","Me","Noone","You","Unknown","a"],
    ["Who is the owner of spotify?","You","Me","Noone","Unknown","b"],
    ["Who is the owner of among us?","You","Noone","Me","Unknown","c"],
    ["Who is the owner of adidas?","You","Noone","Unknown","Me","d"],
    ["Who is the owner of google?","Me","Noone","You","Unknown","a"],
    ["Who is the owner of microsoft?","You","Me","Noone","Unknown","b"]
    ]

level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0
for i in range(0,len(list)):
    question = list[i]
    print(f"This question is for amount {level[i]}\n")
    print(f"{int(i+1)}. {question[0]}\n")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}\n")
    useranswer = (input("Select your option.( 1 to 4) : "))
    if(useranswer == question[5]):
        print(f"You won {level[i]}")
        if(i>=4 and i<9):
            print(f"You have {level[4]} , even if you give wrong answer now.")
        elif(i>=9 and i<13):
            print(f"You have {level[9]} , even if you give wrong answer now.")
        elif(i>=13):
            print(f"You have {level[13]} , even if you give wrong answer now.")    
        elif(i==14):
            print(f"You have won the bumper amount of {level[14]}")
        print("\n")        
    else:
        print(f"Wrong Answer,The correct answer is {question[5]}")
        if(i>=4 and i<9):
            print(f"You have {level[4]}.")
        elif(i>=9 and i<13):
            print(f"You have {level[9]}.")
        elif(i>=13):
            print(f"You have {level[13]}.")    
        elif(i==14):
            print(f"You have won the bumper amount of {level[14]}")
        print("\n")  
        break    
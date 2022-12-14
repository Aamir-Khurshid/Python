# for loop to print even number with a different way

x = int(input("Enter the number: "))
for i in range(2,x+1,2):
    print(i)

# nested loop for fun 

fruits = ["Apple","Mango","Banana","Grapes"]    
for fruit in fruits:
    print(fruit)
    for alpha in fruit:
        print(alpha)
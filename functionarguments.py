def average(a=3, b =4):
    print("The average " , (a+b)/2)

average(4,5)
average(a=6)  # b  have default value 4
average(b=4)  # a has default value 3

average(b=9,a=3)             # keyword argument  - order dont need to be maintained it will assign with the argument

def sum(a,b):              # a and b here are required argument as their value is required      
    print("The sum is " , a+b)

sum(4,5)
#sum(4)          # It will throw a  error 


def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    print("The average of numbers " , sum/len(numbers))    
avg(4,5,6)    
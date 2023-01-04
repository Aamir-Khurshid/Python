# Using Recursion find:-

# 1. Factorial 

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 

n = int(input("Enter the number "))          
print(factorial(n))

# 2. Fibonacci  

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
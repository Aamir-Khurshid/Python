a = "1"
b = "2" 
print(a+b)   # output will be 12

a = "1"  # As 1 is a valid int so it can be converted but "Aamir" cant be converted to integer
b = "2"
print(int(a) + int(b)) # output will be 3 (explicit h ye )

a = "1"
b = "2" 
print(a*b)   #error

a = "1"  
b = "2"
print(int(a) * int(b))

a = "1"
b = "2" 
print(a/b)   #error

a = "1"  
b = "2"
print(int(a) / int(b))

a = "1"
b = "2" 
print(a**b)   #error

a = "1"  
b = "2"
print(int(a) ** int(b))

a = "1"
b = "2" 
print(a-b)   #error

a = "1"  
b = "2"
print(int(a) - int(b))
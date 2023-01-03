l= [1,4,3,5,4,6]
print(l)
print("\n")

# Here you think there will be only change in m but it will change l also 
m = l
m[0] = 0
print(m)
print(l)
print("\n")    

# To protect the list l from changing you should use copy

m = l.copy()
m[1] = 1
print(m)
print(l)
print("\n")

# To insert a value at a particular index use .insert(index,value)

l.insert(2,6)
print(l)
print("\n")

# To sort a list we can use sort()

l.sort()                  # For increasing order
print(l)              
l.sort(reverse=True)      # For decreasing order
print(l)   
print("\n")

# Add element at the end using append

l.append(9)
print(l)
print("\n") 

# Using extend() you can add two list 
# If you dont want to change the list so create a new list

l.extend(m)  # Here list "m" will become a part of list "l"
print(l)
print("\n")


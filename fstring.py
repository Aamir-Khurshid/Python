# Using fstring my friend 

l = "Hey My name is {0} and i am from {1}"
name = "Aamir"
place = "India"
 
print(l.format(name,place))       # This is the old and confusing way
print("\n")

#F-string
print(f"Hey My name is {name} and i am from {place}")
print("\n")

# can be used to fix the number of decimal values

n = 2.34556
print(f"{n:.2f}")
print("\n")
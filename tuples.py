tup = (1,5,6,5,63,7)
# Tuple can't be changed

# to make a one element tuple use Syntax  tup = (1,)
# You can't write tup=(1) because if you dont write (,) it will be taken as int

print(type(tup)) 
print(len(tup))

# Can make a new tuple to make changes
tup2 = tup[1:3]
print(tup2)


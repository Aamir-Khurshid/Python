s1 = {1,3,4,5,6,1}
s2 = {7,7,8,9,6,0}

print(s1.union(s2))   # Union - Combining two set without repeating same values

print(s1.intersection(s2))   # Intersection - Common between two sets


# Use update() to update a set , Can also be used to add multiple values

states ={'Delhi', 'Bihar', 'Bengal', 'Up'}
morestates = {"Goa","Assam"}
states.update(morestates)
print(states)

print(s1.isdisjoint(s2))  # True if nothing is common

state = {"Delhi","Bihar","Up"}   # add() is used to add a single value
state.add("Bengal")
print(state)

# If the value we want to remove is not present is set remove() will show erreo and stop the code
# But if discard() is used it will not raise a error

state.remove("Bengal")   # remove() is used to remove value from set
print(state)             # discard() can also be used at place of remove()

# pop() used to delete a random value
fruit = "HELLO"
print(len(fruit))  #  len() is used to print length of a string

print(fruit[0:2])
print(fruit[1:-3])
"""upperbound wil be taken but not lower bound will not be taken.
   like below example will mention -3 element but not -1 element. """
print(fruit[-3:-1])   

print(fruit[-4:-2])
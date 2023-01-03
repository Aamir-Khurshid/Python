# Docstring can also be print it will not be ignored by python

def cube(n):
    '''Take input and return the cube of input'''
    print(n**3)
cube(9)
print(cube.__doc__)
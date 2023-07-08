# Private modifier is used by  "__"
"""Cant be accessed directly but can be accessed indirectly
 _classname__attribute"""

class Aamir:
    def __init__(self):
        self.__age = 10  # Private Attribute
one = Aamir()
print(one._Aamir__age)  # Correct
print(one.__age)      # Incorrect

#Object Inspection

x = [1, 2]
print(dir(x))  #Tells about the methods that could be applied on the passed argument.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p = Person("Aamir",20)
print(p.__dict__)  #Will provide with all the attributes of the class.
print(help(Person))  #Provides with the documentation.

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Programmer(Employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

aamir = Programmer("AAMIR", "1", "Python")
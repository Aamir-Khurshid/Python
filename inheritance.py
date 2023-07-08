class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee : {self.id} is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("Python")

one = Employee("Aamir",21)
one.showDetails()
onion = Programmer("Aamir",21)
onion.showDetails()
onion.showLanguage()
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"My name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"my dance form is {self.dance}")


class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance


e1 = DancerEmployee("shivani", "Bhangra")
e1.show()
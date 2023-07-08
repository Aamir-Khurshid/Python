class Employee:
    companyname = "Socialsaks" # Class Variable - Same for the whole class.
    def __init__(self, name):
        self.name = name  # Instance Variable - Different for every instance.
    def showDetails(self):
        print(f"Name:{self.name} and company name is {self.companyname}")

emp = Employee("AAMIR")
emp.showDetails()
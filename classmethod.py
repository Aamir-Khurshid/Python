class Aamir:
    company = "Amazon"
    def show(self):
        print(f"My name is {self.name} and the company i work in is {self.company}")
    @classmethod # Can also change the class variable value.
    def changecompany(cls, newname):
        cls.company = newname
e1 = Aamir()
e1.name = "Aamir Khurshid"
e1.show()
e1.changecompany("Flipkart")
e1.show()
print(Aamir.company)


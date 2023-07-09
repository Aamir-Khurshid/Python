class Parent:
    def parent_method(self):
        print("Parent")

class Child(Parent):
    def parent_method(self):
        print("Aamir")
        super().parent_method()

    def child_method(self):
        print("Child")


f = Parent()
e = Child()
e.parent_method()






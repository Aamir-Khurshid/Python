class Employee:
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return "Hello"
    def __repr__(self):
        return "Hello Again"
    def __call__(self):
        print("You are using Employee Class Package")


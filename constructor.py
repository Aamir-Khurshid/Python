# Constructor is a special function . Return type - None
# def __init__(self,na,oc) 
# self is passed automatically so you need to pass only two arguments.

class hello:
    def __init__(self,na,oc): # Constructor
        print("Hey bro")
        self.name = na
        self.occ = oc
    def intro(self):
        print(f"Hey , My Name is {self.name}") 
a = hello("Aamir","owner")
a.intro()           

class employee:
    def __init__(self,n,o):
        print(f"Hey , {n} is a {o}")
a = employee("Aamir","Engineer")
b = employee("Aamirk","Engineer")
c = employee("Aamirkh","Engineer")
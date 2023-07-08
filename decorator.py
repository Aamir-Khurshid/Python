# decorators - Takes input in form of a function .
def greet(fx):
    def mfx(*args ,**kwargs):
        print("Hello")
        fx(*args ,**kwargs)
        print("Thanks ")
    return mfx


# For using decorators with function without any parameter.  
@greet
def name():
    print("Aam")
name()

@greet
def add(a,b):
    print(a+b)
# For using decorators with function with parameter.
add(1,0)
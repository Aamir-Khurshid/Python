# custom error
a = int(input("Eneter any value  between 6 and 10 "))
if(a<6 or a>10):
    raise ValueError("Value should be between 6 and 10")  # raise-keyword to raise a error

b = input("Enter a string")
if(b != "quit"):
    raise ValueError("Value entered is not quit")
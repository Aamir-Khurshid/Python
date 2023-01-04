a = input("Enter the number : ")
print(f"Multiplication Table of {a} is: ")
print("\n")
try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")        
except :
    print("Some errror occured")
    print("\n")
print("Suppose here is some important code , it could have been not executed if the above code has any error ")        

# You can use except more than one time with one try 
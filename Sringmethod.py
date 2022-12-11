aamir ="::::hello BRO:!!!!!"
aam =":::: !!!!!"

# New copy of aamir will be made to make a change as strings are immutable

print(aamir.upper()) # upper method convert to uppercase

print(aamir.lower()) # lower method convert to lowercase

print(aamir.rstrip("!")) # using rstrip method we could remove elements at last

print(aamir.rstrip(":")) # rstrip wont affect any leading symbols

print(aam.rstrip(":")) 

print(aamir.replace("BRO","Aamir")) # Replace method to replace element with other element

print(aamir.split(":")) # split method converts to list and wherever the passed symbol is found it will become a different element of the list


a="hello aAmir"
print(a.capitalize())  # capitalize()  will convert first element to Capital and rest will be converted to small

print(a.center(22))

print(a.count("aAmir"))  # Count() help to find the number of times a element is repeated


b = "aamir11"
print(b.endswith("1"))  # Endswith method will trell us about whether a string ends with the passed character or not

print(b.find("m"))   # find() will return the index of passed character if found else will return -1

print(b.index("m"))  # index() will return the index if found else stop the code

print(b.isalnum())  # isalnum() will return true if there is no speacial character else return false

print(b.isalpha())  # isalpha() will return true if there is only alphabets else return false

print(b.islower()) # b.islower() will return true if all are lowercase else return false

print(b.isupper()) # b.isupper() will return true if all are uppercase else return false


c = " "
print(c.isspace()) # should only contain space will return true else false

hehe = "Hello world i am aamir"
print(hehe.startswith("Hello"))  # checks the first element
print(hehe.swapcase())  # uppercase  <->  lowercase
print(hehe.title())  # first letter of every word capital
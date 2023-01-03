# Methods for tuples
# All list methods can be used by tuple by converting tuple to list

# To make change in tuple you can use mainly two methods or options :-


# 1. You need to create a new list
country = ("India","India","China","Bangladesh","Nepal","Pakistan")
print(country)
print("\n")
countrytemp = list(country)
countrytemp.append("Palestine")
country = tuple(countrytemp)
print(country)
print("\n")

# 2. You need to create a new tuple

state = ("Delhi","Bihar","West Bengal","UP","Goa")
newtuple = country + state  # concatenation of tuples
print(newtuple)
print("\n")

# To print number of occurence
India = country.count("India")
print(India)
print("\n")





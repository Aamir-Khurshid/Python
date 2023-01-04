# Dictionary

info = {
    "Aamir" : "Male",       # Key : Value
    "Mummy" : "Female",
    "Papa"  : "Head"
}

print(info["Aamir"])      # dictname[key]
print(info.keys())
print(info.values())       

# If key is not present then print(info[key]) will throw error
# If key is not present then print(info.get(key)) will not throw error, will return none
print(info.get("Aamir2"))      

# To print using for loop

for k in info.keys():              # Print values using key
    print(info[k])
    
for key,value in info.items():     # Print key with the value
    print(f"key {key} and the value is {value}")

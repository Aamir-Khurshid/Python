list = [3,5,6,"Aamir"]
list1 = [3,4,5,6,66,6,6,6,6]
# to print complete list
print(list[:])
print(list)

# to print an iteration
print(list[0])

# to print elements with a fixed iterartion
print(list1[1:8:2]) # 2 act as gap iteration = iteration + 2

# to find element is list

if 3 in list:
    print("Yes")
else:
    print("No")  

if "ir" in "Aamir":
    print("Yes")

list2 = [i for i in range(4)]
print(list2)
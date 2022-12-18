# break is used to exit the loop at a particular iteration
for i in range(1,8):
    print(i)
    if(i==5):
        print("Here is the termination part bro")
        break

# continue is used to skip a particular iteration
for i in range(1,8):
    print(i)
    if(i==5):
        print("Here is the skipping part bro")
        continue
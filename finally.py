# Finally will always be executed
def func():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter the index: "))
        print(l[i])
    except:
        print("Some error occured")
        return 0;    
    finally:
        print("Always executed even after return")    
a = func()        
print(a)
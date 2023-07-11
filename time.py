import time
def usingWhile():
    i = 0
    while i < 500:
        i = i+1
        print(i)


def usingFor():
    for i in range(500):
        i = i + 1
        print(i)
init = time.time()
usingWhile()
print(time.time() - init)
init2 = time.time()
usingFor()
print(time.time() -  init2)

init3 = time.localtime()
formated = time.strftime("Date = %Y-%M-%d Time = %H:%M:%S")
print(init3)
print(formated)
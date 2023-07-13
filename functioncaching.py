import functools
import time


@functools.lru_cache()
def fx(n):
    time.sleep(2)
    return n*5


print(fx(20))
print("Done")
print(fx(3))
print("Done")
print(fx(20))
print("Done")
print(fx(3))
print("Done")


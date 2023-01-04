# update() in dictionary

ep = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 99}
ep.update(ep2)
print(ep)

# pop(key) to delete a value with its key
ep.pop(122)
print(ep)

# clear() to delete complete dictionary
ep.clear()
print(ep)


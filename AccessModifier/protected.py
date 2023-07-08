# Protected modifier is used by  "_"
class Aamir:
    def __init__(self):
        self._age = 10  # Protected attribute
class Noone(Aamir):
    pass

one = Noone()
print(one._age)  # Correct


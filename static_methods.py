class Math:
    def __init__(self, num):
        self.num = num
    def autonum(self,n):
        self.num = n + self.num
    @staticmethod    #Does not require an instance
    def sum(a, b):
        return a + b

c = Math(4)
print(c.sum(3, 6))
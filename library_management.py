class Library:
    def __init__(self):
        self.n = 0
        self.books = []
    def addBooks(self, books):
        self.books.append(books)
        self.n = len(self.books)
    def showinfo(self):
        print(f"The library has {self.n} books and that are :")
        for i in self.books:
            print(i)

li = Library()
li.addBooks("ENGLISH")
li.addBooks("ENGLISH")
li.addBooks("ENGLISH")
li.addBooks("ENGLISH")
li.showinfo()
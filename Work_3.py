class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def getFullName(self): return f"{self.title} {self.author}"
    def toString(self): return f"Title ={self.title} Author={self.author} Pages={self.pages}"
class Numbers(Book):
    def __init__(self, title, author, pages, books_number):
        super().__init__(title, author, pages)
        self.books_number = books_number
book = Numbers("The Lord of the Rings", "J.R.R. Tolkien", 1207, 10001)
print(book.getFullName())
print(book.toString())
print(book.books_number)
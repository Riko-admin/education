class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
    def get_full_name(self):
        return f"{self._title} {self._author}"
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}"
class Numbers(Book):
    def __init__(self, title, author, pages, books_number):
        super().__init__(title, author, pages)
        self._books_number = books_number
    def get_books_number(self):
        return self._books_number
book = Numbers("The Lord of the Rings", "J.R.R. Tolkien", 1207, 10001)
print(book.get_full_name())
print(book)
print(book.get_books_number())

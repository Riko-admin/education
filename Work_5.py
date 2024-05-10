class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
    def get_full_name(self):
        return f"{self._title} {self._author}"
    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}"
    def read(self):
        return "Шуршит страницами..."
class Numbers(Book):
    def __init__(self, title, author, pages, books_number):
        super().__init__(title, author, pages)
        self._books_number = books_number
    def get_books_number(self):
        return self._books_number
class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self._format = format
    def read(self):
        return f"Открывает файл в формате {self._format}..."
# Создание объектов разных типов
physical_book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1207)
numbered_book = Numbers("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 42, 1)
ebook = Ebook("Pride and Prejudice", "Jane Austen", 279, "EPUB")

# Вывод информации о книгах
print(physical_book.get_full_name())
print(physical_book)
print(physical_book.read())

print(numbered_book.get_full_name())
print(numbered_book)
print(numbered_book.get_books_number())
print(numbered_book.read())

print(ebook.get_full_name())
print(ebook)
print(ebook.read())

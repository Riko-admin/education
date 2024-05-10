# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Соломин Владислав Алексеевич
- ИНО ОЗБ ПОАС 22-1

| Задание | Сам_раб |
| ------ |-----|
| Задание 1 | + | 
| Задание 2 | + | 
| Задание 3 | + | 
| Задание 4 | + | 
| Задание 5 | + | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1207)
print(book.title)
print(book.author)
print(book.pages)
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_8/pic/1.png)

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def getFullName(self): return f"{self.title} {self.author}"
    def toString(self): return f"Title ={self.title} Author={self.author} Pages={self.pages}"
book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1207)
print(book.getFullName())
print(book.toString())
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_8/pic/2.png)

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_8/pic/3.png)

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_8/pic/4.png)

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_8/pic/5.png)

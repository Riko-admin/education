# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Соломин Владислав Алексеевич
- ИНО ОЗБ ПОАС 22-1

| Задание | Сам_раб |
| ------ |------|
| Задание 1 | - | 
| Задание 2 | - | 
| Задание 3 | - | 
| Задание 4 | - | 
| Задание 5 | - | 

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
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
### Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines
```python
def analyze_text(filename):
    letters = 0
    words = 0
    lines_count = 0
    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words += len(line.split())
            letters += sum(1 for char in line if char.isalpha())
    print(f"Input file contains:")
    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines_count} lines")
if __name__ == "__main__":
    analyze_text('input.txt')
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_7/pic/4.png)

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова:
hello email python the exam wor is
### Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
### Ожидаемый результат:
*****, ***ld! ****** ** *** programming language of *** future. My
***** **....
****** ** awesome!!!!
```python
inputText = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
with open("./zapret.txt", "r", ) as myFile:
    words = myFile.read().split(" ")
for word in words:
    inputText = inputText.lower().replace(word, "*" * len(word))
inputText = list(inputText)
inputText = str.join('', inputText)
print(inputText)
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_7/pic/5.png)

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Написать программу ежедневник, которая:
- Запишет задачу.
- Укажет дату выполнения задачи.
- Даст возможность просматривать задачи.
- Будет иметь возможность выйти.
```python
def add_expense():
  date = input("Введите дату выполнения задачи (YYYY-MM-DD): ")
  category = input("Введите тему задачи: ")
  description = input("Введите описание задачи: ")
  with open("diary.txt", "a", encoding='utf-8') as file:
    file.write(f"{date},{category},{description}\n")
  print("Задача добавлена.")
def view_expenses():
  print("Дата\t\tТема\tОписание")
  with open("diary.txt", "r", encoding='utf-8') as file:
    for line in file:
      date, category, description = line.strip().split(",")
      print(f"{date}\t{category}\t\t{description}")
while True:
  action = input("Выберите действие (1-добавить/2-посмотреть/3-выход): ")
  if action.lower() == "1":
    add_expense()
  elif action.lower() == "2":
    view_expenses()
  elif action.lower() == "3":
    break
  else:
    print("Неизвестное действие.")
```
### Результат.
![Меню](https://github.com/Riko-admin/education/blob/Тема_7/pic/6.png)

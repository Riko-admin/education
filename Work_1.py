class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1207)
print(book.title)
print(book.author)
print(book.pages)


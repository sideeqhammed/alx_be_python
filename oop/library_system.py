class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    print(f"{self.title} by {self.author}")

  def book_detail(self):
    print(f"{self.title} by {self.author}")

class EBook(Book):
  def __init__(self, title, author, file_size:int):
    super().__init__(title, author)
    self.file_size = file_size

  def __str__(self):
    print(f"{self.title} by {self.author}, File Size: {self.file_size}KB") 

  def book_detail(self):
    print(f"{self.title} by {self.author}, File Size: {self.file_size}KB") 
    

class PrintBook(Book):
  def __init__(self, title, author, page_count:int):
    super().__init__(title, author)
    self.page_count = page_count

  def __str__(self):
    print(f"{self.title} by {self.author}, Page Count: {self.page_count}")

  def book_detail(self):
    print(f"{self.title} by {self.author}, Page Count: {self.page_count}")


class Library:
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)    

  def list_books(self):
    # print(self.books)
    for book in self.books:
      book.book_detail()
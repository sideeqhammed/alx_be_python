class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

    self._is_checked_out = False

class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    """add book to lirary"""
    self._books.append(book)
    print(f"Added {book.title} by {book.author}")
    
  def check_out_book(self, title):
    """check out a book"""
    for book in self._books:
      if (title == book.title):
        book._is_checked_out = True

  def return_book(self, title):
    """returns a book"""
    for book in self._books:
      if (title == book.title):
        book._is_checked_out = False
    
  def list_available_books(self):
    """list available books"""
    for book in self._books:
      if (book._is_checked_out == False):
        print(f"{book.title} by {book.author}")

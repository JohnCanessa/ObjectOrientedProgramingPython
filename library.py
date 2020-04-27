# **** import(s) ****
from book import Book

# **** Library class ****
class Library:

    # **** constructor method ****
    def __init__ (self):
        self.books = []

    # **** add a book ****
    def add_book(self, book):
        self.books.append(book)

    # **** check out book ****
    def check_out(self, title, name):

        # **** look for the book in the library O(n) ****
        for book in self.books:
            if book.title == title:
                book.check_out(name)
                return
        
        # **** ****
        print("Book not found.")

    # **** check in book ****
    def check_in(self, title, name):

        # **** check if the book in the library O(n) ****
        for book in self.books:
            if book.title == title:
                print("Book not found.")
                return

        # **** ****
        book.check_in(name)

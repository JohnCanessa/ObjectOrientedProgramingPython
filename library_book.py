# **** ****
from book import Book

# **** LibraryBook inherits from Book class ****
class LibraryBook(Book):

    # **** ****
    #pass

    # **** constructor ****
    def __init__(self, title, author, inventory):
        # self.title = title
        # self.author = author
        super().__init__(title, author)

        self.inventory = inventory
        self.borrowers = []

    # **** check out book from the library ****
    def check_out(self, name):

        # **** check inventory (should raise an exception)
        if self.inventory < 1:
            print("Sorry, not available.")
            return

        # **** update other fields ****
        self.inventory -= 1
        self.borrowers.append(name)
    
    # **** print information about a book (overrides super class in book) ****
    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Inventory Remaining: {self.inventory}")
        print(f"Borrowers: {', '.join(self.borrowers)}")
    
    # **** check in a book into the library ****
    def check_in(self, name):

        # ***** check the borrower name ****
        if self.borrowers.__contains__(name) == False:
            print("Invalid borrower.")
            return

        # **** update other fields ****
        self.inventory += 1
        self.borrowers.remove(name)

# **** Book class ****
class Book:

    # **** constructor method ****
    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    # **** print info about the book ****
    def print_info(self):
        print(self.title + " is written by " + self.author)
        #print(f"{self.title} is written by {self.author}")
    
    # **** representation of a book (equivalent to toString in Java) ****
    def __repr__(self):
        return self.title

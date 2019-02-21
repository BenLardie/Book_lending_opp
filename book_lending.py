import random
from datetime import datetime


class Book:
    """A class describing a book"""

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def create(self):
        newbook = Book()
        return self.on_shelf.append(newbook)

    def browse(self):
        random.choice(self.on_shelf)

    

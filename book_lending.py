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

    def lent_out(self, Book):
        if Book == self.on_loan:
            return True
        else:
            return False

    def current_due_date(self):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14  # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

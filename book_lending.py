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

    @classmethod
    def create(cls, title, author, isbn):
        newbook = Book(title, author, isbn)
        cls.on_shelf.append(newbook)
        return newbook

    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)

    def lent_out(self):
        return self in Book.on_loan

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14  # two weeks expressed in seconds
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    def borrow(self):
        if self.lent_out() is True:
            return False
        else:
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            Book.current_due_date()
            return True

    def return_to_library(self):
        if not self.lent_out():
            return False
        else:
            self.due_date = None
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            return True

    @classmethod
    def overdue(cls):
        overdue = []
        for book in Book.on_loan:
            if cls.current_due_date() < datetime.now():
                overdue.append(book)
        return overdue


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse())
print(Book.browse())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sister_outsider.lent_out())
print(sister_outsider.borrow())
print(sister_outsider.current_due_date())
print(len(Book.overdue()))
print(sister_outsider.return_to_library())
print(len(Book.on_shelf))
print(len(Book.on_loan))

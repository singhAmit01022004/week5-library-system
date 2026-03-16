from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def check_out(self, member_id):
        self.available = False
        self.borrowed_by = member_id
        # Sets due date to 14 days from now
        self.due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    def return_book(self):
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by} (Due: {self.due_date})"
        return f"{self.title.ljust(30)} | {self.author.ljust(20)} | {status}"
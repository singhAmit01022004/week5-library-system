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

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        b = cls(data['title'], data['author'], data['isbn'], data['year'])
        b.available = data['available']
        b.borrowed_by = data.get('borrowed_by')
        b.due_date = data.get('due_date')
        return b

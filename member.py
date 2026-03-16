class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] # List of ISBNs

    def __str__(self):
        return f"ID: {self.member_id.ljust(10)} | Name: {self.name.ljust(20)} | Books: {len(self.borrowed_books)}"
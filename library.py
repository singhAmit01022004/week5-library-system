import json
import os

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def add_book(self, title, author, isbn, year):
        from book import Book
        self.books[isbn] = Book(title, author, isbn, year)
        return True, "Book added successfully."

    def register_member(self, name, m_id):
        from member import Member
        self.members[m_id] = Member(name, m_id)
        return True, "Member registered successfully."

    def borrow_book(self, m_id, isbn):
        if m_id not in self.members: return "Member not found."
        if isbn not in self.books: return "Book not found."
        
        book = self.books[isbn]
        member = self.members[m_id]

        if not book.available: return "Book is already out."
        if len(member.borrowed_books) >= 5: return "Borrow limit reached."

        book.check_out(m_id)
        member.borrowed_books.append(isbn)
        return f"Successfully borrowed: {book.title}"

    def return_book(self, isbn):
        if isbn not in self.books or self.books[isbn].available:
            return "Error: Book is already in the library."
        
        book = self.books[isbn]
        member = self.members.get(book.borrowed_by)
        
        if member:
            member.borrowed_books.remove(isbn)
        
        book.return_book()
        return f"Successfully returned: {book.title}"

    def save_data(self):
        # Logic to save to JSON files
        pass

    def load_data(self):
        # Logic to load from JSON files
        pass
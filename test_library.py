from library_system.book import Book

def test_book_creation():
    book = Book("Test Title", "Author", "123", "2024")
    assert book.title == "Test Title"
    assert book.available == True

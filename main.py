from library import Library

def main():
    lib = Library()
    
    print("=" * 32)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("=" * 32)
    print(f"Loaded {len(lib.books)} books from file")
    print(f"Loaded {len(lib.members)} members from file")

    while True:
        print("\n1. Add New Book")
        print("2. Register New Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View All Members")
        print("9. Save & Exit")
        print("0. Exit Without Saving")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            t = input("Title: "); a = input("Author: "); i = input("ISBN: "); y = input("Year: ")
            _, msg = lib.add_book(t, a, i, y)
            print(msg)

        elif choice == "3":
            m_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(lib.borrow_book(m_id, isbn))

        elif choice == "6":
            print("-" * 60)
            print(f"{'Title'.ljust(30)} | {'Author'.ljust(20)} | Status")
            print("-" * 60)
            for b in lib.books.values():
                print(b)

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
def display_menu():
    print("\n------- Library Menu -------")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. Remove a Book")
    print("6. Exit")

books = []

def add_book():
    book_id = input("Enter the Book ID: ")
    for book in books:
        if book['id'] == book_id:
            print("Book already exists.")
            return
    title = input("Enter the Book Title: ")
    author = input("Enter the Author: ")
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })
    print("Book added successfully.")

def display_all_books():
    if not books:
        print("No books available.")
        return
    print("\nAvailable Books in Library:")
    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}")

def borrow_book():
    book_id = input("Enter the Book ID to borrow: ")
    for book in books:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                print(f"You have borrowed '{book['title']}' successfully!")
                return
            else:
                print("Book is currently not available.")
                return
    print("Book ID not found.")

def return_book():
    book_id = input("Enter the Book ID to return: ")
    for book in books:
        if book['id'] == book_id:
            if not book['available']:
                book['available'] = True
                print(f"Thank you for returning '{book['title']}'!")
                return
            else:
                print("This book was not issued.")
                return
    print("Book ID not found!")

def remove_book():
    book_id = input("Enter the Book ID to remove: ")
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            print("Book removed successfully.")
            return
    print("Book ID not found!")

# MAIN LOOP
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        display_all_books()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        remove_book()
    elif choice == '6':
        print("Exiting Library. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

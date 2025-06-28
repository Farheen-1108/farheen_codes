class Library:
    def __init__(self):
        # Store books as dictionary with book_id as key
        # Each book will have title, author, and availability status
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book with ID '{book_id}' already exists.")
            return
        self.books[book_id] = {
            "title": title,
            "author": author,
            "available": True  # True means book is available to borrow
        }
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nAvailable books in the library:")
        for book_id, info in self.books.items():
            status = "Available" if info["available"] else "Borrowed"
            print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}")

    def borrow_book(self, book_id):
        if book_id not in self.books:
            print("Book ID not found.")
            return
        if not self.books[book_id]["available"]:
            print(f"Sorry, '{self.books[book_id]['title']}' is already borrowed.")
            return
        self.books[book_id]["available"] = False
        print(f"You have successfully borrowed '{self.books[book_id]['title']}'.")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Book ID not found.")
            return
        if self.books[book_id]["available"]:
            print(f"'{self.books[book_id]['title']}' was not borrowed.")
            return
        self.books[book_id]["available"] = True
        print(f"Thank you for returning '{self.books[book_id]['title']}'.")


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid input! Please choose a valid option (1-5).")


if __name__ == "__main__":
    main()

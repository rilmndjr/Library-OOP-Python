class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Initially set as available

class Library:
    def __init__(self):
        self.books = []  # List to store Book objects

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found in the library")

    def display_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List to store Book objects

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"This book '{book.title}' is not borrowed by {self.name}")

# Example usage:
if __name__ == "__main__":
    library = Library()

    # Function to input books
    def input_books():
        while True:
            title = input("Enter book title (or 'done' to finish adding): ")
            if title.lower() == 'done':
                break
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

    # Function to input members
    def input_members():
        members = []
        while True:
            name = input("Enter member name (or 'done' to finish adding): ")
            if name.lower() == 'done':
                break
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            members.append(member)
        return members

    # Input books
    print("Add books to the library:")
    input_books()

    # Input members
    print("\nRegister members:")
    members = input_members()

    # Display all books in the library
    print("\nBooks available in the library:")
    library.display_books()

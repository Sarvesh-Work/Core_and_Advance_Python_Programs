# Lab1:  Write a Python program to model a Library system. The program should include a class named Library with the following specifications: 

# 1. Class Attributes: ○ total_books: A class attribute representing the total number of books available in the library. ○ all_books: A class attribute that stores a list of all books available. 

#  2. Instance Attributes: ○ name:Nameof the library member. ○ borrowed_books: A list to keep track of books borrowed by the member. 

#  3. Methods: ○ borrow_book(self, book): A method to borrow a book from the library. The method should: ■ Checkif the book is available

# . ■ Addthebook to the member's borrowed list. 

#  ■ Removethe book from the library's all_books list. 

#  ■ Decrease total_books by 1

# . ■ If the book is not available, return a message saying "Book not available." ○ return_book(self, book): A method to return a book. The method should: 

#  ■ Addthebook back to the library's all_books list.

#  ■ Removethe book from the member's borrowed_books list. 

#  ■ Increase total_books by 1. 

#  4. Class Method: ○ view_library_books(cls): A class method that prints the total number of books and lists all available books.


# solution---->

class Library:
    total_books = 0  # Class attribute to track total books in the library
    all_books = []  # Class attribute to store all available books

    def __init__(self, name):
        self.name = name  # Instance attribute for the library member's name
        self.borrowed_books = []  # List to track books borrowed by the member

    def borrow_book(self, book):
        """Method to borrow a book from the library"""
        if book in Library.all_books:
            self.borrowed_books.append(book)
            Library.all_books.remove(book)
            Library.total_books -= 1
            return f"{self.name} has borrowed '{book}'."
        else:
            return "Book not available."

    def return_book(self, book):
        """Method to return a borrowed book to the library"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            Library.all_books.append(book)
            Library.total_books += 1
            return f"{self.name} has returned '{book}'."
        else:
            return "This book was not borrowed by you."

    @classmethod
    def view_library_books(cls):
        """Class method to view all available books in the library"""
        print(f"Total Books: {cls.total_books}")
        print("Available Books:", ", ".join(cls.all_books) if cls.all_books else "No books available.")

# Example Usage
Library.all_books = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Moby Dick"]
Library.total_books = len(Library.all_books)

# Creating a library member
member1 = Library("Alice")
print(member1.borrow_book("1984"))
print(member1.borrow_book("The Great Gatsby"))

Library.view_library_books()

print(member1.return_book("1984"))
Library.view_library_books()

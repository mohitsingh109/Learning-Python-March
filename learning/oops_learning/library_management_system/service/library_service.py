from models.book import Book
from utils.file_handling import load_books, save_book


class LibraryService:

    def __init__(self):
        self.__books = load_books() # list of books
        self.__borrowed = []


    # Admin can do

    def add_book(self):
        book_id = input("Enter book id: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        category = input("Enter book category: ")
        status = input("Enter book status: ")

        book = Book(book_id, title, author, category, status)
        self.__books.append(book)
        save_book(book) # file append
        print("Book added successfully!")


    def remove_book(self):
        book_id = input("Enter book id: ")
        pass


    def view_all_books(self):
        for book in self.__books:
            print(book) # __str__

    def view_all_borrowed_books(self):
        pass

    # User can do
    


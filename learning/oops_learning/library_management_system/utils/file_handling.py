from ..models.book import Book

BOOK_FILE = 'books.txt'
BORROWED_FILE = 'borrowed.txt'

def load_books():
    books = []
    with open(BOOK_FILE, 'r') as f:
        for line in f:
            data = line.split(',')
            if len(data) == 5:
                book = Book(*data)
                books.append(book)

    return books

def save_book(book):
    with open(BOOK_FILE, 'a') as f:
        f.write(book.to_file_string())


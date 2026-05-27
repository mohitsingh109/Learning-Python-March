class Book:

    def __init__(self, book_id, title, author, category, status = "Available"):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__category = category
        self.__status = status


    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_category(self):
        return self.__category

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Book id: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Category: {self.__category}, Status: {self.__status}"

    def to_file_string(self):
        return f"{self.__book_id},{self.__title},{self.__author},{self.__category},{self.__status}\n"


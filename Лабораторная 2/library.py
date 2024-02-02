from book import *


class Library:
    def __init__(self, books: list[Book] = []):
        if not isinstance(books, list):
            raise TypeError("List of books must be a list")
        for e in books:
            if not isinstance(e, Book):
                raise TypeError("List must contain books")
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id):
        for book in self.books:
            if book.id_ == id:
                return self.books.index(book)
        raise ValueError("Книги с запрашиваемым id не существует")
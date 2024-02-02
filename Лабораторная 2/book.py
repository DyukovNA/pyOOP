class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 1:
            raise ValueError("Name can't be an empty string")
        self.name = name

        if not isinstance(id_, int):
            raise TypeError("ID must be an integer")
        if id_ < 0:
            raise ValueError("ID must be positive")
        self.id_ = id_

        if not isinstance(pages, int):
            raise TypeError("Number of pages must be an integer")
        if pages < 0:
            raise ValueError("Number of pages must be positive")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name="{self.name}", pages={self.pages})'
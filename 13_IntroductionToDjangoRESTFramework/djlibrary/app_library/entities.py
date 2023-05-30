class Book:
    def __init__(self, name, isbn, release, pages, autor):
        self.name = name
        self.isbn = isbn
        self.release = release
        self.pages = pages
        self.autor = autor

    def to_dict(self):
        return {
            'name': self.name,
            'isbn': self.isbn,
            'release': self.release,
            'pages': self.pages,
            'autor': self.autor,
        }
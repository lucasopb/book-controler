
class BookController:
    books = []

    def get(self, nome=None):
        if nome:
            for book in self.books:
                if book['nome'] == nome:
                    return book
        return self.books

    def create(self, data):
        self.books.append(data)
        return data

    def update(self, nome, data):
        for book in self.books:
            if book['nome'] == nome:
                book.update(data)
                return book
        return None

    def delete(self, nome):
        for book in self.books:
            if book['nome'] == nome:
                self.books.remove(book)
                return book
        return None

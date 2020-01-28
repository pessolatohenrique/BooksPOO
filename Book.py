from Publication import Publication

class Book(Publication):
    def __init__(self, name, publicated_at, genders, pages, isbn, authors):
        super().__init__(name, publicated_at, genders, pages)
        self._isbn = isbn
        self._authors = authors

    def get_book_authors(self):
        authors_names = []
        for author in self._authors:
            authors_names.append(author.name)

        authors_text = ', '.join(authors_names)
        return authors_text

    def show_info(self):
        authors_text = self.get_book_authors()
        print(f'Livro: {self._name} ({self._pages} páginas) - Publicado em: {self._publicated_at} - Autores: {authors_text}')

    def calculate_days_to_read(self, pages_readed):
        average = int(self._pages / pages_readed)
        print(f'Você possivelmente terminará o livro "{self._name}" em {average} dias')
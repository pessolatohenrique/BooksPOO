class Publication:
    def __init__(self, name, publicated_at, genders, pages):
        self._name = name
        self._publicated_at = publicated_at
        self._genders = genders
        self._pages = pages

    def show_info(self):
        print(f'Título: {self._name} - Gêneros: {self._genders} - Publicado em: {self._publicated_at}')
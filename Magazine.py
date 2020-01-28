from Publication import Publication

class Magazine(Publication):
    def __init__(self, name, publicated_at, genders, edition):
        super().__init__(name, publicated_at, genders)
        self._edition = edition

    def show_info(self):
        print(f'Revista: {self._name} - Edição: {self._edition} - Publicado em: {self._publicated_at}')

    def get_next_edition(self):
        next = self._edition + 1
        print(f"Próxima edição será a de número {next}")

    def get_previous_edition(self):
        previous = self._edition - 1
        print(f"A edição anterior foi a de número {previous}")
from Genre import Genre
from Author import Author
from Publication import Publication
from Magazine import Magazine

if (__name__ == "__main__"):
    #gêneros
    adventure = Genre('Aventura')
    fantasy = Genre('Fantasia')
    philosophy = Genre('Filosofia')
    science = Genre('Ciências')

    #autores
    jkrowling = Author('J.K. Rowling')
    cortella = Author('Mario Sérgio Cortella')

    #publicacoes
    harrypotter = Publication('Harry Potter e a pedra filosofal', 2019, [adventure.name, fantasy.name])
    harrypotter.show_info()

    #revistas
    mundoestranho = Magazine('Mundo Estranho', 'Jan / 2019', science.name, 129)
    mundoestranho.show_info()
    mundoestranho.get_next_edition()
    mundoestranho.get_previous_edition()
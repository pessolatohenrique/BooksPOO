from Genre import Genre
from Author import Author
from Publication import Publication

if (__name__ == "__main__"):
    #gêneros
    adventure = Genre('Aventura')
    fantasy = Genre('Fantasia')
    philosophy = Genre('Filosofia')

    #autores
    jkrowling = Author('J.K. Rowling')
    cortella = Author('Mario Sérgio Cortella')

    #publicacoes
    harrypotter = Publication('Harry Potter e a pedra filosofal', 2019, [])
    print(harrypotter._name)
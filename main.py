from Genre import Genre
from Author import Author
from Magazine import Magazine
from Book import Book

if (__name__ == "__main__"):
    #gêneros
    adventure = Genre('Aventura')
    fantasy = Genre('Fantasia')
    philosophy = Genre('Filosofia')
    science = Genre('Ciências')

    #autores
    jkrowling = Author('J.K. Rowling')
    cortella = Author('Mario Sérgio Cortella')
    karnal = Author('Leandro Karnal')
    ponde = Author('Luiz Felipe Pondé')

    #livros
    harrypotter = Book('Harry Potter e a pedra filosofal', 2019, [adventure.name, fantasy.name], 230,'5433-1', [jkrowling])
    felicidade = Book('Felicidade: modos de usar', 2019, [philosophy], 100, '4351-2', [cortella, karnal, ponde])
    harrypotter.show_info()
    harrypotter.calculate_days_to_read(30)
    print('\n')
    felicidade.show_info()
    felicidade.calculate_days_to_read(50)
    print('\n')

    #revistas
    mundoestranho = Magazine('Mundo Estranho', 'Jan / 2019', [science], 50, 129)
    mundoestranho.show_info()
    mundoestranho.get_next_edition()
    mundoestranho.get_previous_edition()
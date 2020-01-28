class Author:
    def __init__(self, name):
        self.__name = name

    def __getitem__(self, item):
        return

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
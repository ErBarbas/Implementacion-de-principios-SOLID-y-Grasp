from abc import abstractmethod
from Enum.Gender import Gender


class Person:

    __name = ''
    __age = 0
    __gender = ''

    def __init__(self, name: str, age: int, gender: Gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise Exception('{} no es un nombre valido para una persona!'.format(value))

        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise Exception('La edad {} no es valida para una persona!'.format(value))

        self.__age = value

    @property
    def gender(self) -> Gender:
        return self.__gender

    @gender.setter
    def gender(self, value: Gender) -> None:
        self.__gender = value

    @abstractmethod
    def read(self) -> None:
        print('Estoy leyendo')

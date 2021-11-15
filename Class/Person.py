from abc import abstractmethod

from Enum.Gender import Gender


class Person:

    def __init__(self, name: str, age: int, gender: Gender):
        if age < 0:
            raise Exception('La edad {} no es valida para una persona!'.format(age))

        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
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

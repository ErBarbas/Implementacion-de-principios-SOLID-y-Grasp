from abc import abstractmethod


class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @abstractmethod
    def read(self):
        print("Estoy leyendo")

    # Este es un ejemplo de lo que no se debe hacer en el principio de responsabilidad única

    '''
    Crear funciones / metodos que asuman una responsabilidad extra a la clase:
    
    def guardarPersona(self):
        print("Guardando persona...")

    def actualizarPersona(self):
        print("Actualizando persona...")

    def eliminarPersona(self):
        print("Eliminando persona...") 
        
    Estos metodos los podría manejar otra clase que se encargue de operar con alguna base de datos.
    Como solución creamos una clase PersonDB.
    '''

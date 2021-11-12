class Persona:

    def __init__(self):
        self.__edad = 0
        self.__nombre = ''
        self.__genero = ''

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

    def leer(self):
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
    Como solución creamos una clase PersonaDB
    '''

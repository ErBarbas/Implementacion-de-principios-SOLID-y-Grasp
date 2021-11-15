from Class.Baby import Baby
from Enum.Gender import Gender
from Class.Kid import Kid
from Class.Person import Person
from Class.Teen import Teen

'''
Primer principio: Principio de responsabilidad única.
Para esto se deben crear funciones / metodos que asuman una responsabilidad extra a la clase:

def guardarPersona(self):
    print("Guardando persona...")

def actualizarPersona(self):
    print("Actualizando persona...")

def eliminarPersona(self):
    print("Eliminando persona...") 
    
Estos metodos los podría manejar otra clase que se encargue de operar con alguna base de datos.
Como solución creamos una clase PersonDB.
'''

print('------------------- SEGUNDO PRINCIPIO - abierto/cerrado --------------------')

'''
Segundo principio SOLID: Principio abierto/cerrado
Para este principio debemos hacer que el codigo que tenemos funcione sin importar la cantidad
de instancias que tengamos. Esto debido a que el modulo o clase debe poder extenderse (código abierto) con nuevas 
funcionalidades sin tener que modificar el codigo para evitar errores (código cerrado).

Mala practica: Crear condiciones innecesarias para imprimir un mensaje cuando una persona de cierta edad está leyendo.
Ejemplo:

persons = [
    Person('Carlos', 18, 'Masculino'),
    Person('Carol', 13, 'Feminino'),
    Person('Julior', 3, 'Masculino')
]

for person in persons:
    if person.age < 5:
        print('Agugu gaga')
    elif 5 < person.age < 13:
        print('Me cuesta mucho leer!')
    elif 13 < person.age < 18:
        print('Estoy leyendo sin problema pero con un poco de torpeza..')
    elif 18 < person.age < 45:
        print('Leo sin ningún problema!')
    elif person.age > 45:
        print('Donde están mis lentes!')


Buena practica: Crear codigo para n instancias:
Ejemplo:

Si tenemos 3 Personas y queremos ejecutar un metodo para que cada persona lea de forma personalizada según se edad, lo 
ideal sería hacer lo siguiente:
'''

persons = [
    Teen('Carlos', 17, Gender.MALE),
    Kid('Carol', 12, Gender.FEMININE),
    Baby('Julior', 3, Gender.MALE)
]

for person in persons:
    print(person.name + " dice: ")
    person.read()

print('\n------------------- TERCER PRINCIPIO - Principio de substitución de Liskov--------------------')

'''
El tercer principio llamado: Principio de substitución de Liskov, el cuál indica que una
subclase (en este caso Baby, Kid, Teen, Adult o Elderly) debe poder ser reemplazada por su superclase (Person).

Esto lo podemos comprobar con el siguiente codigo:
'''

teen = Teen('Valentina', 15, Gender.FEMININE)
teen.read()

'''
Ahora podemos llamar la superclase Person y no tendremos ningún problema, ya que está tiene su codigo propio para el
metodo read.
'''

person = Person('Carlos', 18, Gender.MALE)
person.read()

'''
El cuarto principio es: Principio de segregación de interfaz. El cuál indica que una clase no debe estar forzada a
implementar interfaces con funcionalidades que nunca llegarán a usar. Esto normalmente debido a que la interfaz no 
está bien estructurada o tiene complejidad innecesaria.

Para combatir contra lo anterior, el principio nos recomienda lo siguiente: 
Debemos segregar una interfaz con gran complejidad en interfaces más pequeñas para que sean más usables.

Ejemplo:

'''

from Class.Baby import Baby
from Class.Connections.DataAccess import DataAccess
from Class.Connections.DataAccessAPI import DataAccessAPI
from Class.Connections.DataAccessDB import DataAccessDB
from Class.LightInfantry import LightInfantry
from Class.Soldier import Soldier
from Class.SupportInfantry import SupportInfantry
from Enum.Gender import Gender
from Class.Kid import Kid
from Class.Person import Person
from Class.Teen import Teen

'''
Primer principio: Principio de responsabilidad única.
Para esto se deben crear funciones / métodos que asuman una responsabilidad extra a la clase:

def save_person(self):
    print("Guardando persona...")

def update_person(self):
    print("Actualizando persona...")

def delete_person(self):
    print("Eliminando persona...") 
    
Estos métodos los podría manejar otra clase que se encargue de operar con alguna base de datos.
Como solución creamos una clase PersonDB.
'''

print('------------------- SEGUNDO PRINCIPIO - abierto/cerrado --------------------')

'''
Segundo principio SOLID: Principio abierto/cerrado
Para este principio debemos hacer que el código que tenemos funcione sin importar la cantidad
de instancias que tengamos. Esto debido a que el modulo o clase debe poder extenderse (código abierto) con nuevas 
funcionalidades sin tener que modificar el código para evitar errores (código cerrado).

Mala práctica: Crear condiciones innecesarias para imprimir un mensaje cuando una persona de cierta edad está leyendo.
Ejemplo:

persons = [
    Person('Carlos', 18, Gender.MALE),
    Person('Carol', 13, Gender.FEMININE),
    Person('Julior', 3, Gender.MALE)
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


Buena practica: Crear código para n instancias:
Ejemplo:

Si tenemos 3 Personas y queremos ejecutar un método para que cada persona lea de forma personalizada según se edad, lo 
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

print('\n------------------- TERCER PRINCIPIO - Principio de substitución de Liskov --------------------')

'''
El tercer principio llamado: Principio de substitución de Liskov, el cual indica que una
subclase (en este caso Baby, Kid, Teen, Adult o Elderly) debe poder ser reemplazada por su superclase (Person).

Esto lo podemos comprobar con el siguiente código:
'''

teen = Teen('Valentina', 15, Gender.FEMININE)
teen.read()

'''
Ahora podemos llamar la superclase Person y no tendremos ningún problema, ya que está tiene su código propio para el
método read.
'''

person = Person('Carlos', 18, Gender.MALE)
person.read()

print('\n------------------- CUARTO PRINCIPIO - Principio de segregación de interfaz  --------------------')

'''
El cuarto principio es: Principio de segregación de interfaz. El cuál indica que una clase no debe estar forzada a
implementar interfaces con funcionalidades que nunca llegarán a usar. Esto normalmente debido a que la interfaz no 
está bien estructurada o tiene complejidad innecesaria.

Para combatir lo anterior, el principio nos recomienda lo siguiente: 
Debemos segregar una interfaz con gran complejidad en interfaces más pequeñas para que sean más usables.

Ejemplo:

Creamos varias interfaces:
-AttackSoldier: La clase que la implemente tendrá la capacidad de utilizar métodos propios de
un soldado de infantería  de ataque.

-GuardSoldier: La clase que la implemente tendrá la capacidad de utilizar métodos propios de
un soldado de infantería  para hacer de guardia o patrullar.

-InfiltrationSoldier: La clase que la implemente tendrá la capacidad de utilizar métodos propios de
un soldado infiltrado en campo enemigo.

-MedicSoldier: La clase que la implemente tendrá la capacidad de utilizar métodos propios de un médico de combate.

Con esto podremos personalizar cada clase de soldado que creemos, implementando las funcionalidades que necesitemos.
Por ejemplo, revisemos algunas de las nuevas clases creadas en la carpeta Class:

LightInfantry (Infanteria ligera) y SupportInfantry (Infanteria de apoyo). Cada una de las clases anteriormente 
mencionadas implementa diferentes funcionalidades. 

En el caso de LightInfantry; esta implementa solamente la interfaz AttackSoldier, debido a que el propósito de un
soldado ligero de infantería  es el ataque.

En el caso de SupportInfantry; esta implementa todas las interfaces anteriormente creadas ya que un soldado de apoyo
puede llegar a realizar diferentes tipos de apoyo, como un apoyo en ataque; un apoyo en guardia o patrulla, o un apoyo
en el cuidado y sanación de las tropas heridas.

Sin embargo, las clases anteriores no están obligadas a implementar estas interfaces, solamente se usarán cuando
necesitemos fines concretos.

'''

light_infantry = LightInfantry(10, 20, 15)
light_infantry.attack()
light_infantry.assault()

print('\n')

support_infantry = SupportInfantry(15, 15, 25)
support_infantry.attack()

carlos = Soldier(20, 45, 35)

support_infantry.bandage(carlos)
support_infantry.patrol()

print('\n------------------- QUINTO PRINCIPIO - Principio de inversión de dependencias  --------------------')

'''
Este prinpicio nos indica que las dependencias de un modulo deben estar basadas en abstracciones, o sea, que debemos
poder asignar de forma completamente personalizada una dependencia en un modulo.

Para esto utilizaremos un ejemplo de conexion a cierta fuente de datos.
Si una clase se encarga de obtener datos de solamente una base de datos, en el momento en el que este mismo servicio
quiera ser reutilizado para poder obtener datos de un API, no lo podremos hacer.

Para esto, se puede crear una interfaz con la cual podamos definir de forma abstracta el tipo de conexion de datos que
usaremos.

Ejemplo:
'''

data_access_db = DataAccess(DataAccessDB())
data_access_db.get_data()

data_access_api = DataAccess(DataAccessAPI())
data_access_api.get_data()

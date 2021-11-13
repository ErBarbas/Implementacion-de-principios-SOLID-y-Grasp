from Class.Baby import Baby
from Class.Kid import Kid
from Class.Teen import Teen

'''
Para el principio de abierto / cerrado debemos hacer que el codigo que tenemos funcione sin importar la cantidad
de instancias que tengamos.

Mala practica: Crear condiciones innecesarias para imprimir cada persona.
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

Si tenemos 3 Personas y queremos ejecutar un metodo personalizado para cada instancia, lo ideal 
sería hacer lo siguiente:
'''

persons = [
    Teen('Carlos', 17, 'Masculino'),
    Kid('Carol', 12, 'Feminino'),
    Baby('Julior', 3, 'Masculino')
]

for person in persons:
    print(person.name + " dice: " + person.read())

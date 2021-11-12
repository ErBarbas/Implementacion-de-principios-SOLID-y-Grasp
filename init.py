# Este es un comentario de prueba.
# como que no se que poner
from Persona import Persona

'''
Para el principio de abierto / cerrado debemos hacer que el codigo que tenemos funcione sin importar la cantidad
de instancias que tengamos.

Mala practica: Crear condiciones innecesarias para imprimir cada persona.

persona1 = Persona()
persona1.edad = 18

persona2 = Persona()
persona2.edad = 16

persona3 = Persona()
persona3.edad = 13

Ejemplo:
if persona1.edad == 18 : print("Persona1 es mayor")
if persona2.edad == 18 : print("Persona2 es mayor")
if persona3.edad == 18 : print("Persona3 es mayor")
if persona1.edad < 18 : print("Persona1 es menor")
if persona2.edad < 18 : print("Persona2 es menor")
if persona3.edad < 18 : print("Persona3 es menor")

Buena practica: Crear codigo para n instancias:
Ejemplo: 

Si tenemos 5 Personas y queremos mostrar sus edades, lo ideal sería hacer lo siguiente:
'''

persona1 = Persona()
persona1.nombre = 'Carlos'
persona1.edad = 18

persona2 = Persona()
persona2.nombre = 'Carol'
persona2.edad = 16

persona3 = Persona()
persona3.nombre = 'Julior'
persona3.edad = 19

personas = [persona1, persona2, persona3]

for persona in personas:
    if persona.edad >= 18:
        print(persona.nombre + " es mayor")
    else:
        print(persona.nombre + " es menor")

from Class.Person.Person import Person


class Teen(Person):

    def __init__(self, name, age, gender):
        if 13 < age < 18:
            self.age = age
        else:
            raise Exception("No ha dado una edad valida para un adolescente!")

        super().__init__(name, self.age, gender)

    def read(self):
        return 'Estoy leyendo sin problema pero con un poco de torpeza..'

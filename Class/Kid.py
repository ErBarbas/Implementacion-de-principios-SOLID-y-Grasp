from Class.Person import Person


class Kid(Person):

    def __init__(self, name, age, gender):
        if 5 < age < 13:
            self.age = age
        else:
            raise Exception("No ha dado una edad valida para un niño!")

        super().__init__(name, self.age, gender)

    def read(self):
        print('Me cuesta mucho leer!')

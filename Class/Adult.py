from Class.Person import Person


class Adult(Person):

    def __init__(self, name, age, gender):
        if 18 < age < 45:
            self.age = age
        else:
            raise Exception("No ha dado una edad valida para un adulto!")

        super().__init__(name, age, gender)

    def read(self):
        print('Leo sin ningún problema!')

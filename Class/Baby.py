from Class.Person import Person


class Baby(Person):
    def __init__(self, name, age, gender):
        if 0 < age < 5:
            self.age = age
        else:
            raise Exception("No ha dado una edad valida para un bebé!")

        super().__init__(name, self.age, gender)

    def read(self):
        print('Agugu gaga')

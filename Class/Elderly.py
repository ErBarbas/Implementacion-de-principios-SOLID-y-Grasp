from Class.Person import Person


class Elderly(Person):

    def __init__(self, name, age, gender):
        if age > 45:
            self.age = age
        else:
            raise Exception("No ha dado una edad valida para un anciano!")

        super().__init__(name, self.age, gender)

    def read(self):
        print('Donde están mis lentes!')

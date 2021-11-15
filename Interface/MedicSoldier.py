from abc import ABCMeta, abstractmethod

from Class.Soldier import Soldier


class MedicSoldier(metaclass=ABCMeta):

    @staticmethod
    def __check_health(soldier):
        if soldier.health == 0:
            print('Ya no hay nada que hacer...')
            return
        else:
            print('Aún puedo salvarlo!')

    @abstractmethod
    def bandage(self, soldier: Soldier):
        self.__check_health(soldier)
        print('Estoy vendando a mi compañero..')
        soldier.health += 20

    @abstractmethod
    def disinfect(self, soldier: Soldier):
        self.__check_health(soldier)
        print('Estoy desinfectando las heridas de mi compañero..')
        soldier.health += 10

    @abstractmethod
    def stitch(self, soldier: Soldier):
        self.__check_health(soldier)
        print('Estoy cociendo las heridas abiertas de mi compañero..!')
        soldier.health += 30

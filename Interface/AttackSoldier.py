from abc import ABCMeta, abstractmethod


class AttackSoldier(metaclass=ABCMeta):

    @abstractmethod
    def attack(self):
        print('Estoy avanzando para atacar!')

    @abstractmethod
    def assault(self):
        print('Estoy asaltando la posición del enemigo!')

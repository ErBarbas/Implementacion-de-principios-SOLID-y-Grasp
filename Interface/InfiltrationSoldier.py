from abc import ABCMeta, abstractmethod


class InfiltrationSoldier(metaclass=ABCMeta):

    @abstractmethod
    def explore(self):
        print('Estoy explorando un asentamiento enemigo...')

    @abstractmethod
    def steal(self):
        print('Estoy robando suministros del enemigo...')

from abc import ABCMeta, abstractmethod


class GuardSoldier(metaclass=ABCMeta):

    @abstractmethod
    def protect(self):
        print('Protegiendo la zona...')

    @abstractmethod
    def patrol(self):
        print('Patrullando la zona...')

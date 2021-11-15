from abc import ABCMeta, abstractmethod


class ConnectionAPP(metaclass=ABCMeta):

    @abstractmethod
    def get_data(self):
        print('Cargando datos...   Carga completada!!')

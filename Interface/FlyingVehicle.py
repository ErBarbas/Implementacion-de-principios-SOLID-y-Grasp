from abc import ABCMeta, abstractmethod


class FlyingVehicle(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass

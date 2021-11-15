class Soldier:
    __health = 0
    __resistance = 0
    __velocity = 0

    def __init__(self, health: int, resistance: int, velocity: int):
        self.health = health
        self.__resistance = resistance
        self.__velocity = velocity

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        if value < 1:
            raise Exception('{} no es un valor valido para la salud del soldado'.format(value))

        self.__health = value

    @property
    def resistance(self) -> int:
        return self.__resistance

    @resistance.setter
    def resistance(self, value: int) -> None:
        if value < 1:
            raise Exception('{} no es un valor valido para la resistencia del soldado'.format(value))

        self.__resistance = value

    @property
    def velocity(self) -> int:
        return self.__velocity

    @velocity.setter
    def velocity(self, value: int) -> None:
        if value < 1:
            raise Exception('{} no es un valor valido para la velocidad del soldado'.format(value))

        self.__velocity = value

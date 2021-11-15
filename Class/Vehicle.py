class Vehicle:

    def __init__(self, color: str, velocity: int, num_wheels: int = 0):
        if num_wheels < 0:
            raise Exception('El numero de ruedas {} no es valido para un vehiculo!'.format(num_wheels))
        if velocity < 0:
            raise Exception('La velocidad {} no es una velocidad valida'.format(velocity))

        self.color = color
        self.velocity = velocity
        self.num_wheels = num_wheels

    def speed_up(self):
        self.velocity += 5

    def reduce_speed(self):
        self.velocity -= 5

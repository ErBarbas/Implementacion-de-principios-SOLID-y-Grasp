from Class.Soldier import Soldier
from Interface.AttackSoldier import AttackSoldier
from Interface.InfiltrationSoldier import InfiltrationSoldier


class LightInfantry(Soldier, AttackSoldier, InfiltrationSoldier):

    def __init__(self, health, resistance, velocity):
        super().__init__(health, resistance, velocity)

    def attack(self):
        AttackSoldier.attack(self)

    def assault(self):
        AttackSoldier.assault(self)

    def explore(self):
        InfiltrationSoldier.explore(self)

    def steal(self):
        InfiltrationSoldier.steal(self)


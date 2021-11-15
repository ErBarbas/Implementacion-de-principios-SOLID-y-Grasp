from Class.Soldier import Soldier
from Interface.AttackSoldier import AttackSoldier
from Interface.GuardSoldier import GuardSoldier
from Interface.MedicSoldier import MedicSoldier


class SupportInfantry(Soldier, AttackSoldier, GuardSoldier, MedicSoldier):

    def attack(self):
        print('Apoyando la posición de ataque de mis compañeros!')

    def assault(self):
        print('Apoyando el asalto contra las tropas enemigas..!')

    def protect(self):
        print('Apoyando la huida de nuestras tropas aliadas!')

    def patrol(self):
        GuardSoldier.patrol(self)

    def bandage(self, soldier):
        MedicSoldier.bandage(self, soldier)

    def disinfect(self, soldier):
        MedicSoldier.disinfect(self, soldier)

    def stitch(self, soldier):
        MedicSoldier.stitch(self, soldier)

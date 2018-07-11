from Character import Character
import random


class Combatant(Character):

    def __init__(self):
        pass

    def getDieRoll(self):
        return random.randint(1, 20)

    def checkHit(self, roll):
        if roll > Combatant.armor:
            return True
        return False

    def attacked(self, dieRoll):
        if dieRoll < 20:
            self.hitpoints -= self.damage
        else:
            self.hitpoints -= 2 * self.damage

    def isAlive(self):
        return self.hitpoints > 0

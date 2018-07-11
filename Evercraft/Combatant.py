from Character import Character
import random

class Combatant(Character):
    
    def __init__(self):
        pass

    def getDieRoll(self):
        return random.randint(1,20)

    def checkHit(self, roll):
        if roll > Combatant.armor:
            return True
        return False







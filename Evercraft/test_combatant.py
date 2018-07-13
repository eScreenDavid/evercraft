
import unittest
from Combatant import Combatant


class TestCombatant(unittest.TestCase):

    def test_armor_default(self):
        player = Combatant()
        self.assertEqual(player.getArmor(), 10)

    def test_hitpoint_default(self):
        player = Combatant()
        self.assertEqual(player.getHitPoints(), 5)

    def test_hit(self):
        player = Combatant()
        opponent = Combatant()
        dieRoll = player.getDieRoll()
        if(dieRoll <= opponent.getArmor()):
            self.assertFalse(opponent.checkHit(dieRoll))
        else:
            self.assertTrue(opponent.checkHit(dieRoll))

    def test_is_alive(self):
        player = Combatant()
        player.attacked(player.getDieRoll())
        self.assertTrue(player.isAlive())

    def test_is_dead(self):
        player = Combatant()
        player.hitpoints = 1
        player.attacked(player.getDieRoll())
        self.assertFalse(player.isAlive())

    def test_attribute_modifiers_on_hitting(self):
        player1 = Combatant()
        player2 = Combatant()
        player2.setAttribute("STRENGTH", 14)
        bonusHit = player2.getModifier(player2.abilities.get("STRENGTH"))
        self.assertTrue(player1.checkHit(9+bonusHit))

    def test_experience_gain(self):
        player = Combatant()
        challenger = Combatant()

        for i in range(10):
            dieRoll = player.getDieRoll()
            currentExperience = player.experience
            
            if player.hitEnemy(dieRoll, challenger.getArmor()):
                challenger.attacked(dieRoll)
                self.assertEqual(player.experience, currentExperience + 10)

            else:
                self.assertEqual(player.experience, currentExperience)

    def test_levels_gained(self):
        player = Combatant()
        challenger = Combatant()

        for i in range(100):

            #get current state
            currentlevel = player.level
            currentHP = player.getHitPoints()
            currentAttack = player.getDamage()
            
            #make attack
            dieRoll = player.getDieRoll()
            player.hitEnemy(15, 10) # Make a guaranteed hit

            
            #check for level up
            if (player.level > currentlevel): # player leveled up
                self.assertTrue(player.getHitPoints() == currentHP + 5 + player.getModifier(player.abilities.get("CONSTITUTION")))
                if (player.level % 2 == 0):
                    self.assertTrue(player.hitEnemy(11-(int(player.level/2)), 10)) #make sure player has bonus to hit gained on increase levels
                      

if __name__ == '__main__':
    unittest.main()

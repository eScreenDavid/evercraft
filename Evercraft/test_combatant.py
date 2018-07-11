
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
        if(dieRoll < opponent.getArmor()):
            self.assertFalse(opponent.checkHit(dieRoll))
        else:
            self.assertTrue(opponent.checkHit(dieRoll))

    def test_damage(self):
        damage_amount = 1 # 1 damage is the base amount if a hit is successful
        player = Combatant()
        player1.attacked(player1.getDieRoll(), damage_amount)
        if player1.getHP <= 0:
            self.assertFalse(player1.isAlive())
        else:
            self.assertTrue(player1.getAlive())

if __name__ == '__main__':
    unittest.main()

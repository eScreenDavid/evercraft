
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
        player = Combatant()
        player.attacked(player.getDieRoll())
        if player.getHitPoints() <= 0:
            self.assertFalse(player.isAlive())
        else:
            self.assertTrue(player.isAlive())


if __name__ == '__main__':
    unittest.main()

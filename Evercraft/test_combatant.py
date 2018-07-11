
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

    def test_is_alive(self):
        player = Combatant()
        player.attacked(player.getDieRoll())
        self.assertTrue(player.isAlive())

    def test_is_dead(self):
        player = Combatant()
        player.hitpoints = 1
        player.attacked(player.getDieRoll())
        self.assertFalse(player.isAlive())


if __name__ == '__main__':
    unittest.main()

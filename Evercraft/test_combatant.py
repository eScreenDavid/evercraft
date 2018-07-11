
import unittest
from Combatant import Combatant


class TestCombatant(unittest.TestCase):

    def test_armor_default(self):
        player = Combatant()
        self.assertEqual(player.getArmor(), 10)

    def test_hitpoint_default(self):
        player = Combatant()
        self.assertEqual(player.getHitPoints(), 5)

    def test_roll_die(self):
        player = Combatant()
        opponent = Combatant()
        dieRoll = player.getDieRoll()
        if(dieRoll < opponent.getArmor()):
            self.assertLess(dieRoll, opponent.getArmor())
        else:
            self.assertGreaterEqual(dieRoll, opponent.getArmor())


if __name__ == '__main__':
    unittest.main()

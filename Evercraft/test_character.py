
import unittest
from Character import Character

class CharacterTest(unittest.TestCase):

    def test_playername(self):
      player = Character()
      player.setName("MasterDonkey")
      self.assertEqual(player.getName(),  "MasterDonkey")

    def test_alignment_good(self):
        player = Character()
        player.setAlignment("Good")
        self.assertEqual(player.getAlignment(), "Good")

    def test_alignment_evil(self):
        player = Character()
        player.setAlignment("Evil")
        self.assertEqual(player.getAlignment(), "Evil")

    def test_alignment_neutral(self):
        player = Character()
        player.setAlignment("Neutral")
        self.assertEqual(player.getAlignment(), "Neutral")
    
    def test_alignment_exception(self):
        player = Character()
        with self.assertRaises(ValueError):
            player.setAlignment('')

    def test_armor_default(self):
        player = Character()
        self.assertEqual(player.getArmor(), 10)

    def test_hitpoint_default(self):
        player = Character()
        self.assertEqual(player.getHitPoints(), 5)

if __name__ == '__main__':
    unittest.main()
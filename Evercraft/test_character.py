
import unittest
from character import Character

class CharacterTest(unittest.TestCase):

    def test_upper(self):
      player = Character()
      player.setName("MasterDonkey")
      self.assertEqual(player.getName(),  "MasterDonkey")

if __name__ == '__main__':
    unittest.main()
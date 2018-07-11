
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

    def test_default_abilities(self):
        playerx = Character()
        self.assertDictEqual(playerx.abilities, {
                             'STRENGTH': 10, 'DEXETERITY': 10, 'CONSTITUTION': 10, 'WISDOM': 10, 'INTELLIGENCE': 10, 'CHARISMA': 10})

    def test_start_modifier(self):
        player = Character()
        self.assertEqual(player.getModifier(1), -5)

    def test_middle_modifier(self):
        player = Character()
        self.assertEqual(player.getModifier(10), 0)

    def test_end_modifier(self):
        player = Character()
        self.assertEqual(player.getModifier(20), 5)

    def test_modifier_out_of_bounds(self):
        player = Character()
        with self.assertRaises(ValueError):
            player.getModifier(21)

    def test_attribute_modifiers_on_strength(self):
        player = Character()
        player.setAttribute("STRENGTH", 13)
        self.assertEqual(player.getDamage(), 2)

    def test_attribute_modifiers_on_dexterity(self):
        player = Character()
        player.setAttribute("DEXTERITY", 7)
        self.assertEqual(player.getArmor(), 8)

    def test_attribute_modifiers_on_constitution(self):
        player = Character()
        player.setAttribute("CONSTITUTION", 18)
        self.assertEqual(player.getHitPoints(), 9)

    def test_attribute_modifiers_boundaries(self):
        player = Character()
        player.setAttribute("STRENGTH", 1)
        self.assertEqual(player.getDamage(), 1)
        player.setAttribute("CONSTITUTION", 1)
        self.assertEqual(player.getHitPoints(), 1)


if __name__ == '__main__':
    unittest.main()

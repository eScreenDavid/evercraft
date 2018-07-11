print("Starting Test...")

from Character.py import Character

print("Starting Test...")

player = Character()
player.setName("MasterDonkey")
assert player.getname() is "MasterDonkey"
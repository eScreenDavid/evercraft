from character import Character

print("Starting Test...")

player = Character()
player.setName("MasterDonkey")
assert player.getName() is "MasterDonkey"
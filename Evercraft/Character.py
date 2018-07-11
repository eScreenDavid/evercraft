
class Character:

    def __init__(self):
        self.name = None
        self.alignment = None
        self.abilities = {
            'STRENGTH': 10,
            'DEXETERITY': 10,
            'CONSTITUTION': 10,
            'WISDOM': 10,
            'INTELLIGENCE': 10,
            'CHARISMA': 10
        }
        self.armor = 10  # defaults to 10
        self.hitpoints = 5  # defaults to 5
        self.damage = 1  # defaults to 1
        self.experience = 0 #defaults to 0

    def getModifier(self, attribute):
        if attribute < 0 or attribute > 20:
            raise ValueError("attribute out of range, must be 1-20")
        modifier = {
            1: -5,
            2: -4,
            3: -4,
            4: -3,
            5: -3,
            6: -2,
            7: -2,
            8: -1,
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5
        }
        return modifier.get(attribute)

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value

    def getAlignment(self):
        return self.alignment

    def setAlignment(self, value):
        if value not in ['Neutral', 'Good', 'Evil']:
            raise ValueError('Alignment not found.')
        self.alignment = value

    def getArmor(self):
        return self.armor

    def getHitPoints(self):
        return self.hitpoints

    def getDamage(self):
        return self.damage

    def setAttribute(self, ability, value):
        self.abilities[ability] = value

        if ability == 'STRENGTH':
            self.damage += self.getModifier(value)
        elif ability == 'DEXTERITY':
            self.armor += self.getModifier(value)
        elif ability == 'CONSTITUTION':
            self.hitpoints += self.getModifier(value)
        else:
            raise ValueError('Attribute not supported')

        if(self.hitpoints < 1):
            self.hitpoints = 1
        if(self.damage < 1):
            self.damage = 1


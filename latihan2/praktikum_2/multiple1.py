class Enemy:

    def __init__(self, name, toughness):
        self.name = name
        self.toughness = toughness

    def move(self):
        print(self.name, " is attacking")

class Zombie:

    def __init__(self, type, weakness):
        self.type = type
        self.weakness = weakness

    def sounds(self):
        print("AaarRRgG The ZoMbiEee has CoMiiNg!")


class FlagZombie(Enemy, Zombie):

    def __init__(self, name, toughness, type, weakness):
        Enemy.__init__(self, name, toughness)
        Zombie.__init__(self, type, weakness)

    def do(self):
        print(self.name, ' is attacking')
        print("The Zombieee has coming to you")


zom = FlagZombie('Bie', 'Low', 'Flag Zombie', 'The low power')
zom.do()
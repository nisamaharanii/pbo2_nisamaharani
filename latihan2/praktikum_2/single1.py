class Enemy:

    def __init__(self, name, toughness):
        self.name = name
        self.toughness = toughness

    def move(self):
        print(self.name, " is attacking")

class Zombie(Enemy):

    def __init__(self, name, toughness, type, weakness):
        super().__init__(name, toughness)
        self.type = type
        self.weakness = weakness

    def sounds(self):
        print("AaarRRgG The ZoMbiEee has CoMiiNg!")

zombie = Zombie("Zomboos", 'Low', "Regular Garden-variety Zombie", 'The low power')
print(zombie.__dict__)
zombie.move() 
zombie.sounds() 
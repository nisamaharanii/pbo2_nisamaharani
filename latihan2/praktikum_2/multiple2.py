class Hero:

    def __init__(self, name, toughness):
        self.name = name
        self.toughness = toughness

    def move(self):
        print(self.name, " is showing its power")

class Plant:

    def __init__(self, recharge, cost, power):
        self.recharge = recharge
        self.cost = cost
        self.power = power

    def plantpower(self):
        print(f'my power is  {self.power}  ready to remove ZOMBIE from the world')


class CherryBombs(Hero, Plant):

    def __init__(self, name, toughness, recharge, cost, power):
        Hero.__init__(self, name, toughness)
        Plant.__init__(self, recharge, cost, power)

    def do(self):
        print(self.name,' is hero which will save you from the zombie\'s attacked')


cheri = CherryBombs('Rybom', 'Massive', 'Very slow', '150', 'Blow up all zombies in an area')
cheri.do()
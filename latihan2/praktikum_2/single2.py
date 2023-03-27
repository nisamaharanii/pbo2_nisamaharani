class Hero:

    def __init__(self, name, toughness):
        self.name = name
        self.toughness = toughness

    def move(self):
        print(self.name,' is showing its power')


class Plant(Hero):
    
    def __init__(self, name, toughness, recharge, cost, power):
        super().__init__(name, toughness)
        self.recharge = recharge
        self.cost = cost
        self.power = power

    def desc(self):
        print(f'Hello Zombie!!, i am ', {self.name}, ' ready to remove you from the world')


plant = Plant('Peashooters','Normal','Fast',100,'Shoot peas at attacking zombies')
print(plant.__dict__)
plant.move()
plant.desc()
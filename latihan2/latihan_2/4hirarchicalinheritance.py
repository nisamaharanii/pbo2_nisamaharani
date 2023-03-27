class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    

class Mammal(Animal):

    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur

    def get_fur(self):
        return self.fur
    

class Bird(Animal):

    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan

    def get_wingspan(self):
        return self.wingspan

# Hierarchical Inheritance
class Reptile(Mammal):

    def __init__(self, name, color, fur, scale):
        super().__init__(name, color, fur)
        self.scale = scale

    def get_scale(self):
        return self.scale
    
Kura2 = Reptile('Turtla', 'Brown', 'No fur', '70x20 cm')
print('Name\t: ',Kura2.get_name())
print('Color\t: ',Kura2.get_color())
print('Fur\t: ',Kura2.get_fur())
print('Scale\t: ',Kura2.get_scale())
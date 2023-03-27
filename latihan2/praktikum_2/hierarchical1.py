class Virus:

    def __init__(self, name, molekul):
        self.name = name
        self.molekul = molekul

    def get_name(self):
        return self.name
    
    def get_molekul(self):
        return self.molekul
    

class VirusCategory(Virus):

    def __init__(self, name, molekul, category):
        super().__init__(name, molekul)
        self.category = category

    def get_category(self):
        return self.category
    

class VirusUsage(Virus):

    def __init__(self, name, molekul, utilization):
        super().__init__(name, molekul)
        self.utilization = utilization

    def get_utilization(self):
        return self.utilization

# Hierarchical Inheritance
class VirusVacsin(VirusUsage):

    def __init__(self, name, molekul, utilization, vaksin_for):
        super().__init__(name, molekul, utilization)
        self.vaksin_for = vaksin_for

    def get_vaksin_for(self):
        return self.vaksin_for
    
virusscandal = VirusVacsin('Varicella zoster', 'DNA genom',  'Producing vaccsines', 'Smallpox')
print('Name\t\t: ',virusscandal.get_name())
print('Molekul\t\t: ',virusscandal.get_molekul())
print('Utilization\t: ',virusscandal.get_utilization())
print('Usage\t\t: ',virusscandal.get_vaksin_for())
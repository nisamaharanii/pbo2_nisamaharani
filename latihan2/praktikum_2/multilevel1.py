class Protista:

    def __init__(self, name, group):
        self.name = name
        self.group = group

    def get_details(self):
        print(f"Name\t\t: {self.name}")
        print(f"Group\t\t: {self.group}")


class ProtistaClasification(Protista):

    def __init__(self, name, group, sel, sifat):
        super().__init__(name, group)
        self.sel = sel
        self.sifat = sifat

    def get_details(self):
        super().get_details()
        print(f"Sel\t\t: {self.sel}")
        print(f"Sifat\t\t: {self.sifat}")


class Ciliata(ProtistaClasification):

    def __init__(self, name, group, sel, sifat, cara_gerak):
        super().__init__(name, group, sel, sifat)
        self.cara_gerak = cara_gerak

    def get_details(self):
        super().get_details()
        print(f"Cara gerak\t: {self.cara_gerak}")


manager = Ciliata('Ciliata', 'Protista mirip hewan', 'Sel tunggal','Heterotrof', 'Bergerak dengan rambut getar (silia)')
manager.get_details()
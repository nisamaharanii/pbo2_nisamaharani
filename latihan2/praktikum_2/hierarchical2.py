class Bakteri:

    def __init__(self, nama, kapsul):
        self.nama = nama
        self.kapsul = kapsul

    def get_nama(self):
        return self.nama
    
    def get_kapsul(self):
        return self.kapsul
    

class BacterialGrouping(Bakteri):

    def __init__(self, nama, kapsul, pengelompokan):
        super().__init__(nama, kapsul)
        self.kelompok = pengelompokan

    def get_kelompok(self):
        return self.kelompok
    

class BacteriShape(Bakteri):

    def __init__(self, nama, kapsul, bentuk):
        super().__init__(nama, kapsul)
        self.bentuk = bentuk

    def get_bentuk(self):
        return self.bentuk

# Hierarchical Inheritance
class Stafilokokus(BacteriShape):

    def __init__(self, nama, kapsul, bentuk, jenis ):
        super().__init__(nama, kapsul, bentuk)
        self.jenis = jenis

    def get_jenis(self):
        return self.jenis
    
stafil = Stafilokokus('Staphylococcus aureus', 'Tidak berkapsul', 'Kokus(bulat)', 'Stafilokokus')
print('Nama bakteri\t: ',stafil.get_nama())
print('Kapsul\t\t: ',stafil.get_kapsul())
print('Bentuk\t\t: ',stafil.get_bentuk())
print('Jenis\t\t: ',stafil.get_jenis())

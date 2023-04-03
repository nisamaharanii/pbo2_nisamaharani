class BangunRuang:
    def volume(self):
        pass

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi **3
    
balok = Balok(2,3,4)
A = balok.volume()
print(A)

kubus = Kubus(4)
B = kubus.volume()
print(B)



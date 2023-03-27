class Kendaraan:

    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berkendara(self):
        print(f"Kendaraan ini ({self.jenis} {self.merk} berwarna {self.warna}) sedang melaju.")

class SepedaMotor(Kendaraan):
    
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    
    def belok(self):
        print(f"Sepeda motor dengan cc {self.cc}  berbelok ke kanan.")

motorA = SepedaMotor("Sepeda Motor", "scoopy", "hitam", 150)
motorA.berkendara() 
motorA.belok() 

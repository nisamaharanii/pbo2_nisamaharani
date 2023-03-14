'''
Nama    : Nisa Maharani
Nim     : 210511136
kelas   : R4 (T121D)
'''
class Mobil:
    def __init__(self, merk, warna, nomor_polisi):
        self.merk = merk
        self.warna = warna
        self.nomor_polisi = nomor_polisi

    def info(self):
        print(f'Mobil {self.merk} berwarna {self.warna} dengan nomor polisi {self.nomor_polisi}')

MobilA = Mobil('Xenia', 'Putih', 'E 1997 DF')
MobilA.info()
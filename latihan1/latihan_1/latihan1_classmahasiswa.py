'''
Nama    : Nisa Maharani
Nim     : 210511136
kelas   : R4 (T121D)
'''
class mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f'Nama\t: {self.nama} \nNim\t: {self.nim}')

mahasiswaA = mahasiswa('Nisa Maharani', '210511136')
mahasiswaA.info()
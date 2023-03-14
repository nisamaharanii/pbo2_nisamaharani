class mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f'Nama\t: {self.nama} \nNim\t: {self.nim}')

mahasiswaA = mahasiswa('Nisa Maharani', '210511136')
mahasiswaA.info()
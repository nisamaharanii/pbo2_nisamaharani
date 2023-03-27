class Fungi:

    def __init__(self, nama, bentuk, warna):
        self.nama = nama
        self.bentuk = bentuk
        self.warna = warna

    def get_info(self):
        print(f'Nama\t: {self.nama}')
        print(f'Bentuk\t: {self.bentuk}')
        print(f'warna\t: {self.warna}')

    
class Zygomycota(Fungi):

    def __init__(self, nama, bentuk, warna, sifat):
        super().__init__(nama,bentuk,warna)
        self.sifat = sifat

    def get_info(self):
        super().get_info()
        print(f'Sifat\t: {self.sifat}')


class Rhizopus(Zygomycota):

    def __init__(self, nama, bentuk, warna, sifat, peran):
        super().__init__(nama, bentuk, warna, sifat)
        self.peran = peran

    def get_info(self):
        super().get_info()
        print(f'Peran\t: {self.peran}')


mycota = Rhizopus('Rhizopus Oryzae', 'Stolon berdinding halus', 'Koloni berwarna putih berangsur-angsur menjadi abu-abu', 'Saprofit', 'Pembuatan tempe')
print(mycota.get_info())
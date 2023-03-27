class Hewan:

    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat

    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")

class Reptil:
    
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Amphibi:

    def __init__(self, metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat

    def display_info(self):
        print(f"Habitat: {self.habitat}")
        print(f"Metamorfosis: {self.metamorfosis}")

class Salamander(Hewan, Reptil, Amphibi):

    def __init__(self, nama, umur, jenis, habitat, metamorfosis):
        Hewan.__init__(self, jenis, habitat)
        Reptil.__init__(self, nama, umur)
        Amphibi.__init__(self, habitat, metamorfosis)

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        super().display_info() #menampilkan info superclass
        print(f"Metamorfosis: {self.metamorfosis}")

# contoh penggunaan
salamander = Salamander("Salamander", 2, "Reptil-Amphibi", "Air dan daratan", "Telur")
salamander.display_info()
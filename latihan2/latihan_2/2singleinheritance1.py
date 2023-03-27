class Manusia:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):

    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar di dalam kelas.")

dosenA = Dosen("Amira", 35, "132546")
dosenA.berbicara() # Output: Amira sedang berbicara.
dosenA.mengajar() # Output: Amira dengan NIP 132546 sedang mengajar di dalam kelas.
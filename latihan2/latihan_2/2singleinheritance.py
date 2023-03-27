class Hewan:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "bergerak dan bersuara")

class Kucing(Hewan):

    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def bersuara(self):
        print("Meow meow!")

kucingA = Kucing("Unyil", 1, "Himalayan")
kucingA.bergerak() # output: Unyil bergerak dan bersuara
kucingA.bersuara() # output: Meow!
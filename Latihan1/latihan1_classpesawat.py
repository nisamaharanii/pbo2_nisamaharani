class PesawatTerbang :
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan

    def info(self):
        print(f' Maskapai {self.maskapai} dengan tujuan {self.tujuan}')
    
pesawatA = PesawatTerbang('Lion Air','Kuala Lumpur')
pesawatA.info()
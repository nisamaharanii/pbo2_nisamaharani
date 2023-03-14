class Buku :
    def __init__(self, Judul, Penulis, Penerbit):
        self.Judul = Judul
        self.penulis = Penulis 
        self.penerbit = Penerbit

    def info(self):
        print(f'''
        Judul Buku  : {self.Judul} 
        Penulis     : {self.penulis}
        Penerbit    : {self.penerbit}
        ''')

bukuC = Buku('Harry Potter And The Chamber Of Secrets', 'J.K. Rowling', 'PT. gramedia Pustaka Utama')
bukuC.info()
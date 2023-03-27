class Universitas:
  def __init__(self):
    self.univ = "Universitas Muhammadiyah Cirebon"
  def display(self):
    print(f"Nama Universitas\t: {self.univ}")


class Matkul(Universitas):
  def __init__(self):
    Universitas.__init__(self)
    self.course = "Pemograman Berorientasi Objek"
  def display(self):  
    print(f"Nama mata kuliah\t: {self.course}")
    Universitas.display(self)


class Prodi(Universitas):
  def __init__(self):
    self.Prodi = "Teknik Informatika"
  def display(self):  
    print(f"Nama program studi\t: {self.Prodi}")


class Mahasiswa(Matkul, Prodi):
  def __init__(self):
    self.name = "Nisa Maharani"
    Prodi.__init__(self)
    Matkul.__init__(self)
  def display(self):
    print(f"Nama mahasiswa\t\t: {self.name}")
    Prodi.display(self)
    Matkul.display(self)


ob = Mahasiswa()  
print()
ob.display()    
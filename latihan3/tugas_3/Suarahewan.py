from playsound import *

class Animal:
    def make_sound(self):
        pass

class Anjing(Animal):
    def make_sound(self):
        playsound('anjing.mp3')

class Kucing(Animal):
    def make_sound(self):
        playsound('kucing.mp3')

class Ayam(Animal):
    def make_sound(self):
        playsound('ayam.mp3')

class Gajah(Animal):
    def make_sound(self):
        playsound('gajah.mp3')

class Kambing(Animal):
    def make_sound(self):
        playsound('kambing.mp3')

class Kelelawar(Animal):
    def make_sound(self):
        playsound('kelelawar.mp3')

class Sapi(Animal):
    def make_sound(self):
        playsound('sapi.mp3')

class Serigala(Animal):
    def make_sound(self):
        playsound('serigala.mp3')

class Burung(Animal):
    def make_sound(self):
        playsound('burung.mp3')

class Ular(Animal):
    def make_sound(self):
        playsound('ular.mp3')

def animal_sound(hewan):
    hewan.make_sound()

print('Mengenal Suara Binatang'.center(70,'='))
print('Cari tau suara suara binatang yuk! ')
print('Suara apa yang ingin kamu dengarkan? ')
print('''
    1. anjing
    2. kucing
    3. ayam
    4. gajah
    5. kambing
    6. kelelawar
    7. sapi
    8. serigala
    9. burung
    10. ular
    11. tidak
    ''')

hewan = input('Jawab ya! (anjing? kucing? tidak?) ')

if hewan == 'tidak':
    pass
    
elif hewan == 'anjing' :
    anjing = Anjing()  
    print(f"Mari dengarkan Suara Anjing")
    animal_sound(anjing)

elif hewan == 'kucing' :
    kucing = Kucing()  
    print(f"Mari dengarkan Suara Kucing")
    animal_sound(kucing)

elif hewan == 'ayam' :
    ayam = Ayam()  
    print(f"Mari dengarkan Suara Ayam")
    animal_sound(ayam)

elif hewan == 'gajah' :
    gajah = Gajah()  
    print(f"Mari dengarkan Suara Gajah")
    animal_sound(gajah)

elif hewan == 'kambing' :
    kambing = Kambing()  
    print(f"Mari dengarkan Suara Kambing")
    animal_sound(kambing)

elif hewan == 'kelelawar' :
    kelelawar = Kelelawar()  
    print(f"Mari dengarkan Suara Kelelawar")
    animal_sound(kelelawar)

elif hewan == 'sapi' :
    sapi = Sapi()  
    print(f"Mari dengarkan Suara Sapi")
    animal_sound(sapi)

elif hewan == 'serigala' :
    serigala = Serigala()  
    print(f"Mari dengarkan Suara Serigala")
    animal_sound(serigala)

elif hewan == 'burung' :
    burung = Burung()  
    print(f"Mari dengarkan Suara Burung")
    animal_sound(burung)

elif hewan == 'ular' :
    ular = Ular()  
    print(f"Mari dengarkan Suara Ular")
    animal_sound(ular)

else:
    print('Isi sesuai daftar nama hewan diatas yaaa :)')

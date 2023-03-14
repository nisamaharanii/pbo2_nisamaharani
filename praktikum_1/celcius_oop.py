'''
Nama    : Nisa Maharani
Nim     : 210511136
Kelas   : R4
'''
class Celcius:
    def __init__(self, celcius):
        self.celcius = celcius

    def Fahrenheit(self):
        return (self.celcius * 9/5) + 32
    
    def Kelvin(self):
        return self.celcius + 273.15
    
    def Reamur(self):
        return self.celcius * 4/5
    
print('KONVERSI CELCIUS OOP'.center(70)) 
print('_'*70) 

C_F = 75
celciusA = Celcius(C_F)
print('Konversi', C_F,  'derajat celcius adalah ', {celciusA.Fahrenheit()}, 'derajat fahrenheit\n' ) 

C_R = 60
CelciusB = Celcius(C_R)
print('Konversi', C_R , 'derajat celcius adalah ', {CelciusB.Reamur()}, 'derajat reamur\n' ) 

C_K = 90
CelciusC = Celcius(C_K)
print('Konversi', C_K , 'derajat celcius adalah ', {CelciusC.Kelvin()}, 'derajat kelvin' ) 
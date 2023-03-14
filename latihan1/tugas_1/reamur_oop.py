'''
Nama    : Nisa Maharani
Nim     : 210511136
Kelas   : R4
'''
class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur

    def Fahrenheit(self):
        return (self.reamur * 2.25) + 32
    
    def Kelvin(self):
        return self.reamur/0.8 + 273.15
    
    def Celcius(self):
        return self.reamur / 0.8
    
print('_'*75) 
print('KONVERSI REAMUR OOP'.center(70)) 
print('_'*75) 

R_F = 75
reamurA = Reamur(R_F)
print('Konversi', R_F,  'derajat reamur adalah ', {reamurA.Fahrenheit()}, 'derajat fahrenheit\n' ) 

R_C = 60
reamurB = Reamur(R_C)
print('Konversi', R_C , 'derajat reamur adalah ', {reamurB.Celcius()}, 'derajat celcius\n' ) 

R_K = 90
reamurC = Reamur(R_K)
print('Konversi', R_K , 'derajat reamur adalah ', {reamurC.Kelvin()}, 'derajat kelvin' ) 
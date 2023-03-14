'''
Nama    : Nisa Maharani
Nim     : 210511136
Kelas   : R4
'''
class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def Fahrenheit(self):
        return (self.kelvin * 9/5) - 459.67
    
    def Reamur(self):
        return 4/5 * (self.kelvin - 273)
    
    def Celcius(self):
        return self.kelvin - 273.15
    
print('_'*75) 
print('KONVERSI KELVIN OOP'.center(70)) 
print('_'*75) 

R_F = 75
kelvinA = Kelvin(R_F)
print('Konversi', R_F,  'derajat kelvin adalah ', {kelvinA.Fahrenheit()}, 'derajat fahrenheit\n' ) 

R_C = 60
reamurB = Kelvin(R_C)
print('Konversi', R_C , 'derajat kelvin adalah ', {reamurB.Celcius()}, 'derajat celcius\n' ) 

R_K = 90
reamurC = Kelvin(R_K)
print('Konversi', R_K , 'derajat kelvin adalah ', {reamurC.Reamur()}, 'derajat reamur' ) 
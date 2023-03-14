'''
Nama    : Nisa Maharani
Nim     : 210511136
Kelas   : R4
'''
class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def Celcius(self):
        return (self.fahrenheit - 32) * 5/9
    
    def Kelvin(self):
        return (self.fahrenheit + 459.67) * 5/9
    
    def Reamur(self):
        return 4/9 * (self.fahrenheit - 32)
    
print('_'*75) 
print('KONVERSI FAHRENHEIT OOP'.center(70)) 
print('_'*75) 

F_C = 75
fahrenheitA = Fahrenheit(F_C)
print('Konversi', F_C,  'derajat fahrenheit adalah ', {fahrenheitA.Celcius()}, 'derajat celcius\n' ) 

F_R = 60
fahrenheitB = Fahrenheit(F_R)
print('Konversi', F_R , 'derajat fahrenheit adalah ', {fahrenheitB.Reamur()}, 'derajat reamur\n' ) 

F_K = 90
fahrenheitC = Fahrenheit(F_K)
print('Konversi', F_K , 'derajat fahrenheit adalah ', {fahrenheitC.Kelvin()}, 'derajat kelvin' ) 
'''
Nama    : Nisa Maharani
Nim     : 210511136
Kelas   : R4
'''
class Celcius:
    @staticmethod
    def Fahrenhait(celcius):
        return (celcius * 9/5) + 32
    
    @staticmethod
    def Kelvin(celcius):
        return celcius + 273.15
    
    @staticmethod
    def Reamur(celcius):
        return celcius * 4/5

print('KONVERSI CELCIUS'.center(70)) 
print('_'*70) 

brpcelcius = 75
print('Konversi', brpcelcius, 'derajat celcius adalah ', {Celcius.Fahrenhait(brpcelcius)}, 'derajat fahrenheit\n' ) 

brpcelcius1 = 60
print('Konversi', brpcelcius1, 'derajat celcius adalah ', {Celcius.Reamur(brpcelcius1)}, 'derajat reamur\n' ) 

brpcelcius2 = 90
print('Konversi', brpcelcius2, 'derajat celcius adalah ', {Celcius.Kelvin(brpcelcius2)}, 'derajat kelvin' ) 

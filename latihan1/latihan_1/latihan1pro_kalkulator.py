'''
Nama    : Nisa Maharani
Nim     : 210511136
kelas   : R4 (T121D)
'''
class kalkulator:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def subtrac(x,y):
        return x - y
    
    @staticmethod
    def multiply(x,y):
        return x * y
    
    @staticmethod
    def divide(x,y):
        if y == 0:
            raise ValueError('Tidak dapat membagi nol')
        return x / y
    
    
    @staticmethod
    def mod(x,y):
        return x % y
    
    @staticmethod
    def floordivision(x,y):
        return x // y
    
print(f'Pertambahan\t= {kalkulator.add(1,2)}')
print(f'Pengurangan\t= {kalkulator.subtrac(4,2)}')
print(f'Perkalian\t= {kalkulator.multiply(3,5)}')
print(f'Pembagian\t= {kalkulator.divide(7,6)}')
print(f'Modulus\t\t= {kalkulator.mod(9,8)}')
print(f'Floor Division\t= {kalkulator.floordivision(13,10)}')
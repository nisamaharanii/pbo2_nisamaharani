class Matematika:
    def subtraction(self, a, b):
        return a - b
    
    def subtraction(self, a, b, c=0):
        return a - b - c
    
mat = Matematika()
B = mat.subtraction(3, 2, 1)
print(B)

mut = Matematika()
C = mut.subtraction(7,3)
print(C)
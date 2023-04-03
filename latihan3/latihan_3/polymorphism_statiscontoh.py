#Contoh 1:
print('Penggunaan fungsi “len” pada berbagai tipe data:')
print(len("Hello")) # output: 5
print(len([1, 2, 3])) # output: 3
print(len((1, 2, 3))) # output: 3
print(len({1, 2, 3})) # output: 3
print()

#Contoh 2:
print('Penggunaan operator “+” pada berbagai tipe data:')
print(2 + 3) # output: 5
print("Hello" + " World") # output: Hello World
print([1, 2] + [3, 4]) # output: [1, 2, 3, 4]
print((1, 2) + (3, 4)) # output: [1, 2, 3, 4]
print(False + False) 
print(True + True) 
print()

#Contoh 3:
print('Penggunaan fungsi “max&min” pada berbagai tipe data:')
print(max(2, 5)) # output: 5
print(min(2, 5)) # output: 2
print(max([1, 2, 3])) # output: 3
print(max("Hello")) # output: "o"
print(min("Hello")) # output: "H"
print()

#Contoh 4:
print('Penggunaan metode “sort” pada berbagai tipe data:')
a = [3, 1, 2]
a.sort()
print(a) # output: [1, 2, 3]
b = ["c", "a", "b"]
b.sort()
print(b) # output: ["a", "b", "c"]
c = [1.2, 1.1, 1.01]
c.sort()
print(c)

# A = [1/x for x in range(1,11)]
# print(A)
# B = [2**i for i in range(11)]
# print(B)
# C = [x for x in B if x % 4 == 0]
# print(C)


# D = [[1, 2, 3, 4], 
#      [4, 5, 6, 7],
#      [7, 8, 9, 1],
#      [8, 7, 4, 5]]

# E = [D[x][x] for x in range(4) ]
# print(E)


# slownik = {
#     "Woda": "Litry",
#     "Jajka": "Sztuki",
#     "Ziemniaki": "Kilogramy",
#     "Pomidory" : "Sztuki"
# }

# F = {a for (a,b) in slownik.items() if b == "Sztuki"}
# print(F)


# import math
# def monotonicznosc(a, b) :
#     if (a > 0):
#         return print("Funkcja rosnąca")
#     elif (a < 0):
#         return print("Funkcja malejąca")
#     else:
#         return print("Funkcja stała")
# monotonicznosc(3, 3)


# import math
# def zad5(a1,b1,a2,b2):
#     if (a1 == a2):
#         return print("Równoległe")
#     elif (a1*a2 == -1):
#         return print("Prostopadłe")
#     else:
#         return print("Przecinające, nie prostopadłe")
# zad5(5,3,-1/5,5)


# import math
# def zad6(a,b):
#     return print (math.sqrt((0-a)**2 + (0-b)**2))
# zad6(6, 6)


# import math
# def zad7(a,b):
#     return print (math.sqrt(a**2 + b**2))
# zad7(3, 4)


# import math
# def zad8(a1,r,i):
#     A = [a1+r*z for z in range(i)]
#     print(A)
#     print (sum(A))
# zad8(1,1,10)


# import math
# def zad9(a1,r,i):
#     A = [a1+r*z for z in range(i)]
#     print(A)
#     print (math.prod(A))
# zad9(1,1,10)


def zad10(** rzeczy):
    wynik = 0
    for ilosc in rzeczy:
        wynik = wynik + rzeczy[ilosc]
    return print(wynik)
zad10(pomidory=10,ziemniaki=20,marchewka=3,nic=5)
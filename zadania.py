# class Material:
#     def __init__(self, rodzaj, dlugosc, szerokosc):
#         self.rodzaj=rodzaj
#         self.dlugosc=dlugosc
#         self.szerokosc=szerokosc
#         self.opis = "Odzież"
    
#     def wyswietl_nazwe(self):
#         return self.rodzaj

# class Ubrania(Material):
#     def __init__(self, rozmiar, kolor, dla_kogo):
#         self.rozmiar =rozmiar
#         self.kolor=kolor
#         self.dla_kogo=dla_kogo

#     def wyswietl_dane(self):
#         return self.rozmiar,self.kolor,self.dla_kogo

# class Sweter(Ubrania):
#     def __init__(self, rodzaj_swetra):
#         self.rodzaj_swetra=rodzaj_swetra
    
#     def wyswietl_dane(self):
#         return self.rodzaj_swetra

# odziez1 = Material("sweter",180,60)
# odziez2 = Ubrania("XL","czerwony","Władysław")
# odziez3 = Sweter("golf")

# print(odziez1.wyswietl_nazwe())
# print(odziez2.wyswietl_dane())
# print(odziez3.wyswietl_dane())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Kwadrat():
#     def __init__(self, x):
#         self.x = x
#         self.y = x

#     def pole(self):
#         return self.x * self.y

#     def __add__(self,other):
#         return self.x + other.x

#     def __ge__(self,other):
#         return self.x >= other.x

#     def __gt__(self,other):
#         return self.x > other.x

#     def __le__(self,other):
#         return self.x <= other.x

#     def __lt__(self,other):
#         return self.x < other.x

# f1 = Kwadrat(5)
# f2 = Kwadrat(10)

# print(f1 + f2)
# print(f1 >= f2)
# print(f1 > f2)
# print(f1 <= f2)
# print(f1 < f2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Point:
#     __counter = []

#     def __init__(self, x=0, y=0):
#         """Konstruktor punktu."""
#         self.x = x
#         self.y = y

#     def update(self, n):
#         self.__counter.append(n)

# p1 = Point(0,0)
# p2 = Point(1,1)
# p3 = Point(2,1)
# p4 = Point(1,2)

# print(p1._Point__counter)
# print(p2._Point__counter)
# p1.update(1)
# print(p1._Point__counter)
# print(p2._Point__counter)
# p2.update(2)
# print(p3._Point__counter)
# print(p4._Point__counter)
# p3.update(5)
# print(p1._Point__counter)
# print(p2._Point__counter)
# p4.update(3)
# print(p3._Point__counter)
# print(p4._Point__counter)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Osoba:

#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko

#     def przedstaw_sie(self):
#         return "{} {}".format(self.imie, self.nazwisko)


# class Pracownik(Osoba):

#     def __init__(self, imie, nazwisko, pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         # lub
#         # super().__init__(imie, nazwisko)
#         self.pensja = pensja

#     def przedstaw_sie(self):
#         return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


# class Menadzer(Pracownik):

#     def przedstaw_sie(self):
#         return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


# jozek = Pracownik("Józek", "Bajka", 2000)
# adrian = Menadzer("Adrian", "Mikulski", 12000)

# print(jozek.przedstaw_sie())
# print(adrian.przedstaw_sie())
# print (isinstance(jozek,Pracownik))
# print (issubclass(Pracownik,Osoba))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class Wspak:
#     """Iterator zwracający wartości w odwróconym porządku"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         if isinstance(self.data,str):
#             return self

#     # def __next__(self):
#     #     if self.index == 0:
#     #         raise StopIteration
#     #     self.index = self.index - 1
#     #     if self.index % 2 == 0:
#     #         return print(self.data[self.index])

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         if self.data[self.index] in ['A','a','E','e','I','i','O','o','U','u','Y','y']:
#             return print(self.data[self.index])


# wyraz = Wspak("autos") 
# it = iter(wyraz)
# print(it)
# next(it)
# next(it)
# next(it)
# next(it)
# next(it)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def reverse(data):
#     for index in range(len(data)-1, -1, -2):
#         yield data[index]


# gen = reverse("Feliks")
# print(next(gen))
# print(next(gen))
# print(next(gen))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import itertools

# lista = [0,1,2,3,4,5,6,7,8,9]
# for a,b,c in itertools.combinations(lista,3):
#     print (a,b,c)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def fibbonacci():
#     a,b = 1,1
#     yield a
#     yield b
#     while True:
#         a,b = b,a+b
#         yield b

# g = fibbonacci()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def miesiace():
    for miesiac in ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]:
        yield miesiac

g = miesiace()

print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))
print (next(g))


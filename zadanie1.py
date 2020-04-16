# plik = open("dane.txt","w+")
# liczby = []
# for x in range(0,101,4):
#     liczby += [x]
# plik.writelines(str(liczby))
# plik.close()

# with open("dane.txt","r") as plik:
#     for linia in plik:
#         print(linia,end="")

# with open("dane.txt", "w+") as plik:
#     liczby = []
#     for x in range(0,51,2):
#         liczby += [x]
#     plik.writelines(str(liczby))
#     print(liczby, end="")

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#         self.opis = "Lista zakupów"
    
#     def wyswietl_produkt(self):
#         return self.nazwa_produktu, str(self.ilosc) + " " + self.jednostka_miary, str(self.cena_jed) + "" + "zł" + "/" + str(self.jednostka_miary)
#     def ile_produktu(self):
#         return str(self.ilosc) + " " + self.jednostka_miary 
#     def ile_kosztuje(self):
#         return str(self.cena_jed * self.ilosc) + " " + "zł"

# produkt = NaZakupy("Ziemniaki",10,"kg",2)
# produkt2 = NaZakupy("Jajka",5,"szt",1)

# print(produkt.wyswietl_produkt())
# print(produkt2.ile_produktu())
# print(produkt.ile_kosztuje())

# class ciagi:
#     def __init__(self, a1, n, r):
#         self.a1=a1
#         self.n=n
#         self.r=r
#         self.opis = "ciagi arytmetyczne"

#     def __del__(self):
#         print ("usunięto")
    
#     def wyswietl_dane(self):
#         lista = [self.a1+self.r*z for z in range(self.n)]
#         return lista

#     def pobierz_elementy(self,n):
#         lista = [self.a1+self.r*z for z in range(self.n)]
#         return lista[n-1]

#     def pobierz_parametry(self):
#         return "pierwszy wyraz:" + " " + str(self.a1),"ilość wyrazów:" + " " +  str(self.n),"różnica:" + " " + str(self.r)

#     def policz_sume(self):
#         lista = [self.a1+self.r*z for z in range(self.n)]
#         return sum(lista)

#     def policz_elementy(self,n):
#         listwa = [self.a1+self.r*z for z in range(n)]
#         return listwa

# ciag1 = ciagi(1,10,5)
# ciag2 = ciagi(5,6,2)

# print(ciag1.wyswietl_dane())
# print(ciag1.pobierz_elementy(5))
# print(ciag1.pobierz_parametry())
# print(ciag1.policz_sume())
# print(ciag1.policz_elementy(5))
# del ciag2
# print(ciag2.policz_sume())

# class Slowa:
#     def __init__(self, slowo,slowo2):
#         self.slowo=slowo
#         self.slowo2=slowo2
#         self.opis = "Słownictwo"
    
#     def wyswietl_wyrazy(self):
#         return self.slowo,self.slowo2

#     def sprawdz_czy_palindrom(self):
#         return self.slowo2 == self.slowo2[::-1]

#     def sprawdz_czy_anagram(self):
#         return sorted(self.slowo) == sorted(self.slowo2)
    
#     def sprawdz_czy_metagramy(self):
#         listwa1 = list(set(sorted(self.slowo)) - set(sorted(self.slowo2)))
#         if (len(listwa1)>=2):
#             return "nie jest metagramem"
#         else:
#             return "jest metagramem"


# slowka = Slowa("lbcten","silent")

# print(slowka.wyswietl_wyrazy())
# print(slowka.sprawdz_czy_palindrom())
# print(slowka.sprawdz_czy_anagram())
# print(slowka.sprawdz_czy_metagramy())

class Robaczek:
    def __init__(self, x, y, krok):
        self.x=x
        self.y=y
        self.krok=krok
        self.opis = "Handicapped Snake"
    
    def idz_w_gore(self,ilosc_krok):
        self.y = self.y + self.krok * ilosc_krok
        return "ruszyłeś " + str(self.krok * ilosc_krok) + " " + "kroków w górę"

    def idz_w_dol(self,ilosc_krok):
        self.y = self.y - self.krok * ilosc_krok
        return "ruszyłeś " + str(self.krok * ilosc_krok) + " " + "kroków w dół"

    def idz_w_lewo(self,ilosc_krok):
        self.x = self.x - self.krok * ilosc_krok
        return "ruszyłeś " + str(self.krok * ilosc_krok) + " " + "kroków w lewo"
    
    def idz_w_prawo(self,ilosc_krok):
        self.x = self.x + self.krok * ilosc_krok
        return "ruszyłeś " + str(self.krok * ilosc_krok) + " " + "kroków w prawo"
    
    def pokaz_gdzie_jestes(self):
        return self.x, self.y

snake = Robaczek(0,0,1)

print(snake.idz_w_gore(6))
print(snake.idz_w_lewo(12))
print(snake.idz_w_prawo(4))
print(snake.pokaz_gdzie_jestes())

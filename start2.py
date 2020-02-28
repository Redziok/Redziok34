print("Hello world!")

def dluga_nazwa_funkcji():
    printf("Hello world!")

# dlugaNazwaFunkcji
# Guido van Rossum
# pep8 pep0008

# Ctrl + / - ustaw komentarz/usuń komentarz
# Shift + Alt + strzałka góra/dół powielanie
# """ parametry: ... """ tzw. docstring
# łańcuch znaków 

imie = "Ala"
imie = 'Ala'
imie = """Ala
ma
kota
głodnego"""

print(type(imie))
# <class 'str'>
imie = str("Ala") # poprzez konstruktor
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isinstance() sprawdzamy czy zmienna jest danego typu
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print("Ala " + "ma kota")
# print("Ala " + "ma " + 5 + " kotów") błąd
print("Ala " + "ma " + str(5) + " kotów")
print(5)
ilosc_kotow = 6
print("Ala " + f"ma {ilosc_kotow} kotów")
liczba = 6.857564746
print(f"Liczba {liczba:.2f}") # 2 miejsca dziesiętne
# http://pyformat.info

print(imie[0])
# imie[0] = "O" nie jest mutowalny
imie.lower()
print(imie)

#liczby
liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) # dzielenie bez reszty
print(1 ** 2) # potęgowaie
print(1 % 2) # modulo

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")

# listy

lista = []
lista2 = [1, 2, 3]
lista3 = [1, "Ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] # wartość 3, indeks 2
lista4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista4[1][1] # 5
# a = input("Podaj zdanie\n")
# count=0
# for i in a:
#     if(i.isspace()):
#         count=count+1
# print("",count)
########################################
# import sys
# print("Podaj jakas liczbe")
# a = sys.stdin.readline()
# a = int(a)
# print("Podaj jakas liczbe")
# b = sys.stdin.readline()
# b = int(b)

# wynik= a*b
# wynik = str(wynik)

# sys.stdout.write(wynik)
##########################################
# a = input("Podaj liczbe: ")
# a = int(a)

# if a >= 0:
#     print(str(a))
# elif a < 0:
#     print(str(-a))
###########################################
# a = input("Podaj liczbe a: ")
# b = input("Podaj liczbe b: ")
# c = input("Podaj liczbe c: ")
# a = int(a)
# b = int(b)
# c = int(c)

# if (a>0 and a<=10) and (a>b or b>c):
#     print("spelnione")
# else:
#     print("nie spelnione")
#############################################
# for liczba in range(0, 5000, 1): # start, stop ,step
#     if liczba%5==0:
#         print(liczba)
#############################################
# liczba = input("Podaj liczbe: ")
# liczba = int(liczba)
# liczba2 = pow(liczba,2)
# print(str(liczba2))
#############################################
# lista = []
# while len(lista)!=20:
#     a = input("Podaj liczbe a: ")
#     lista.insert(0,a)
#     print('lista: ',lista)
##############################################
# liczba = input("Podaj liczbe wielocyfrowa: ")
# liczba = int(liczba)
# list = []
# while liczba>1:
#     list.insert(0,liczba%10)
#     liczba = liczba/10
#     print('list: ',list)
# lista = [ int(x) for x in list]
# wynik = sum(lista)
# print(wynik)
##############################################
# h = input("wysokosc wiezy: ")
# h = int(h)
# if h<=10:
#     for num in range(h+1):
#         for i in range(num):
#             print("A", end="")
#         print("\n") 
##############################################
h = input("wysokosc wiezy: ")
h = int(h)
num = (h+3)
if h<=9 and h>=3:
    for num in range(h+1):
        for i in range(num):
            print("o", end="")
        print("\n") 

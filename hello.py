# import random
# import math

# print("hello world")
# #to jest komentarz 
# zmienna=10
# print(type(zmienna))

# rzeczywista=10.5
# print(type(rzeczywista))
# print ('%.20f'%rzeczywista)

# tekst1="jakis tekst"
# print(type(tekst1))
# print(tekst1[1])

# tekst_wielolinijkowy="""
# a
# b
# c
# """
# print(tekst_wielolinijkowy)

# suma=2+4
# roznica=5-2
# iloczyn=4*2
# iloraz=10/2
# potega=4**2
# reszta=5%2

# tekst2="abcd"
# polaczenie=tekst1+tekst2
# print(polaczenie)
# ciag="slowo"*10
# print(ciag)

# print("Wartość zmiennej zmienna to: ", zmienna)
# print("Wartość zmiennej zmienna to: %.2f" %zmienna)
# print(f"Wartość zmiennej zmienna to {zmienna}")
# print("Wartość zmiennej zmienna to: "+str(zmienna))

# # imie=input("jak masz na imię?")
# # print("Cześć",imie,"!")
# # print(f"Cześć {imie}!")

# # wiek=int(input ("Podaj swój wiek: "))
# # print("Masz",wiek,"lat.")


# los=random.randint(1, 20)
# print(los)

# potegowanie=math.pow(2,5)
# print(potegowanie)

# liczba=int(input("Podaj liczbę: "))

# if liczba>0:
#     print("Liczba jest dodatnia")
# elif liczba<0:
#     print("Liczba jest ujemna")
# else:
#     print('Liczba jest równa zero')


# if liczba%2==0:
#     print("Liczba jest podzielna przez 2")
# else:
#     print("Liczba nie jest podzielna przez 2")


# if "prosty" in zdanie:
#     print("tekst zawiera słowo 'prosty'")
# else:
#     print("tekst zawiera słowo 'prosty'")

# a=5
# b=5

# if a is b:
#     print("zmienne a i b są takie same")
# else:
#     print("zmienne a i b nie są rózne")

# liczba=int(input("Podaj liczbe:  "))

# if liczba >= 0:
#     print

for i in range(3):
    print(i)

for i in range(1,100,2):
    print(i)

for i in range(100,0 ,-2):
    print(i)

for v in "string":
    if v=="i":
        break
    print(v)

for v in "string":
    if v=="i":
        continue
    print(v)

def powitanie():
    print("cześć")

powitanie()

def powitanie_imienne(imie):
    print("cześć", imie)

powitanie_imienne("Roman")

def dzielenie(dzielna, dzielnik):
    if dzielnik==0:
        return
    else:
        return dzielna/dzielnik
    
x=dzielenie(3,4)
print(x)
print(dzielenie(4,2))



lista=[1,2,3]
print(lista)


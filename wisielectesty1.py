import random


lista = ["szkola", "ksiazka", "warzywo", "owoce", "poduszka"]


haslo = str(lista[random.randint(0, len(lista) - 1)])
tablica = list(haslo)

  
for i in range(len(haslo)):
    tablica[i] = "_"


zycia = 10


while zycia > 0:
    print("")
    print(" pozostalo ci ", zycia, " zyc")
    print("")
    print(" ".join(tablica))
    print(" ")
    print("Podaj swoja litere: ")
    litera = input()
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera
        if "".join(map(str, tablica)) == haslo:
            print("")
            print(" pozostalo ci ", zycia, " zyc")
            print("")
            print(" ".join(tablica))
            print(" ")
            print(" wygrales!")
            break
    else:
        zycia -= 1
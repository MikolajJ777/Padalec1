import random 

odp = input("Podaj swoją liczbę:")

los=random.randint(1, 49)
print("Wylosowana liczba:",los)


if los ==int(odp):
    print("Brawo udało ci się, wygrałes")
else:
    print("Nie udało ci się spróbuj jeszcze raz")
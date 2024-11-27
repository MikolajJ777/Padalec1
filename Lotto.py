import random 
c=2
while c==2:

    odp = input("Podaj swoją liczbe od 1 do 49: ")

    los=random.randint(1, 49)
    print("Wylosowana liczba: ",los)


    if los ==int(odp):
        print("Brawo udało ci się, wygrałes główną nagrode!: ")
    else:
        print("Nie udało ci się spróbuj jeszcze raz: ")
    c=int(input("By zagrać ponownie wciśnij dwa: "))
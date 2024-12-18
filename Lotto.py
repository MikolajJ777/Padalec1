import random 
c=0
while c==0:

    odp = input("Podaj swoją liczbe od 1 do 777: ")

    los=random.randint(1, 777)
    print("Wylosowana liczba: ",los)


    if los ==int(odp):
        print("Brawo udało ci się, wygrałes główną nagrode!: ")
    else:
        print("Nie udało ci się spróbuj jeszcze raz: ")
    c=int(input("By zagrać ponownie wciśnij zero: "))
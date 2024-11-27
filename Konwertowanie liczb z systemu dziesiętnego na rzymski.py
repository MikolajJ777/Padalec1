

M=1000
D=500
C=100
L=50
X=10
V=5
I=1











c=1
while c==1:
    print("Witaj w konwerterze liczb z systemu dziesiętnego na rzymski: ")
    print("""Wpisz numer operacji której chcesz użyć
    1.Z systemu dziesiętnego na rzymski""")
    numer=int(input("numer operacji: "))

    if numer==1:
        x=int(input("Podaj liczbe w systemie dziesiętnym: "))
        print("Liczba w systemie rzymskim to: ",x)
    c=int(input("Jeżeli chcesz kontynuować wciśnij jeden: "))
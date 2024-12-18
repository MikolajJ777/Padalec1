while True:
    n=int(input("Podaj swoją liczbe: "))
    for i in range(-1,n):
        if n==1:
            print("To nie jest liczba pierwsza")
            break
        elif n==3:
            print("To jest liczba pierwsza")
            break
        elif n==2:
            print("To jest liczba pierwsza")
            break
        elif n==5:
            print("To jest liczba pierwsza")
            break
        elif n%2==0:
            print("To nie jest liczba pierwsza")
            break
        elif n%3==0:
            print("To nie jest liczba pierwsza")
            break
        elif n%5==0:
            print("To nie jest liczba pierwsza")
            break
        else:
            print("To jest liczba pierwsza")
            break
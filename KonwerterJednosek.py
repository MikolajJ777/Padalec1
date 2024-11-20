print("Witaj konwerterze jednostek")
print("""Wpisz numer operacji której chcesz użyć
1.Z milimetrów na centymetry
2.Z centymetrów na metry 
3.Z metrów na kilometry
4.Z centymetrów na milimetry
5.Z metrów na centymetry
6.Z kilometry na metry""")
numer=int(input("numer operacji: "))



if numer==1:
    x=int(input("Podaj długość w milimetrach: "))
    print("Długość w centymetrach wynosi: ",x/10)
elif numer==2:
    x=int(input("Podaj długość w centymetrach: "))
    print("Długość w metrach wynosi: ",x/100)
elif numer==3:
    x=int(input("Podaj długość w metrach: "))
    print("Długość w kilometrach wynosi: ",x/1000)
elif numer==4:
    x=int(input("Podaj długość w centymetrach: "))
    print("Długość w milimetrach wynosi: ",x*10)
elif numer==5:
    x=int(input("Podaj długość w metrach: "))
    print("Długość w centymetrach wynosi: ",x*100)
elif numer==6:
    x=int(input("Poja długość w kilometrach: "))
    print("Długość w metrach wynosi: ",x*1000)
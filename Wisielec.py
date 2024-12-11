import random

lista=["samochod", "drzwi", "ksiazka", "stol", "slonce", "komputer", "morze", "kot", "kawa", "jablko", "telefon", "okno", "pies",
 "biurko", "drzewo", "zima", "miasto", "chleb", "gwiazda", "pilka", "woda", "kwiat", "milosc", "rzeka", "niebo", "czasopismo",
 "rower", "szkola", "dom", "skarpetki", "mysz", "stacja", "komputer", "marmur", "herbata", "cukier", "park", "plot", "snieg",
 "noc", "zegar", "ksiazka", "gitara", "kawalek", "samochod", "obraz", "zamek", "hotel", "sala", "kolezanka", "kolega", "ogrod",
 "szafa", "przyjaciel", "telefon", "wschod", "zachod", "noc", "rzeka", "ziemia", "oceany", "krajobraz", "latarka", "serce", "pies",
 "lampa", "miasto", "las", "strona", "okno", "komputer", "pociag", "kawa", "parasol", "walizka", "przyroda", "pralka", "ksiazka",
 "reka", "historia", "lawka", "czolo", "tlum", "rower", "kotlet", "wiatr", "pustynia", "zapach", "krzeslo", "swiatlo", "kawalek",
 "zaba", "zdjecie", "paleta", "klucz", "zupa", "akordeon", "koralik", "zuraw", "kolo", "granat", "piasek", "budynek", "smierc",
 "zegarek", "wiatrak", "sylwetka", "wino", "kolo", "jablko", "strona", "towar", "blad", "nos", "ksiazka", "chlopak", "rower",
 "drzwi", "przygoda", "rzeka", "telefon", "zmiana", "swiat", "biurko", "telefon", "buty", "plyn", "ulica", "wschod", "zmierzch",
 "worek", "prad", "woda", "brzuch", "wiatr", "morze", "plaza", "wolnosc", "palce", "liczba", "samochod", "komputer", "ksiazka",
 "flet", "poranek", "gabinet", "szkola", "pokoj", "woda", "krzeslo", "las", "wedka", "krzak", "kieliszek", "klocki", "roslina",
 "palec", "przyjaciel", "dziecko", "statek", "karta", "czekolada", "hamulec", "powietrze", "koza", "ucho", "swiatlo", "blad",
 "krol", "nos", "proces", "ser", "okular", "strefa", "deszcz", "ksiazka", "dzwiek", "laptop", "pytanie", "odpowiedz", "korona",
 "zdjecie", "atrament", "pokoj", "waga", "deska", "kwiatek", "wieloryb", "brama", "krew", "tance", "pokoj", "horyzont", "portfel",
 "szklo", "traktor", "zamek", "motocykl", "basen", "zbior", "sciana", "palac", "lod", "balwan", "las", "milosc", "ciasto", "mysz",
 "grzebien", "pusta", "ksiazka", "muszka", "koralik", "zegar", "deska", "koc", "pokoj", "ekipa", "bieg", "zdjecie", "sciana",
 "szklanka", "ul", "kwiat", "slon", "pasta", "krawat", "laptop", "ekran", "kwiaty", "spiew", "snieg", "budzik", "fala", "pomarancza",
 "jajko", "wilk", "lod", "zupa", "tatuz", "pamiec", "zarowka", "wulkan", "spodnica", "maszynka", "komputer", "klucz", "zegar", "las",
 "zupa", "opowiesc", "lisc", "szalik", "banknot", "peleryna", "ksiazka", "chleb", "pokoj", "slonce", "meble", "pilka", "lampa", "woda",
 "koc", "obraz", "owoc", "jez", "mieso", "praca", "zima", "pasek", "koc", "kosc", "komputer", "plac", "prosiak", "latarnia", "ksiazka",
 "piekarnik", "waz", "guma", "szklo", "pokoj", "serce", "pilka", "strona", "zloto", "miod", "gorka", "prad", "tablet", "fotele",
 "proszek", "slonce", "roza", "grzanka", "zegar", "przyjaciel", "portfel", "komputer"]

haslo = str(lista[random.randint(0,len(lista)-1)])
tablica=list(haslo)


for i in range(len(haslo)):
    tablica[i]= "_"


zycia=6


while zycia > 0:
    print("")
    print("pozostało ci ", zycia,"zyc")
    print("")
    print(" ".join(tablica))
    print(" ")
    print("Podaj swoją litere: ")
    litera=input()
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i]==litera:
                tablica[i]=litera
        if "".join(map(str, tablica))==haslo:
            print("")
            print("Pozostało ci ", zycia, "zyc")
            print("")
            print(" ".join(tablica))
            print(" ")
            print("Wygrałeś!")
            break
    else:
        zycia-=1

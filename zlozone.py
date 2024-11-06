lista=[13,45,13]
print(lista)

lista.sort() #lista.sort
print(lista)

lista.reverse
print(lista)

print(lista.count(13))

lista.remove(13)
print(lista)

lista.append(13)
print(lista)

print(len(lista))

print(lista[0])

for i in lista:
    print(i)



print(*lista)

print(*lista, sep=", ")

lista1=["a","nb"]
print("".join(lista1))

print(lista+lista1)

lista[0]=11
print(lista)

kontakty={
    "Jan":123732840,
    "Anna":123456789,
    "Michal":234567091

}


kontakty["Edward"]=123678904

print(kontakty)

print(kontakty["Jan"])

for imie, numer in kontakty.items():
    print(imie,numer)

for imie, numer in kontakty.items():
    print("%s ma numer telefonu: %d"%(imie, numer))


del kontakty["Jan"]

print(kontakty.keys())
print(kontakty.values())


zbior1={1,2,3,4}
zbior2={3,4,5,6}

laczenie=zbior1.union(zbior2)
print(laczenie)

wspolna=zbior1.intersection(zbior2)
print(wspolna)


roznica=zbior1.difference(zbior2)
print(roznica)


print(set("On ma na imie Eryk i Eryk to jego imie".split()))


krotka=(1,2,3,4,5)
print(krotka)

krotka1=2,3,4,5,6
krotka2=("a",)

print(len(krotka1))
print(krotka1.count(3))

print(krotka1[0])
print(krotka1[-1])

print(krotka1[1:3])
print(krotka1[:-3])

krotka3=krotka1+krotka2
print(krotka3)

del krotka3

print(krotka1)

a,b,c,d,e=krotka1
print(a)
print(b)
print(c)
print(d)
print(e)



import time
n=int(input("Podaj liczbe całkowitą: "))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
end=time.time()
print(end-start)

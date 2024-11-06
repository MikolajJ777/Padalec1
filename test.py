n=int(input("Podaj n"))
suma=0
for i in range(1, n+1):
    suma+=1
print(suma)


def suma_rekrutacyjna(n):
    if n==0:
        return 0 
    return n+suma_rekrutacyjna(n=1)

print(suma_rekrutacyjna(n))
x=int(input("Podaj liczbę 1: "))
k=int(input("Podaj liczbę 2: "))
znak=(input("Podaj znak działania(+,-,*,/,**))"))

operators = {"+": x+k, "-": x-k,"/": x/k, "*": x*k, "**": x**k, "%": x%k }


if znak == "+":
    print(operators["+"])
elif znak == "-":
    print(operators["-"])
elif znak == "/":
    print(operators["/"])
elif znak == "*":
    print(operators["*"])
elif znak == "**":
    print(operators["**"])
elif znak == "%":
    print(operators["%"])

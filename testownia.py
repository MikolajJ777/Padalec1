from collections import OrderedDict
def write_system_rzymski(num):

    system_rzymski = OrderedDict()
    system_rzymski[1000] = "M"
    system_rzymski[900] = "CM"
    system_rzymski[500] = "D"
    system_rzymski[400] = "CD"
    system_rzymski[100] = "C"
    system_rzymski[90] = "XC"
    system_rzymski[50] = "L"
    system_rzymski[40] = "XL"
    system_rzymski[10] = "X"
    system_rzymski[9] = "IX"
    system_rzymski[5] = "V"
    system_rzymski[4] = "IV"
    system_rzymski[1] = "I"

    def system_rzymski_num(num):
        for r in system_rzymski.keys():
            x, y = divmod(num, r)
            yield system_rzymski[r] * x
            num -= (r * x)
            if num > 0:
                system_rzymski_num(num)
            else:
                break

    return "".join([a for a in system_rzymski_num(num)])
num = int(input("Podaj liczbę do przekonwertowania na system rzymski: "))
print ("Liczba" ,num, "w systemie rzymskim to: ",write_system_rzymski(num))

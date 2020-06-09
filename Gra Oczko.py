
print("Gra oczko")
import random
#gracz1 wybiera 4,5 lub 6
a=random.randint(4,6)
print("Gracz 1 wybiera:",a)
suma=a
print("Suma=",suma)

#gracz2 wybiera 4,5 lub 6
b=random.randint(4,6)
print("Gracz 2 wybiera:",b)
suma=suma+b
print("Suma=",suma)

#gracz1 wybiera 4,5 lub 6
c=random.randint(4,6)
print("Gracz 1 wybiera:",c)
suma=suma+c
print("Suma=",suma)

#gracz2 wybiera 4,5 lub 6
d=random.randint(4,6)
print("Gracz 2 wybiera:",d)
suma=suma+d
print("Suma=",suma)
if suma>21:
    print("Wygrywa gracz 1.")
if suma==21:
    print("Remis")
if suma<21:
    #gracz1 wybiera 4,5 lub 6
    e=random.randint(4,6)
    print("Gracz 1 wybiera:",e)
    suma=suma+e
    print("Suma=",suma)
    if suma>21:
        print("Wygrywa gracz 2.")
    if suma==21:
        print("Remis.")
    if suma<21:
        print("Wygrywa gracz 1.")

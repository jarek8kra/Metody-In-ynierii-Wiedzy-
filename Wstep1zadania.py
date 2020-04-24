print("Przypisanie do zmiennej")
text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"


imie = "Jarosław"
nazwisko = "Kraśnicki"

litera1 = imie[2]
litera2 = nazwisko[4]# 4 zamiast 3 bo jest polski znak, wtedy wynik 0
liczba_literLI1=text.count(litera1)
liczba_literLI2=text.count(litera2)
print("W tekście jest",liczba_literLI1,"liter...oraz",liczba_literLI2,"liter")
print("Extended Slices dla Jarosław Kraśnicki:")
print(nazwisko[::-1].capitalize(),imie[::-1].capitalize())


#for x in range(1,10,1):
#    print(x)


#for x in range(100, 19, -5):
#   print(x)

lista1=[]
for x in range(1,11):
    lista1.append(x)
print(lista1)

lista2=[]
for x in lista1[5:]:
    lista2.append(x)
    lista1.remove(x)

print("Listy podzielone: ")
print(lista1)
print(lista2)
#połączenie
lista3=lista1+lista2
print(lista3)
lista3.insert(0,0)
print(lista3)
lista3.reverse()
print(lista3)
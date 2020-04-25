#Wprowadzenie zad 1-2
print("Przypisanie do zmiennej")
text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
imie = "Jarosław"
nazwisko = "Kraśnicki"
litera1 = imie[2]
litera2 = nazwisko[4]# 4 zamiast 3 bo jest polski znak, wtedy wynik 0
liczba_literLI1=text.count(litera1)
liczba_literLI2=text.count(litera2)
print("W tekście jest",liczba_literLI1,"liter...oraz",liczba_literLI2,"liter")

#Wprowadzenie zad 4
#print(dir("Napis"))
#help("Napis".count("p"))

#Wprowadzenie zad 5
print("Extended Slices dla Jarosław Kraśnicki:")
print(nazwisko[::-1].capitalize(),imie[::-1].capitalize())

#Wprowadzenie zad 6-7
lista1=[]
for x in range(1,11):
    lista1.append(x)
print("Lista", lista1)

lista2=[]
for x in lista1[5:]:
    lista2.append(x)
    lista1.remove(x)

print("Listy podzielone: ")
print(lista1,lista2)
lista1.extend(lista2)

print("Połączone: ",lista1)
lista1.insert(0,0)
print("Dodane zero: ",lista1)
lista1.reverse()
print("Odwrócona: ",lista1)


#Wprowadzenie zad 10
listatel=[1,2,2,2,3,3,6,6,9,9,47,47]
unikatowe=set(listatel)
print("Lista numerów:",listatel)
print("Lista unikatowa",unikatowe)

#Wprowadzenie zad 11
listx=[]
for x in range(1,11,1):
    listx.append(x)
print("Lista 1-10",listx)

#Wprowadzenie zad 12
listy=[]
for x in range(100, 19, -5):
   listy.append(x)
print("Lista 100-20",listy)

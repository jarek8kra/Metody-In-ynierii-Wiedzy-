#Wprowadzenie 2 zad 1
a_list=[5,6,4,2,8,1,0,9,3,7]
b_list=[4,8,2,1,3,7,5,9,0,6]

def funkcjazad1(a_list,b_list):
    c_list=[]
    for x in a_list:
        if(a_list.index(x)%2==0):
            c_list.append(a_list.index(x))
    for x in b_list:
        if(b_list.index(x)%2!=0):
            c_list.append(b_list.index(x))

    return(c_list)
print(funkcjazad1(a_list,b_list))

#Wprowadzenie 2 zad 2
data_text="Pies"
print("Zad 2:", data_text)
def fdatatext(data_text):
    listaznakow=[]
    for x in data_text:
        listaznakow.append(x)
    dict={
        "length":len(data_text),
        "letters":listaznakow,
        "big_letters":data_text.upper(),
        "small_letters":data_text.lower()
        }
    return(dict)
print(fdatatext(data_text))

#Wprowadzenie 2 zad 3
text='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
letter ='e'

def usunlitere(text,letter):
    wynik=''
    for x in text:
        if(x!=letter):
            wynik+=str(x)
    return(wynik)
print("Zadanie 3, usunięcie litery:",letter)
print(usunlitere(text,letter))

#Wprowadzenie 2 zad 4 temperatura
stopniC=20.0
temperature_type='R'# lub K lub R

def funkcjatemp(s,t):
    wynik=0.0
    try:
        if(t=='K'):
            wynik=s+273.15
        if(t=='F'):
            wynik=s*9/5+32
        if(t=='R'):
            wynik=(s+273.15)*9/5
        return(wynik)
    except:
        return("Błąd danych wejściowych!")
print("Zad 4, przelicznik temperatur z C na ",temperature_type)
print(funkcjatemp(stopniC,temperature_type))

#Wprowadzenie 2 zad 5 kalkulator
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def difference(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
zestaw1=Calculator(2,3)
print("Liczby a i b:",zestaw1.a,"i",zestaw1.b)
print("Dodawanie:",zestaw1.add()," Odejmowanie:",zestaw1.difference()," Mnożenie:",zestaw1.multiply()," Dzielenie:",zestaw1.divide())

#Wprowadzenie 2 zad 6 kalkulator Naukowy a**b
class ScienceCalculator(Calculator):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def power(self):
        return self.a**self.b
zestawScience=ScienceCalculator(2,9)
print("Liczby do naukowego: ",zestawScience.a,"i",zestawScience.b)
print("Potęgowanie kal. naukowym: ",zestawScience.power())

#Wprowadzenie 2 zad 7 funkcja odwracania napisów
napis='koteł'
def funcrev(napis):
    length=len(napis)
    wynik=napis[length::-1]
    return(wynik)
print(funcrev(napis))

#Wprowadzenie 2 zad 8 file_manager
file_name="plik.txt"
class FileManager:
    def __init__(self, file_name):
        self.file_name=file_name
    def read_file(self,file_name):
        f=open(file_name,"r")
        return(print(f.read()))#zawartość pliku

    def update_file(self,file_name,text_data): 
        f=open(file_name,"a")
        f.write(text_data)#dopisanie do pliku
        f = open(file_name, "r")
        return(print(f.read()))
        f.close()
p1=FileManager(file_name)
print(p1.read_file(file_name))
p2=FileManager(file_name)
print(p2.update_file(file_name,"\n Nowa linia..."))

 





    
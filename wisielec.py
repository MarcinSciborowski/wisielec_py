import random
import string

PLIK_Z_LISTA_SLOW = "wyrazy.txt"

def zaladuj_slowa():
    """
    Zwraca liste poprawnych wyrazow (bez polskich znakow diakrytycznych). 
    Wyrazy zawsze zaczynaja sie z malej litery.
    
    """
    print "Laduje liste slow z pliku..."
    # plikWejsciowy : plik
    plikWejsciowy = open(PLIK_Z_LISTA_SLOW , 'r', 0)
    # linia: string
    linia = plikWejsciowy.readline()
    # listaSlow: lista stringow
    listaSlow = string.split(linia)
    print "  ", len(listaSlow), "wyrazow zaladowano."
    return listaSlow

def wylosuj_wyraz(listaSlow):
    """
    wylosuj_wyraz (lista): lista slow (stringow)

    Zwraca losowy wyraz z listy wyrazow
    """
    return random.choice(listaSlow)

listaSlow = zaladuj_slowa()
a=wylosuj_wyraz(listaSlow)
proba=0
def wisielec():
    global proba
    znaki=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z"]
    wyko_znaki=[]
    proba=10
    print ("Witaj w grze wisielec!")
    print "Wyraz zawiera ",len(a),"znakow"
    print "Pozosta³o ci",proba,"prób"
    print "Dostepne znaki: ",znaki
    print "================================================="
    podloga=list("_"*len(a))
    koniec=False
    while koniec==False:
        koniec=True 
        for i in podloga:
            if i=="_":
                koniec=False
        if koniec==True:
            print "Gratulacje, wygra³eœ"
            break
        litera=raw_input("Podaj literê: ")
        if litera in znaki:
            znaki.remove(litera)
            wyko_znaki.append(litera)
            zakreslanie(podloga,litera)
        else:
            print "Wykorzysta³eœ ju¿ literê."
        print podloga
        print "Pozosta³o ci",proba,"prób"
        print "Dostepne znaki: ",znaki
        print "================================================="
        if proba==0:
            print "Wykorzysta³eœ limit prób, przegrana!"
            print "Wylosowany wyraz to:",a
            break
        
def zakreslanie(podloga,litera):
    global proba
    slowo_lista=list(a)
    sprawdz=False
    for i in range(len(a)):
        if litera==slowo_lista[i]:
            podloga[i]=litera
            sprawdz=True
            print "Tafi³eœ!"
    if sprawdz==False:
        proba=proba-1
        print "Wyraz nie zawiera tej litery!"
    return podloga
                
wisielec()

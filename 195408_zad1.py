'''Gra Mastermaind
   Jest to gra w ktorej komputer losuje kombinacje 4 elementow
   ze zbioru {a,b,c,d,e,f} nastepnie gracz ma za zadanie
   w 9 rundach odgadnac ta kominacje.
   Pomoca dla gracza jest wyswietlany wynik w postaci 1 i 2.
   1 - oznacza ze gracz wytypowal dobry element, ale na zlym miejscu
   2 - oznacza ze gracz wytypowal dobry element na dobrym miejscu
   Wynik jest w innej kolejnosci niz trafione elementy.

   Gracz wygrywa jezeli wtytpuje wszystkie 4 elementy i wynik bedzie
   sie skladac z samych 2.

    Autor: Piotr Gasior
    Data: 24.03.2014r.
'''

import random #zaimportowanie metody odpowiedzialnej za losowanie

def scan_replay():
    '''Metoda odpowiedzialna za wczytanie odpowiedzi uzytkownika '''
    temp = []
    temp.insert(0, raw_input("1 znak: ")) #wczytanie pierwszego znaku
    temp.insert(1, raw_input("2 znak: ")) #wczytanie drugiego znaku
    temp.insert(2, raw_input("3 znak: ")) #wczytanie trzeciego znaku
    temp.insert(3, raw_input("4 znak: ")) #wczytanie czwartego znaku
    return temp

def check_correct(rep, patt):
    '''Metoda odpowiedzialna za sprawdzenie czy
    odpowiedz zawiera odpowiednie znaki '''
    for k in range(4): #sprawdzenie wszystkich 4
        if rep[k] not in patt: #jezeli nie znajduje sie we wzorcu
            print ("Bladna odpowiedz popraw odpowiedz!")
            return False #zwroc blad
    else:
        return True #inaczej potwierdz poprawnosc

def set_field(patt):
    '''Metoda odpowiedzialna za ulozenie pytania z 4 elementow '''
    fil = []
    for j in range(4): #wybranie 4 losowych elementow
        fil.insert(j, random.choice(patt))
    return fil #zwrocenie zadania

def check_answer(rep, fiel):
    '''Metoda sprawdzajaca poprawnosc trafienia i oceniajaca'''
    rating = [] #tablica przetrzymujaca ocene za odpowiedz
    temp = fiel[:] #przekopiowanie zadania do zmiennej pomocniczej
    for i in range(4): #sprawdzenie poprawnosci
        #jezeli w tych samych komorkach jest ta sama odpowiedz
        if (rep[i] in temp) and (rep[i] == temp[i]):
            temp.remove(rep[i]) #usun ten element
            temp.insert(i, 'x') #wstaw zastepczy
            rating.append(2) #dodaj 2 pkt jako odgadniete
    for i in range(4): #ponowne sprawdzenie za podobnymi kolorami
        #jezeli sa te same elementy, ale w innych komorkach
        if rep[i] in temp:
            temp.remove(rep[i]) #usun kolor
            rating.append(1) #dodaj jeden pkt
    return rating #zwroc wynik

def if_win(ratings):
    '''Metoda sprawdzajaca czy nastapila wygrana'''
    if ratings.count(2) < 4: #jezeli jest mniej niz 4 dwojki
        return False #nie ma wygranej
    return True #jezeli sa 4 dwojki jest wygrana

if __name__ == '__main__':
    '''Glowna funkcja gry'''
    PATTERN = ('a', 'b', 'c', 'd', 'e', 'f') #krotka ze wzorcem odpowiedzi
    print("\n            Zaczynamy gre Mastermind :) \n\n\
            Wybierz 4 litery ze zbioru: {a, b, c, d, e, f}")
    FIELD = set_field(PATTERN) #wylosowanie zagadki przez komputer

    for l in range(1, 10):
        print ("Proba %d/9" %l) #informacja o aktualnej rundzie
        replay = scan_replay() #wczytaj odpowiedz
        while not  check_correct(replay, PATTERN): #sprawdzenie danych
            replay = scan_replay()
        print("Twoje Odpowiedzi:")
        print replay #podane odpowiedzi
        print("Trafienia:")
        print check_answer(replay, FIELD) #sprawdzenie wyniku
        if if_win(check_answer(replay, FIELD)): #sprawdzenie wygranej
            print("GRATULUJE! Wygrales Mastermind w %d probie! :)" % l)

    else: #jezeli konczy sie ilosc porob to przegrana
        print("Nistety przegrales :(")

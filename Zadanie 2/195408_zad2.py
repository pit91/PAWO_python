'''
Kalkulator prostych rownan zapisanych w notacji polskiej.

Obslugiwane rownania:
    1) + dodawanie
    2) - odejmowanie
    3) * mnozenie
    4) / dzielenie

Dodatkowe funkcje:
    1) save <nazwa_do_zapisu.txt> - zapis wykonwnych zadan do pliku
    2) q - wyjscie z programu

Program zawiera obsluge wyjatkow przy wprowadzaniu rownania,
by zapobiec wprowadzeniu liczby/litery zamiast liczby.

Posiada asercje przy bledach wprowadzania, blednych znakach
rownania, zlej iloci wprowadzonych danych, oraz braku
nazwy pliku do zapisu.

Autor: Piotr Gasior
Data: 30.03.2014r.
'''

#dodanie bibliotek
import sys

def scan_eq():
    '''
    Metoda odpowiedzialna za wczytaniw linii rownania
    oraz za zwrocenie wartosci wczytanej w formie listy.

    Dodatkowo posiada obsluge wylapywana bledow:
    1) Blad wprowadzenia liczb - gdy dana nie jest liczba
    2) Bledna ilosc argumantow
    3) Nieobslugiwany znak rownania

    W wypadku wystopienia bladu zostaje wyswietlony blad
    oraz zwrocona wartosc None

    OUT:
    - lista [<str> <float> <float>] zawierajaca <znak><liczbe<Liczbe>
        rownania podanego przez uzytkownika
    '''
    scan = raw_input("Podaj rownanie w notacji polskiej: ") #wczytanie
    equation = map(str, scan.split()) #konwersja stringa do listy stringow

     #sprawdzenie czy uzytkownik wybral opcje zapisu
    if equation[0] == 'save' and len(equation) == 2 or equation[0] == 'q':
        return equation

    #sprawdzenie czy ilosc danych jest odpowiednia
    if len(equation) != 3:
        print ("Blad wprowadzonych danych! - blad ilosci danych!")
        equation = None #zwroc nic
        return equation

    #obsluzenie wyjatku wpisania znaku lub litery zamiast cyfry
    try:
        equation[1] = float(equation[1]) #konwersja na float
        equation[2] = float(equation[2]) #konwersja na float
    except ValueError: #jezeli zdazy sie taki wyjatek
        print ("Blad wprowadzonych danych! - nieprawidlowa liczba!")
        equation = None #nic nie zwracaj
        return equation
    #sprawdzenie czy znak rownania jest obslugiwany
    if equation[0] != '/' and equation[0] != '*' \
       and equation[0] != '+' and equation[0] != '-':
        print ("Blad wprowadzonych danych! - nieprawidlowy znak rownania!")
        equation = None #zwroc nic
        return equation
    return equation #zwrocenie listy z rownaniem

def do_eq(log):
    '''
    Metoda odczytujaca znak rownania oraz odpowiednio obliczajaca
    wartosc rownania.

    Obslugiwane rownania:
    1) + dodawanie
    2) - odejmowanie
    3) * mnozenie
    4) / dzielenie

    IN:
    - eq - lista zawierajaca rownanie w notacji polskiej
           <znak><liczba><liczba>
    OUT:
    - wynik przeprowadzonego rownania
    '''
    #przypisanie do zmiennej wartosci liczb rownania
    if len(log[len(log)-1]) == 3:
        var_a = log[len(log)-1][1]
        var_b = log[len(log)-1][2]

    if log[len(log)-1][0] == '+': #jezeli wywolano dodawania
        result = var_a + var_b
    elif log[len(log)-1][0] == '-': #jezeli wywolano odejmowanie
        result = var_a - var_b
    elif log[len(log)-1][0] == '*': #jezeli wywlano mnozenie
        result = var_a * var_b
    elif log[len(log)-1][0] == '/': #jezeli wywolano dzielenie
        result = var_a / var_b
    elif log[len(log)-1][0] == 'save':
        save_eq(log)
        result = None
    elif log[len(log)-1][0] == 'q':
        sys.exit()

    return result #zwrocenie wyniku rownania

def save_eq(log):
    '''
    Metoda odpowiedzialna za wpisanie do pliku rejestru
    przeproawdzonych dzialan w naszym programie.

    IN:
    - log - lista zawierajaca informacje o wykonanym rownaniu

    OUT:
    - plik tekstowy o nazwie "calc_log.txt"
    '''

    #wczytanie nazwy pliku do zapiu
    name = log[len(log)-1][1]

    #wyrzucenie z lity informacji o zapisie
    log.pop()

    #zamiana wszystkich elementow na string by umozliwic zapis
    for it_k in range(len(log)):
        for it_j in range(len(log[it_k])):
            log[it_k][it_j] = str(log[it_k][it_j])

    with open(name, 'w') as file_save: #otwarcie pliku do zapisu
        for it_m in range(len(log)): #wpisanie kolejno rownan
            for it_n in range(len(log[it_m])): #wypisanie kolejnych elementow
                file_save.write(log[it_m][it_n])
                file_save.write(" ")
                if it_n == 2:
                    file_save.write(" Wynik: ")
            file_save.write("\n")


if __name__ == '__main__':
    '''
    Metoda glowna programu posiadajaca petle nieskonczona wykonujaca
    program.
    Zawiera sprawdzanie czy poprawnie wprowadzono dane, jezeli nie,
    wywoluje ponownie funkcje czytajaca.
    '''
    REG = [] #lista zawierajaca informacje o rownaniach
    TEMP = None #zmienna pomocnicza do wczytania danych

    print "                    Prosty kalkulator rownan +, -, *, /.\n"
    print "* Aby zapisac wykonywane rownania wpisz: save <nazwa_zapisu.txt>\n"
    print "* Aby zamknac kalkulator wpisz: q\n"

    while True: #petla nieskonczona
        while TEMP == None: #dopoki nie odczyta sie poprawnie danych
            TEMP = scan_eq() #odczytaj dane

        REG.append(TEMP) #wczytanie rownanie do rejestru
        REG[len(REG)-1].append(do_eq(REG)) #wczytanie wyniku
        print "Wynik rownania: "
        print REG[len(REG)-1][3] #wyswietlenie wyniku
        TEMP = None #wyzeruj zmienna

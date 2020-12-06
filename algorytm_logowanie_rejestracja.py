#trzeba dodac czesc z prosba i potwierdzenie czy jestesmy juz zarejestrowani

#jezeli rejestracja, to blok rejestracyjny, nastepnie pytanie,
#czy chce sie przejsc do okreanu logowania
#jezeli logowanie, to do obszaru logowania

flaga = False
flaga2 = False
flaga3 = False
while not flaga3:
    while not flaga:
        try:
            logowanie_rejestracja = int (input (f"Chcesz sie zalogowac (1) czy zarejestrowac (2)?: "))
            flaga = True
        except ValueError:
            continue
    
    #BLOK LOGOWANIA###############################################################
    #odczyt danych z pliku w formie slownika
    
    if logowanie_rejestracja == 1:   
        nazwy_hasla_r = open("nazwy_hasla.txt", "r")
        nazwy_hasla_a = open ("nazwy_hasla.txt", "a")
        slownik_uzytkownikow_hasel = {}
        n = 0
        while not flaga2 and n < 4:        
            for j in nazwy_hasla_r:
                j = j.rstrip()
                k = str(j)
                k2 = eval(k)
                slownik_uzytkownikow_hasel.update(k2)
                
        
            l = input (f"Podaj nazwe uzytkownika: ")
            m = input (f"Podaj haslo: ")
            
            try:
                if slownik_uzytkownikow_hasel[l] == m:
                    print ("Zalogowano.")
                    flaga = True
                    flaga2 = True
                    flaga3 = True
                    nazwy_hasla_r.close()
                    nazwy_hasla_a.close()                     
                else:
                    print ("Podales zle dane logowania. Pozostale proby logowania: {}".format(3-n))
                    n = n + 1
            except KeyError:
                print ("Podales zle dane logowania. Pozostale proby logowania: {}".format(3-n))
                n = n + 1          
    
    #BLOK REJESTRACYJNY###########################################################
    #ta czesc prosi o wprowadzenie nazwy uzytkownika i sprawdza czy jest w bazie
    if logowanie_rejestracja == 2:
        file = open("nazwy_uzytkownikow.txt", "r")
        file2 = open ("nazwy_uzytkownikow.txt", "a")
        
        lista_uzytkownikow = []
        
        for i in file:
            i = i.rstrip()
            lista_uzytkownikow.append(i)
        
        file.close()
        file2.close()
        
        file = open("nazwy_uzytkownikow.txt", "r")
        file2 = open ("nazwy_uzytkownikow.txt", "a")
        
        uzytkownik = input(f"Wprowadz nazwe uzytkownika: ")
        
           
        while (True):
            if uzytkownik in lista_uzytkownikow:
               uzytkownik = input(f"Taka nazwa uzytkownika jest juz w bazie. Wprowadz inna nazwe uzytkownika: ")
               continue
            elif len(uzytkownik) < 6:
               uzytkownik = input(f"Taka nazwa uzytkownika jest za krotka. Wprowadz dluzsza nazwe uzytkownika: ")
               continue        
            else:
                print (uzytkownik, file=file2)
                break
            
        file.close()
        file2.close()
        
    #ta czesc prosi o wprowadzenie hasla i sprawdza czy jest poprawne
        znaki = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', ':', ';', '"', '<', ',', '>', '.', '?', '/']
        lista_znakow_hasla = []
        b = -1
        a = 0
        
        while (True):
            if a == 0:
                haslo = input (f"Podaj haslo skladajace sie z 8 znakow, znaku specjalnego i duzej litery: ")
                b = -1
                if len(haslo) > 7: 
                    for i2 in haslo:
                        if i2.isupper():
                            for i in haslo:
                                lista_znakow_hasla.append(i)        
                            for i in lista_znakow_hasla:
                                try:
                                    b = znaki.index(i)
                                except:        
                                    continue
                            if b > -1 and len(haslo) > 7 and i2.isupper():
                                a = 1
                                break
            else:
                break
        
    #ta czesc zapisuje uzytkownika i haslo w ramach slownika do pliku
    #robi odczyt i dodaje do swojego wewnetrznego slownika uzytkownikow i hasla
    #sprawdzam czy jest w slowniku hasel i uzytkownikow
        nazwy_hasla_r = open("nazwy_hasla.txt", "r")
        nazwy_hasla_a = open ("nazwy_hasla.txt", "a")
        slownik_uzytkownikow_hasel = {}
        slownik_u_h = {}
        
        slownik_u_h[uzytkownik] = haslo
        print (slownik_u_h, file = nazwy_hasla_a)
        
        for j in nazwy_hasla_r:
            j = j.rstrip()
            k = str(j)
            k2 = eval(k)
            slownik_uzytkownikow_hasel.update(k2)
            
        nazwy_hasla_r.close()
        nazwy_hasla_a.close()
        print ("Twoja nazwa uzytkownika to: {}, haslo to: {}.".format(uzytkownik, haslo)) 
        flaga = True
        flaga2 = True
        flaga3 = True
    else:
         if flaga and flaga2 and flaga3:
             break
         else:
            try:
                logowanie_rejestracja = int (input (f"Chcesz sie zalogowac (1) czy zarejestrowac (2)?: "))
            except ValueError:
                continue
        

        
    
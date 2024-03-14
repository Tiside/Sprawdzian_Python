with open("napisy.txt", 'r') as plik:
    plik = plik.read().splitlines()


#a parzyste 
    def liczbyParzyste(plik):
        parzyste = 0
        for liczby in plik:
            if len(liczby) %2 == 0:
                parzyste += 1
        return parzyste
    print(liczbyParzyste(plik))
    
#b takiesame 
    def takiesame(plik):
        takiesame = 0
        for liczby in plik:
            if liczby.count('0') == liczby.count('1'):
                takiesame += 1
        return takiesame
    print(takiesame(plik))
#c same zera i same jedynki
    def sameZera(plik):
        sameZera = 0
        for liczby in plik:
            if liczby.count('0') == 0:
                sameZera += 1
        return sameZera
    def sameJedynki(plik):
        sameJedynki = 0
        for liczby in plik:
            if liczby.count('1') == 0:
                sameJedynki += 1
        return sameJedynki
    print(sameZera(plik))
    print(sameJedynki(plik))
#d konczy sie jedynka
    def koniecJedynka(plik):
        koniecJedynka = 0
        for liczby in plik:
            if liczby.endswith('1'):
                koniecJedynka += 1
        return koniecJedynka
    print(koniecJedynka(plik))
    
#e palindrom
    def samPalindrom(pali):
        return pali == pali[::-1]
    def palindrom(plik):
        palindromy = 0
        for liczby in plik:
            if samPalindrom(liczby):
                palindromy += 1
        return palindromy

    print(palindrom(plik))
    
#f ile napisow po dlugosci
    def dlugosciNapisow(plik):
        dwa = 0
        trzy = 0
        cztery = 0
        piec = 0
        szesc = 0
        siedem = 0
        osiem = 0
        dziewiec = 0
        dzisiec = 0
        jedenasci = 0
        dwanascie = 0
        trzynascie = 0
        czternascie = 0
        pietnascie = 0
        szesnascie = 0
        for liczby in plik:
            if len(liczby) == 2:
                dwa += 1
            elif len(liczby) == 3:
                trzy += 1
            elif len(liczby) == 4:
                cztery += 1
            elif len(liczby) == 5:
                piec += 1
            elif len(liczby) == 6:
                szesc += 1
            elif len(liczby) == 7:
                siedem += 1
            elif len(liczby) == 8:
                osiem += 1
            elif len(liczby) == 9:
                dziewiec += 1
            elif len(liczby) == 10:
                dzisiec += 1
            elif len(liczby) == 11:
                jedenasci += 1
            elif len(liczby) == 12:
                dwanascie += 1
            elif len(liczby) == 13:
                trzynascie += 1
            elif len(liczby) == 14:
                czternascie += 1
            elif len(liczby) == 15:
                pietnascie += 1
            elif len(liczby) == 16:
                szesnascie += 1
        return dwa, trzy, cztery, piec, szesc, siedem, osiem, dziewiec, dzisiec, jedenasci, dwanascie, trzynascie, czternascie, pietnascie, szesnascie
    print(dlugosciNapisow(plik))
wyniki = []

wyniki.append(f"{liczbyParzyste(plik)}")
wyniki.append(f"{takiesame(plik)}")
wyniki.append(f"{sameZera(plik)}")
wyniki.append(f"{sameJedynki(plik)}")
wyniki.append(f"{koniecJedynka(plik)}")
wyniki.append(f"{palindrom(plik)}")

with open('wynik.txt', 'w') as wyniki:
    wyniki.write(f"Liczby parzyste: {liczbyParzyste(plik)}\n")
    wyniki.write(f"Takie same: {takiesame(plik)}\n")
    wyniki.write(f"Same zera: {liczbyParzyste(plik)}\n")
    wyniki.write(f"Same jedynki: {sameJedynki(plik)}\n")
    wyniki.write(f"Koncem jest jedynka: {sameZera(plik)}\n")
    wyniki.write(f"Palindromy: {palindrom(plik)}\n")
    wyniki.write(f"punkt f wszystko w kolejnosci: {dlugosciNapisow(plik)}\n")
    



    



    


import Functions as f

## PRZEKSZTAŁCANIE ZZ
# Spis

# 4.A - Wejście w moduł zamówienia, wejscie w wygenerowane zamówienie ZZ, ustawinie ceny zakupu,
        # w pozostałych danych ustawienie rejestu PZ/1 do przekształcenia, ustawineie statusu, zatwierdzenie i przekształcenie dokumentu.

# 4.B - Wejscie w przekształcony dokument PZ, dodanie artykulu T1, zatwierdzenie.


def sprawdz_poz_dok(symbol_art, ilosc, cena, klucz_dok):

    zapytanie = "select symbol_art from poz_dok where symbol_art = ? and ilosc = ?  and cena=? and klucz_dok=?;"
    f.cursor.execute(zapytanie, (symbol_art, ilosc, cena, klucz_dok))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Pozycja dokumentu '{symbol_art}'  nie istnieje w bazie danych!"
    return results


## 4.A
f.aktywacja()
f.time.sleep(1)
f.dwa('shift', 'alt')
#f.kilka(17, 'down')
f.kilka(16, 'down')
f.kilka(1, 'right')
f.kilka(5, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.kilka(5, 'tab')
f.tekst('1')
f.kilka(4, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1.5)
f.kilka(8, 'tab')
f.jeden('enter')
f.time.sleep(1)
f.kilka(1, 'tab')
f.kilka(1, 'down')
f.kilka(6, 'tab')
f.jeden('enter')
f.kilka(5, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.jeden('spacja')
f.przeksztalc()
f.time.sleep(1)
f.dwa('shift', 'T')
f.time.sleep(3)
for i in range(3):
    f.jeden('esc')
    f.time.sleep(0.3)

#sprawdz_poz_dok('S1', '615', '1', 'PZ/1  /24/000001')

## 4.B
f.operacje('z', 'p')
f.time.sleep(0.5)
f.jeden('enter')
f.time.sleep(0.5)

f.jeden('insert')
f.time.sleep(1)
f.kilka(1, 'tab')
f.tekst('T1')
f.kilka(1, 'tab')
f.tekst('2000')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(4, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
f.dwa('shift', 'o')
f.jeden('esc')



#sprawdz_poz_dok('T1', '2000', '1', 'PZ/1  /24/000001')
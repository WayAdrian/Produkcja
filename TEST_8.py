import Functions as f

#PRZEKSZTAŁCAM ZS W WD
# 6.A  Do kolejnych operacji potrzebna jest konfiguracja: Dodaje magazyniera
# 6.B Do kolejnych operacji potrzebna jest konfiguracja:  W ust. globalnych
# 6.C Wchodze w listę - zaznaczam  swojego ZSa, spod f12 zminiam status na 'Potwierdzone' i przekształcam w WD

import pytest

def sprawdz_poz_dok(symbol_art, ilosc, cena, klucz_dok):
    zapytanie = "select symbol_art from poz_dok where symbol_art = ? and ilosc = ?  and cena=? and klucz_dok=?;"
    f.cursor.execute(zapytanie, (symbol_art, ilosc, cena, klucz_dok))
    results = f.cursor.fetchall()
    print(results)
    if not results:
        pytest.fail(f"Pozycja dokumentu '{symbol_art}' nie istnieje w bazie danych!")

    return results


# 6.A
f.aktywacja()
f.operacje('o', 'm')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1.5)
f.kilka(2, 'tab')
f.zakladka(3)
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.jeden('enter')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.jeden('esc')
f.jeden('esc')

# 6.B
f.aktywacja()
f.operacje('o', 'u')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.kilka(18, 'tab')
f.jeden('spacja')
f.dwa('shift', 'o')
f.kilka(3, 'tab')
f.dwa('shift', 'o')

f.aktywacja()
f.dwa('shift', 'alt')
#f.kilka(17, 'down')
f.kilka(16, 'down')
f.kilka(1, 'right')
f.kilka(2, 'down')
f.jeden('enter')
f.time.sleep(1)
f.jeden('spacja')
f.jeden('f12')
f.time.sleep(0.5)
f.kilka(4, 'down')
f.jeden('enter')
f.time.sleep(0.5)
f.kilka(2, 'down')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.dwa('shift', 't')
f.dwa('shift', 'o')
f.time.sleep(0.5)
f.jeden('spacja')
f.przeksztalc()
f.time.sleep(4)

for i in range(3):
    f.jeden('esc')
    f.time.sleep(0.3)
# asercja dla dokumentu WD

#sprawdz_poz_dok('T1', '1', '1111', 'WD/1  /24/000001')
#sprawdz_poz_dok('W1', '123', '22', 'WD/1  /24/000001')
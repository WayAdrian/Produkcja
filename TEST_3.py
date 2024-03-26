
import Functions as f
import datetime
import time
import pyautogui
import keyboard
import time
import pyperclip
import pytest
import sys
import datetime
import pyodbc

# 3.A - Dodaje towar T1


today = str(datetime.date.today())
dzis = today.replace("-", "")
f.pyautogui.PAUSE = 1
poczatek_testu = time.time()



f.aktywacja()


def sprawdz_art(symbol_art, rodz_art):
    zapytanie = "SELECT rodz_art, symbol_art FROM artykuly WHERE symbol_art = ? AND rodz_art = ?;"
    f.cursor.execute(zapytanie, (symbol_art, rodz_art))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{symbol_art}' o typie '{rodz_art}' nie istnieje w bazie danych!"
    return results

def sprawdz_tech(symbol_tec, symbol_wyr):
    zapytanie = "select symbol_tec, symbol_wyr from technolog WHERE symbol_tec = ? AND symbol_wyr = ?;"
    f.cursor.execute(zapytanie, (symbol_wyr, symbol_tec))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{symbol_wyr}' o typie '{symbol_tec}' nie istnieje w bazie danych!"
    return results

f.aktywacja()
# 2.C
f.operacje('p', 'a')
f.jeden('insert')
f.time.sleep(3)
f.tekst('T1')
f.kilka(1, 'tab')
f.tekst('T1')
f.kilka(11, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
#asercja
sprawdz_art('T1', 'T')

# Dodanie artykułu Surowiec S1 KG + Dostawca
f.jeden('insert')
f.time.sleep(1)
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('S1')
f.kilka(2, 'tab')
f.kilka(2, 'down')
f.kilka(9, 'tab')
f.tekst('KG')
f.kilka(1, 'tab')
for i in range(6):
    keyboard.press_and_release('ctrl+tab')
    f.time.sleep(0.1)
f.kilka(1, 'tab')
f.jeden('insert')
f.tekst('K0002') # tu bedzie później dostawca
f.kilka(2, 'tab')
f.tekst('55')
f.kilka(3, 'tab')
f.tekst('1234')
f.kilka(1, 'tab')
f.tekst('1234')
f.kilka(4, 'tab')
f.jeden('spacja')
f.dwa('shift', 'o')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
#asercja
sprawdz_art('S1', "S")


# Dodaje wyrób
# Uzupełniam d
# Dane podstawowe
f.jeden('insert')
f.time.sleep(2.5)
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('W1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(9, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
#Przeskakuje na karte Inne
f.zakladka(8)
# Zaznaczam checkbox "numery seryjne"
f.kilka(1, 'tab')
f.jeden('spacja')
f.kilka(1, 'tab')
f.jeden('spacja')
f.kilka(7, 'tab')
f.tekst('13')
f.kilka(1, 'tab') # zatwierdzam ale to do usuniecia jak w 007 bedzie poprawione partie
f.dwa('shift', 'o')
f.time.sleep(1)

sprawdz_art('W1', "W")
# checkbox obsługa partii
# for i in range(3):
#     keyboard.press_and_release('ctrl+tab')
#     f.time.sleep(0.1)
# f.kilka(7, 'tab'
# f.jeden('spacja')



#### DOdaje technologie i operacje !!!!!!!!!!
# Dodaje Półprodukt
f.jeden('insert')
f.time.sleep(2.5)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('PP1')
f.kilka(2, 'tab')
f.kilka(5, 'down')
f.kilka(9, 'tab')
f.tekst('SZT')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

sprawdz_art('PP1', "R")

f.time.sleep(1)
f.jeden('f12')
f.kilka(31, 'down')
f.jeden('enter')
# dane podstawowe technologii
f.dwa('ctrl', 'a')
f.tekst('PP1')
f.time.sleep(2)
f.kilka(1, 'tab')
f.tekst('PP1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(1, 'tab')

f.zakladka(1)

f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(1)
# nowa operacja
f.kilka(2, 'tab')
f.tekst('OP')
f.kilka(2, 'tab')
f.time.sleep(1)
f.zakladka(1)
f.time.sleep(1)
f.zakladka(3)
#zakładka wyroby gotowe
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
#zatwierdzenie operacji
f.dwa('shift', 'o')
f.time.sleep(1)
# wchodze jeszcze raz w operacje
f.jeden('f5')
f.time.sleep(1.5)
f.kilka(4, 'tab')
f.zakladka(3)
#zakładka surowce dodaje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(1)
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('3')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.kilka(11, 'tab')
f.kilka(1, 'down')
f.time.sleep(1)
f.dwa('shift', 't')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
# asercja
sprawdz_tech('PP1', 'PP1')

################################################  tchno dla wyrobu W
f.kilka(1, 'up')
f.jeden('f12')
f.time.sleep(0.5)
f.kilka(31, 'down')
f.jeden('enter')
f.dwa('ctrl', 'a')
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('W1')
f.kilka(2, 'tab')
f.kilka(1, 'down')
f.kilka(3, 'tab')
f.tekst('40')
# ZAKŁAdka Operacje!!!!!!!!
f.zakladka(1)
#zakładka operacje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(2)
f.jeden('insert')
f.time.sleep(2)
# nowa operacja
f.kilka(2, 'tab')
f.tekst('OP2')
f.kilka(2, 'tab')
f.zakladka(4)
#zakładka wyroby gotowe
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(2)
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
#zatwierdzenie operacji
f.dwa('shift', 'o')
f.time.sleep(1)
# wchodze jeszcze raz w operacje
f.jeden('f5')
f.time.sleep(1.5)
f.kilka(2, 'tab')
f.zakladka(3)
#zakładka surowce dodaje
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(0.5)
f.tekst('S1')
f.kilka(1, 'tab')
f.tekst('2')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

f.time.sleep(1)
f.jeden('insert')
f.time.sleep(0.5)
f.tekst('PP1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(1, 'tab')
f.dwa('shift', 'o')

f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('enter')
f.time.sleep(1)
f.dwa('shift', 'o')
f.time.sleep(1)
f.kilka(11, 'tab')
f.kilka(1, 'down')
f.time.sleep(1)
f.dwa('shift', 't')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('esc')

f.updatesql()
#asercja
sprawdz_tech('W1', 'W1')
sprawdz_tech('PP1', 'PP1')













# automatycznie generuj dok. rozchodowe   auto_dok_r
# automatycznie pobierz załącnziki
# autmatycznie uaktualnij stany mag. wyrobu auto_prz_p
# automatycznie uaktualnij stany mag. braków auto_prz_b
# automatycznie uaktualnij stany mag. odpadów auto_prz_o


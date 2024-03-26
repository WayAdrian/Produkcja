
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

# 4.A Dodaje dokument ZS w którym dodaje pozycje: W1 - 123 szt i T1 -1 sztuk, na dokumencie wskazuje odział
# 5.A
today = str(datetime.date.today())
dzis = today.replace("-", "")
f.pyautogui.PAUSE = 1
poczatek_testu = time.time()


termin = datetime.date.today()
jutro = termin + datetime.timedelta(days=1)
czas = jutro.strftime("%d-%m-%Y")

pojutro = termin + datetime.timedelta(days=30)
czas2 = pojutro.strftime("%d-%m-%Y")

def sprawdz_poz_dok(symbol_art, ilosc, cena, klucz_dok):
    zapytanie = "select symbol_art from poz_dok where symbol_art = ? and ilosc = ?  and cena=? and klucz_dok=?;"
    f.cursor.execute(zapytanie, (symbol_art, ilosc, cena, klucz_dok))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Pozycja dokumentu '{symbol_art}'  nie istnieje w bazie danych!"
    return results


f.aktywacja()
f.time.sleep(1)
f.dwa('shift', 'alt')
#f.kilka(17, 'down')
f.kilka(16, 'down')
f.kilka(1, 'right')
f.kilka(2, 'down')
f.jeden('enter')
f.jeden('insert')
f.time.sleep(2)
f.kilka(1, 'tab')
f.tekst('O-'+dzis)
f.kilka(1, 'tab')
f.jeden('enter')
f.time.sleep(1)
#f.kilka(7, 'tab')
f.kilka(6, 'tab')
f.tekst('OD001WARSZAWA')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
f.kilka(2, 'tab')
f.tekst(czas)
f.kilka(1, 'tab')
f.tekst(dzis)
f.kilka(5, 'tab')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(2)
f.tekst('W1')
f.kilka(1, 'tab')
f.tekst('123')
f.kilka(6, 'tab')
f.tekst('22')
f.kilka(3, 'tab')
f.dwa('shift', 'n')
f.time.sleep(1)
f.tekst('T1')
f.kilka(1, 'tab')
f.tekst('1')
f.kilka(6, 'tab')
f.tekst('1111')
f.kilka(3, 'tab')
f.dwa('shift', 'o')
f.time.sleep(0.5)
f.dwa('shift', 'o')
f.time.sleep(1)
f.jeden('esc')

sprawdz_poz_dok('T1', '1', '1111', 'ZS/1  /24/000001')
sprawdz_poz_dok('W1', '123', '22', 'ZS/1  /24/000001')


###################### TTP - Plan produkcyjny - konfiguracja
f.time.sleep(1)
f.dwa('shift', 'alt')
# f.kilka(21, 'down')
# f.kilka(1, 'right')
# f.kilka(28, 'down')
f.kilka(20, 'down')
f.kilka(1, 'right')
f.kilka(26, 'down')
f.jeden('enter')
f.jeden('insert')
f.time.sleep(2)
f.tekst('Plan')
f.kilka(1, 'down')
f.tekst('Plan')
f.kilka(2, 'tab')
f.dwa('shift', 'o')
f.updatesql2()
f.jeden('esc')

############ rejste PP ##############

f.operacje('o', 'd')
f.kilka(45, 'down')
f.kilka(2, 'right')

def sprPP():

    f.dwa('ctrl', 'c')
    rej = f.pyperclip.paste()
    if rej == 'Plan produkcji                                    ':
        f.jeden('enter')
        f.time.sleep(1)
        f.kilka(3, 'tab')

        f.dwa('ctrl', 'c')
        wla = f.pyperclip.paste()

        while wla != 'Konfiguracja                                                                                        ':

            f.kilka(1, 'down')
            f.dwa('ctrl', 'c')
            wla = f.pyperclip.paste()

        f.jeden('enter')
        f.time.sleep(1)
        f.jeden('enter')
        f.kilka(1, 'tab')
        f.dwa('shift', 'o')
    else:
        f.kilka(1, 'down')
        sprPP()

sprPP()
#################### Plan produkcji ############
f.time.sleep(1)
f.dwa('shift', 'alt')
#f.kilka(22, 'down')
f.kilka(21, 'down')
f.kilka(1, 'right')
f.kilka(10, 'down')
f.jeden('enter')
f.time.sleep(2)
f.jeden('insert')
f.time.sleep(3)
f.kilka(1, 'tab')
f.tekst(dzis)
f.kilka(2, 'tab')
f.tekst(czas)
f.kilka(1, 'tab')
f.tekst(czas2)
f.kilka(16, 'tab')
f.jeden('spacja')
f.dwa('shift', 'o')
f.jeden('esc')
f.jeden('esc')

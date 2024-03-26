
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

# 2.A Dodaje dostawce o nazwie D- 'dziś'
# 2.B Dodaje odbiorce o nazwei O-'dzis', dodaje mu  adres (oddział) o nazwie i adresie "Warszawa'

# 2.C Dodaje artykuł
f.nowytxt()
def sprawdz_kontrah(typ_ktr, nazwa_ktr):
    zapytanie = "SELECT typ_ktr, Nazwa_ktr FROM kontrah WHERE Nazwa_ktr = ? AND TYP_KTR = ?;"
    f.cursor.execute(zapytanie, (nazwa_ktr, typ_ktr))
    results = f.cursor.fetchall()
    print(results)
    assert results, f"Dokument '{nazwa_ktr}' o typie '{typ_ktr}' nie istnieje w bazie danych!"
    return results





today = str(datetime.date.today())
dzis = today.replace("-", "")
f.pyautogui.PAUSE = 1
poczatek_testu = time.time()



f.aktywacja()


# 2.A

f.operacje('p', 'k')
f.time.sleep(1)
f.jeden('insert')
f.time.sleep(3)
f.kilka(1, 'tab')
f.kilka(1, 'down') # typ dostawca
f.kilka(29, 'tab')
f.tekst('D-' + dzis)
f.kilka(2, 'tab')
f.dwa('shift', 'o')
f.time.sleep(1)
f.kilka(1, 'right')
f.dwa('ctrl', 'c')
dostawca = pyperclip.paste()
#asercja
D='D-' + dzis
sprawdz_kontrah('D',D)
time.sleep(1)


# 2.B
f.jeden('insert')
time.sleep(3)
f.kilka(30, 'tab')
O=f.tekst('O-' + dzis)
f.kilka(1, 'tab')
for i in range(2):
    keyboard.press_and_release('ctrl+tab')
f.time.sleep(0.5)
f.kilka(1, 'tab')
f.jeden('insert')
f.time.sleep(0.5)
f.kilka(1,'tab')
f.tekst('Warszawa')
for i in range(1):
    keyboard.press_and_release('ctrl+tab')
f.dwa('shift', 'o')
f.kilka(1, 'tab')
f.dwa('shift', 'o')
time.sleep(1)
f.dwa('ctrl', 'c')
odbiorca = pyperclip.paste()
f.jeden('esc')
#asercja
O='O-' + dzis
sprawdz_kontrah('D',D)
sprawdz_kontrah('O',O)


f.doplikutxt('Dodano dostawe o symbolu: '+ dostawca+
             ' oraz nazwie: '+ D)
f.doplikutxt('Dodano odbiorce o symbolu '+ odbiorca + ' oraz nazwie '+ O)









